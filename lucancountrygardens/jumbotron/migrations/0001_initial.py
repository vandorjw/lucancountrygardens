# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Slide'
        db.create_table('jumbotron_slide', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('headline', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('caption', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('sort', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('jumbotron', ['Slide'])


    def backwards(self, orm):
        # Deleting model 'Slide'
        db.delete_table('jumbotron_slide')


    models = {
        'jumbotron.slide': {
            'Meta': {'ordering': "['sort']", 'object_name': 'Slide'},
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'headline': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'sort': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['jumbotron']