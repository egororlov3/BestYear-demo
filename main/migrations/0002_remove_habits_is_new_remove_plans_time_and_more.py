# Generated by Django 5.1.4 on 2025-01-02 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='habits',
            name='is_new',
        ),
        migrations.RemoveField(
            model_name='plans',
            name='time',
        ),
        migrations.AddField(
            model_name='habits',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='habits',
            name='done',
            field=models.BooleanField(default=True, verbose_name='Выполнено'),
        ),
    ]
