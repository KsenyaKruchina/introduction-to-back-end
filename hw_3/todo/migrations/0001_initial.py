# Generated by Django 5.0.2 on 2024-02-20 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Thing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('due_date', models.DateField(auto_created=True, auto_now=True, null=True)),
                ('title', models.CharField(default='', max_length=255)),
                ('description', models.CharField(default='', max_length=3000)),
                ('status', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Thing',
                'verbose_name_plural': 'Things',
            },
        ),
    ]
