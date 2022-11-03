from django.urls import path

from todo_app.views import TaskListView, TagListView, TaskCreateView, toggle_done, TaskUpdateView, TaskDeleteView, \
    TagsCreateView, TagsDeleteView, TagsUpdateView

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("tags/", TagListView.as_view(), name="tags-list"),
    path("task-create/", TaskCreateView.as_view(), name="task-create"),
    path("<int:pk>/toggle-done/", toggle_done, name="toggle-done"),
    path("<int:pk>/task-update/", TaskUpdateView.as_view(), name="task-update"),
    path("<int:pk>/task-delete/", TaskDeleteView.as_view(), name="task-delete"),
    path(
        "tags/tags-create/",
        TagsCreateView.as_view(),
        name="tag-create",
    ),
    path(
        "tags/<int:pk>/tags-update/",
        TagsUpdateView.as_view(),
        name="tag-update",
    ),
    path(
        "tags/<int:pk>/tags-delete/",
        TagsDeleteView.as_view(),
        name="tag-delete",
    ),
]

app_name = "todo_app"
