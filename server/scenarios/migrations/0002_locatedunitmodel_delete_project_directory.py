# Generated by Django 5.0.6 on 2024-07-12 18:49

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scenarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LocatedUnitModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='scenarios.locatedunitmodel')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='Project',
        ),
        migrations.CreateModel(
            name='Directory',
            fields=[
                ('locatedunitmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='scenarios.locatedunitmodel')),
            ],
            options={
                'abstract': False,
            },
            bases=('scenarios.locatedunitmodel',),
        ),
    ]
