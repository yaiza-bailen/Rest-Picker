# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Restaurant.map'
        db.add_column('restaurants_restaurant', 'map',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Restaurant.map'
        db.delete_column('restaurants_restaurant', 'map')


    models = {
        'restaurants.food': {
            'Meta': {'object_name': 'Food'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True'})
        },
        'restaurants.restaurant': {
            'Meta': {'object_name': 'Restaurant'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'desc': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'food': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['restaurants.Food']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'map': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True'}),
            'menu': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True'}),
            'post_code': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'town': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['restaurants.Town']"}),
            'votes': ('django.db.models.fields.IntegerField', [], {'default': '4'}),
            'web': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'restaurants.town': {
            'Meta': {'object_name': 'Town'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['restaurants']