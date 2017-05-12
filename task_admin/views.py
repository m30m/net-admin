from django.http import HttpResponse
from django.http.response import JsonResponse
from django.views.generic import TemplateView, View
from django_filters.rest_framework.backends import DjangoFilterBackend
from rest_framework import mixins
from rest_framework.decorators import detail_route
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet, GenericViewSet

from task_admin.models import TaskRunSet, Task, TaskRun
from task_admin.serializers import TaskRunSetSerializer, TaskSerializer, TaskRunSerializer
from task_admin.task_render import get_all_possible_vars, render_preview


class RenderPreviewView(View):
    def get(self, request):
        response = []
        for template, rendered in get_all_possible_vars().items():
            response.append({'template': template, 'rendered': rendered})
        return JsonResponse(response, safe=False)


class TaskRunSetsView(TemplateView):
    template_name = "task_admin/taskrunsets.html"


class TaskRunsView(TemplateView):
    template_name = "task_admin/taskruns.html"


class TasksAPI(ModelViewSet):
    serializer_class = TaskSerializer
    filter_fields = ('id', 'name', 'author', 'is_local')
    queryset = Task.objects.order_by('-created_at')


class Pagination(PageNumberPagination):
    page_size = 500
    page_size_query_param = 'page_size'


class TaskRunsAPI(ReadOnlyModelViewSet, mixins.ListModelMixin):
    serializer_class = TaskRunSerializer
    filter_fields = ('desk', 'contestant', 'node', 'run_set', 'status')
    queryset = TaskRun.objects.select_related('run_set', 'contestant', 'node', 'desk').filter(
        run_set__deleted=False).order_by(
        '-created_at')
    pagination_class = Pagination

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response.data['pagination'] = self.paginator.get_html_context()
        return response

    @detail_route(methods=['post'])
    def stop(self, request, pk):
        task_run = self.get_object()
        result = task_run.get_celery_result()
        result.revoke()
        return HttpResponse('', status=204)


class TaskRunSetFilterBackend(DjangoFilterBackend):
    def filter_queryset(self, request, queryset, view):
        filter_queryset = super().filter_queryset(request, queryset, view)
        runset_state = request.query_params.get('state', None)
        if runset_state == 'finished':
            return [runset for runset in filter_queryset if runset.is_finished]
        return filter_queryset


class TaskRunSetsAPI(mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.ListModelMixin,
                     mixins.DestroyModelMixin,
                     GenericViewSet):
    filter_backends = (TaskRunSetFilterBackend,)
    pagination_class = Pagination
    serializer_class = TaskRunSetSerializer
    filter_fields = ('is_local',)
    queryset = TaskRunSet.objects.prefetch_related('taskruns', 'taskruns__desk', 'taskruns__node',
                                                   'taskruns__contestant').select_related('owner').filter(
        deleted=False).order_by('-created_at')
    max_page_size = 10000

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response.data['pagination'] = self.paginator.get_html_context()
        return response

    def perform_destroy(self, instance):
        instance.deleted = True
        # TODO: stop all remaining tasks
        instance.save()

    @detail_route(methods=['post'])
    def stop(self, request, pk):
        task_runset = self.get_object()
        for task_run in task_runset.taskruns.all():
            result = task_run.get_celery_result()
            result.revoke()
            # TODO: check if successful , don't change the state
            task_run.status = 'REVOKED'
            task_run.save()
        return HttpResponse('', status=204)
