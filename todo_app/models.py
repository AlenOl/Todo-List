from django.db import models


class Tags(models.Model):
    name = models.CharField(max_length=69)


class Task(models.Model):
    content = models.CharField(max_length=255)
    datetime = models.CharField(max_length=69)
    deadline = models.CharField(max_length=69, blank=True)
    is_done = models.BooleanField()
    tags = models.ManyToManyField(Tags)

    class Meta:
        ordering = ["deadline", "datetime"]



# content - describes what you should do.
# datetime, when a task was created
# optional deadline datetime if a task should be done until some datetime
# the boolean field that marks if the task is done or not
# tags that are relevant for this task
# Tag - a tag symbolizes the theme of the task and consists only of a name.
