# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import adhocracy4.images.validators


class Migration(migrations.Migration):

    dependencies = [
        ('euth_organisations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organisation',
            name='image',
            field=models.ImageField(blank=True, upload_to='organisations/images', validators=[adhocracy4.images.validators.validate_hero_image]),
        ),
        migrations.AlterField(
            model_name='organisation',
            name='logo',
            field=models.ImageField(blank=True, upload_to='organisations/logos', validators=[adhocracy4.images.validators.validate_logo]),
        ),
    ]
