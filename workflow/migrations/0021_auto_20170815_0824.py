# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-15 15:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0020_auto_20170815_0732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partner',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='stakeholder_partner', to='workflow.StakeholderType'),
        ),
    ]
