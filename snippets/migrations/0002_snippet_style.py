# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='snippet',
            name='style',
            field=models.CharField(default=b'friendly', max_length=100, choices=[(b'autumn', b'autumn'), (b'borland', b'borland'), (b'bw', b'bw'), (b'colorful', b'colorful'), (b'default', b'default'), (b'emacs', b'emacs'), (b'friendly', b'friendly'), (b'fruity', b'fruity'), (b'igor', b'igor'), (b'manni', b'manni'), (b'monokai', b'monokai'), (b'murphy', b'murphy'), (b'native', b'native'), (b'paraiso-dark', b'paraiso-dark'), (b'paraiso-light', b'paraiso-light'), (b'pastie', b'pastie'), (b'perldoc', b'perldoc'), (b'rrt', b'rrt'), (b'tango', b'tango'), (b'trac', b'trac'), (b'vim', b'vim'), (b'vs', b'vs'), (b'xcode', b'xcode')]),
        ),
    ]
