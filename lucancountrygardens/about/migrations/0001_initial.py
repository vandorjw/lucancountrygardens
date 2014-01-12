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
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=255)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(blank=True, max_length=100, null=True)),
            ('short_content', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('sort', self.gf('django.db.models.fields.IntegerField')(unique=True, default=0)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('meta_description', self.gf('django.db.models.fields.CharField')(blank=True, max_length=300)),
            ('meta_keywords', self.gf('django.db.models.fields.CharField')(blank=True, max_length=300)),
        ))
        db.send_create_signal('about', ['About'])

        # Adding model 'ArticleSection'
        db.create_table('about_articlesection', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('about', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['about.About'])),
            ('sort', self.gf('django.db.models.fields.IntegerField')(unique=True, default=0)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(blank=True, max_length=100, null=True)),
            ('image_caption', self.gf('django.db.models.fields.CharField')(blank=True, max_length=255)),
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
            'Meta': {'object_name': 'About', 'ordering': "['sort', 'name']"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'blank': 'True', 'max_length': '100', 'null': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'meta_description': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '300'}),
            'meta_keywords': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '300'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'short_content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '255'}),
            'sort': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'default': '0'})
        },
        'about.articlesection': {
            'Meta': {'object_name': 'ArticleSection', 'ordering': "['sort']"},
            'about': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['about.About']"}),
            'article_section': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'blank': 'True', 'max_length': '100', 'null': 'True'}),
            'image_caption': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '255'}),
            'section_header': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'sort': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'default': '0'})
        }
    }

    complete_apps = ['about']