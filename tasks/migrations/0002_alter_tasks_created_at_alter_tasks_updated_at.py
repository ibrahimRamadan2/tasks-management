# Generated by Django 5.0.6 on 2024-06-08 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
