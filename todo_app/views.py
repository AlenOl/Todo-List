from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from todo_app.forms import TaskForm
from todo_app.models import Task, Tags


class TaskListView(generic.ListView):
    model = Task


class TagListView(generic.ListView):
    model = Tags


class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("todo_app:task-list")


def toggle_done(request, pk):
    if Task.objects.get(id=pk):
        Task.is_done = False
    else:
        Task.is_done = True

    return HttpResponseRedirect(reverse_lazy("todo_app:task-list", args=[pk]))


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("todo_app:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("todo_app:task-list")


class TagsCreateView(generic.CreateView):
    model = Tags
    fields = "__all__"
    success_url = reverse_lazy("todo_app:tags-list")


class TagsUpdateView(generic.UpdateView):
    model = Tags
    fields = "__all__"
    success_url = reverse_lazy("todo_app:tags-list")


class TagsDeleteView(generic.DeleteView):
    model = Tags
    fields = "__all__"
    success_url = reverse_lazy("todo_app:tags-list")
