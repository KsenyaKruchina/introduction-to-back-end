# Generated by Django 5.0.2 on 2024-02-14 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='thing',
            name='duration',
        ),
        migrations.RemoveField(
            model_name='thing',
            name='producer',
        ),
        migrations.AddField(
            model_name='thing',
            name='due_date',
            field=models.DateField(default='', max_length=3000),
        ),
        migrations.AddField(
            model_name='thing',
            name='status',
            field=models.BooleanField(default=0),
        ),
    ]
