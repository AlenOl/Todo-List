from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

from todo_app.forms import TaskForm
from todo_app.models import Task, Tags


class TaskListView(generic.ListView):
    model = Task
    context_object_name = "task_list"
    template_name = "todo_app/task_list.html"


class TagListView(generic.ListView):
    model = Tags


class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("todo_app:task-list")


def toggle_done(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_done = not task.is_done
    task.save()

    return HttpResponseRedirect(reverse_lazy("todo_app:task-list"))


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
    queryset = Task.objects.all().prefetch_related("tags")
    success_url = reverse_lazy("todo_app:tags-list")


class TagsUpdateView(generic.UpdateView):
    model = Tags
    fields = "__all__"
    success_url = reverse_lazy("todo_app:tags-list")


class TagsDeleteView(generic.DeleteView):
    model = Tags
    fields = "__all__"
    success_url = reverse_lazy("todo_app:tags-list")
