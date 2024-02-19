from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from appTodo.models import Job
from appTodo.forms import JobForm
import requests
# from django.core.cache import cache
from django.views.decorators.cache import cache_page
from . import tasks


class JobsView(LoginRequiredMixin, ListView):
    template_name = "appTodo/job_list.html"
    context_object_name = "jobs"

    def get_queryset(self):
        return Job.objects.filter(user=self.request.user.profile).order_by(
            "-created_date"
        )

    def post(self, request):
        form = JobForm(self.request.POST)
        if form.is_valid():
            form.save()
        return redirect("appTodo:jobs")


class JobDeleteView(LoginRequiredMixin, DeleteView):
    success_url = reverse_lazy("appTodo:jobs")
    model = Job


class JobUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "appTodo/job_update.html"
    model = Job
    fields = ["name", "status"]
    success_url = "/todo/jobs/"


# for background processing learning
def test_send_email(request):
    tasks.task2.delay()
    return HttpResponse("<h1>email sent</h1>")


# for learning cache usage
# def test_delay_3(request):
#     if cache.get('test_delay_3') is None:
#         response = requests.get('https://de1316b2-9246-42d9-9225-609e057b47ca.mock.pstmn.io/test/delay/3')
#         cache.set('test_delay_3', response.json(), 30)
#     return JsonResponse(cache.get('test_delay_3'))
@cache_page(30)
def test_delay_3(request):
    response = requests.get('https://de1316b2-9246-42d9-9225-609e057b47ca.mock.pstmn.io/test/delay/3')
    return JsonResponse(response.json())
