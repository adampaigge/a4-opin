# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('euth_projects', '0007_fix_typo_in_is_public_helptext'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('modified', models.DateTimeField(blank=True, null=True, editable=False)),
                ('enabled', models.BooleanField(default=True)),
                ('creator', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(to='euth_projects.Project')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='follow',
            unique_together=set([('project', 'creator')]),
        ),
    ]
