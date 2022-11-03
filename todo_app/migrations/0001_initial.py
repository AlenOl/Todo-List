# Generated by Django 4.1.3 on 2022-11-02 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=69)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=255)),
                ('datetime', models.DateTimeField()),
                ('deadline', models.DateTimeField()),
                ('is_done', models.BooleanField()),
                ('tags', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ['deadline', 'datetime'],
            },
        ),
    ]
