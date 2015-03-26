from __future__ import unicode_literals
from django.db import models, migrations
from cms.api import create_page, add_plugin

def insert_sites(apps, schema_editor):
    """Populate the sites model"""
    Site = apps.get_model('sites', 'Site')
    Site.objects.all().delete()
    Site.objects.create(domain='peopleskillsforgeeks.com', name='psfg')

def insert_cms_pages(apps, schema_editor):
    """Populate cms with structure and dummy pages"""

    homepage = create_page(
        title='Homepage',
        template='article.html',
        language='en',
        published=True,
    )
    articlelist = create_page(
        title='Articles',
        template='articlelist.html',
        language='en',
        parent=homepage,
        published=True,
    )

    base = create_page(
        title='Base Article - do not delete, copy to create articles',
        template='article.html',
        language='en',
        parent=articlelist,
        in_navigation=True,
        published=False,
    )
    test = create_page(
        title='Test Article',
        template='article.html',
        language='en',
        parent=articlelist,
        in_navigation=True,
        published=True,
    )
    another = create_page(
        title='Another Test',
        template='article.html',
        language='en',
        parent=articlelist,
        in_navigation=True,
        published=True,
    )

    for article in [ base, test, another ]:
        add_plugin(
            placeholder=article.placeholders.get(slot='article'),
            plugin_type='TextPlugin',
            language='en',
            body='Hello, world.',
        )


class Migration(migrations.Migration):
    dependencies = [
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(insert_sites),
        migrations.RunPython(insert_cms_pages),
    ]
