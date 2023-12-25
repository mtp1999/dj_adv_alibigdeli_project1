from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from appTodo.models import Job
from appTodo.forms import JobForm
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


def test_send_email(request):
    tasks.task2.delay()
    return HttpResponse("<h1>email sent</h1>")
