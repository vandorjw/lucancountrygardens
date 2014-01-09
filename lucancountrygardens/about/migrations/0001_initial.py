# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'About'
        db.create_table('about_about', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, unique=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=255, unique=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('short_content', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('sort', self.gf('django.db.models.fields.IntegerField')(default=0, unique=True)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('meta_description', self.gf('django.db.models.fields.CharField')(max_length=300, blank=True)),
            ('meta_keywords', self.gf('django.db.models.fields.CharField')(max_length=300, blank=True)),
        ))
        db.send_create_signal('about', ['About'])

        # Adding model 'ArticleSection'
        db.create_table('about_articlesection', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('about', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['about.About'])),
            ('sort', self.gf('django.db.models.fields.IntegerField')(default=0, unique=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('image_caption', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('section_header', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('article_section', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('about', ['ArticleSection'])


    def backwards(self, orm):
        # Deleting model 'About'
        db.delete_table('about_about')

        # Deleting model 'ArticleSection'
        db.delete_table('about_articlesection')


    models = {
        'about.about': {
            'Meta': {'ordering': "['sort', 'name']", 'object_name': 'About'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'meta_description': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'meta_keywords': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True'}),
            'short_content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255', 'unique': 'True'}),
            'sort': ('django.db.models.fields.IntegerField', [], {'default': '0', 'unique': 'True'})
        },
        'about.articlesection': {
            'Meta': {'ordering': "['sort']", 'object_name': 'ArticleSection'},
            'about': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['about.About']"}),
            'article_section': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'image_caption': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'section_header': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'sort': ('django.db.models.fields.IntegerField', [], {'default': '0', 'unique': 'True'})
        }
    }

    complete_apps = ['about']