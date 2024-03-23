# Generated by Django 5.0.2 on 2024-02-10 17:26

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
                ('title', models.CharField(default='', max_length=255)),
                ('description', models.CharField(default='', max_length=3000)),
                ('producer', models.CharField(default='', max_length=3000)),
                ('duration', models.IntegerField(default=0)),
            ],
        ),
    ]
