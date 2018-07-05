# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appform', '0002_auto_20180503_0657'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dogs',
            old_name='idade',
            new_name='observador',
        ),
        migrations.RenameField(
            model_name='dogs',
            old_name='nome',
            new_name='od',
        ),
        migrations.RemoveField(
            model_name='dogs',
            name='raca',
        ),
    ]
