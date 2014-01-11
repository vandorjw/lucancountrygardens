# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Slide.headline'
        db.add_column('jumbotron_slide', 'headline',
                      self.gf('django.db.models.fields.CharField')(blank=True, default='', max_length=255),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Slide.headline'
        db.delete_column('jumbotron_slide', 'headline')


    models = {
        'jumbotron.slide': {
            'Meta': {'object_name': 'Slide', 'ordering': "['sort']"},
            'caption': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '255'}),
            'headline': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'blank': 'True', 'null': 'True', 'max_length': '100'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'sort': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['jumbotron']