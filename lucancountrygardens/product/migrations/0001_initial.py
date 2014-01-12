# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Category'
        db.create_table('product_category', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, null=True, to=orm['product.Category'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, unique=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=255, unique=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('sort', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=2, unique=True)),
            ('meta_description', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('meta_keywords', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True, null=True)),
        ))
        db.send_create_signal('product', ['Category'])

        # Adding model 'Product'
        db.create_table('product_product', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=255, unique=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, null=True, to=orm['product.Category'])),
            ('meta_description', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('meta_keywords', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('is_featured', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('price', self.gf('django.db.models.fields.DecimalField')(decimal_places=2, max_digits=8)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('product', ['Product'])

        # Adding model 'ProductImage'
        db.create_table('product_productimage', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['product.Product'])),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True, null=True)),
            ('caption', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('sort', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('product', ['ProductImage'])


    def backwards(self, orm):
        # Deleting model 'Category'
        db.delete_table('product_category')

        # Deleting model 'Product'
        db.delete_table('product_product')

        # Deleting model 'ProductImage'
        db.delete_table('product_productimage')


    models = {
        'product.category': {
            'Meta': {'ordering': "['sort']", 'object_name': 'Category'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True', 'null': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'meta_description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'meta_keywords': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'null': 'True', 'to': "orm['product.Category']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255', 'unique': 'True'}),
            'sort': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '2', 'unique': 'True'})
        },
        'product.product': {
            'Meta': {'ordering': "['name']", 'object_name': 'Product'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'null': 'True', 'to': "orm['product.Category']"}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'meta_description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'meta_keywords': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'price': ('django.db.models.fields.DecimalField', [], {'decimal_places': '2', 'max_digits': '8'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255', 'unique': 'True'})
        },
        'product.productimage': {
            'Meta': {'ordering': "['sort']", 'object_name': 'ProductImage'},
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True', 'null': 'True'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['product.Product']"}),
            'sort': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['product']