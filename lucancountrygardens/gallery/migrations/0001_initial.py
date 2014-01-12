# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Gallery'
        db.create_table('gallery_gallery', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('meta_description', self.gf('django.db.models.fields.CharField')(blank=True, max_length=255)),
            ('meta_keywords', self.gf('django.db.models.fields.CharField')(blank=True, max_length=255)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('gallery', ['Gallery'])

        # Adding model 'GalleryImage'
        db.create_table('gallery_galleryimage', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('gallery', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gallery.Gallery'])),
            ('image', self.gf('django.db.models.fields.files.ImageField')(null=True, blank=True, max_length=100)),
            ('caption', self.gf('django.db.models.fields.CharField')(blank=True, max_length=255)),
            ('sort', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('gallery', ['GalleryImage'])


    def backwards(self, orm):
        # Deleting model 'Gallery'
        db.delete_table('gallery_gallery')

        # Deleting model 'GalleryImage'
        db.delete_table('gallery_galleryimage')


    models = {
        'gallery.gallery': {
            'Meta': {'ordering': "['name']", 'object_name': 'Gallery'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'meta_description': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '255'}),
            'meta_keywords': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '255'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '255'})
        },
        'gallery.galleryimage': {
            'Meta': {'ordering': "['sort']", 'object_name': 'GalleryImage'},
            'caption': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '255'}),
            'gallery': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gallery.Gallery']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'null': 'True', 'blank': 'True', 'max_length': '100'}),
            'sort': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['gallery']