# Generated by Django 4.1.3 on 2022-11-03 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0003_alter_task_datetime_alter_task_deadline'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='tags',
        ),
        migrations.AddField(
            model_name='task',
            name='tags',
            field=models.ManyToManyField(to='todo_app.tags'),
        ),
    ]
