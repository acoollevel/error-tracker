# Generated by Django 2.2.7 on 2019-11-29 07:29

from django.db import migrations, models
import error_tracker.libs.mixins


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ErrorModel',
            fields=[
                ('hash', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('host', models.CharField(max_length=1024)),
                ('path', models.CharField(max_length=4096)),
                ('method', models.CharField(max_length=64)),
                ('request_data', models.TextField()),
                ('exception_name', models.CharField(max_length=256)),
                ('traceback', models.TextField()),
                ('count', models.IntegerField(default=0)),
                ('created_on', models.DateTimeField(auto_now=True)),
                ('last_seen', models.DateTimeField(auto_now=True, db_index=True)),
            ],
            options={
                'db_table': 'exceptions',
                'swappable': 'APP_ERROR_DB_MODEL',
            },
            bases=(models.Model, error_tracker.libs.mixins.ModelMixin),
        ),
    ]
