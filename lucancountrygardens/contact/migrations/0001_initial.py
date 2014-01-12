# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'OperationHours'
        db.create_table('contact_operationhours', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('days', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('display_order', self.gf('django.db.models.fields.IntegerField')(max_length=1, default=0, unique=True)),
        ))
        db.send_create_signal('contact', ['OperationHours'])


    def backwards(self, orm):
        # Deleting model 'OperationHours'
        db.delete_table('contact_operationhours')


    models = {
        'contact.operationhours': {
            'Meta': {'ordering': "['display_order']", 'object_name': 'OperationHours'},
            'days': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'display_order': ('django.db.models.fields.IntegerField', [], {'max_length': '1', 'default': '0', 'unique': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['contact']