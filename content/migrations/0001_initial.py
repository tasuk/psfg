from __future__ import unicode_literals
from django.db import models, migrations
from cms.api import create_page, add_plugin, publish_page
from django.contrib.auth.models import User
from os.path import dirname
import yaml

def create_admin(apps, schema_editor):
    User.objects.create_superuser('admin', 'admin@example.com', 'admin')

def insert_sites(apps, schema_editor):
    """Populate the sites model"""
    Site = apps.get_model('sites', 'Site')
    Site.objects.all().delete()
    Site.objects.create(domain='peopleskillsforgeeks.com', name='psfg')

def populate(page, data):
    for key in data:
        add_plugin(
            placeholder=page.placeholders.get(slot=key),
            plugin_type='TextPlugin',
            language='en',
            body=data[key],
        )

    if page.is_published('en'):
        publish_page(page, User.objects.all()[0], 'en')

def insert_cms_pages(apps, schema_editor):
    """Populate cms with structure and dummy pages"""

    homepage = create_page(
        title='Homepage',
        template='content/home.html',
        language='en',
        published=True,
    )

    with open(dirname(__file__) + '/data/homepage.yaml') as data_file:
        populate(homepage, yaml.safe_load(data_file))

    articlelist = create_page(
        title='Articles',
        template='content/articlelist.html',
        language='en',
        parent=homepage,
        published=True,
    )

    base = create_page(
        title='Base Article - do not delete, copy to create articles',
        template='content/article.html',
        language='en',
        parent=articlelist,
        in_navigation=True,
        published=False,
    )
    populate(base, { 'article': 'Hello, world!' })
    test = create_page(
        title='Test Article',
        template='content/article.html',
        language='en',
        parent=articlelist,
        in_navigation=True,
        published=True,
    )
    populate(test, { 'article': '<h2>Subheading</h2><p>Some text</p>' })
    another = create_page(
        title='Another Test',
        template='content/article.html',
        language='en',
        parent=articlelist,
        in_navigation=True,
        published=True,
    )
    populate(another, { 'article': 'A journey of a thousand miles begins with a single step.' })


class Migration(migrations.Migration):
    dependencies = [
        ('sites', '0001_initial'),
        ('menus', '0001_initial'),
        ('djangocms_text_ckeditor', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_admin),
        migrations.RunPython(insert_sites),
        migrations.RunPython(insert_cms_pages),
    ]
