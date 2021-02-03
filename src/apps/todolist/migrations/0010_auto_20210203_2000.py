# Generated by Django 3.1.5 on 2021-02-03 13:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0009_auto_20210203_1952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='priority',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='todolist.priority'),
        ),
    ]
