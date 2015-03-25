from __future__ import unicode_literals
from django.db import models, migrations

def insert_sites(apps, schema_editor):
    """Populate the sites model"""
    Site = apps.get_model('sites', 'Site')
    Site.objects.all().delete()
    Site.objects.create(domain='peopleskillsforgeeks.com', name='psfg')

class Migration(migrations.Migration):
    dependencies = [
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(insert_sites),
    ]
