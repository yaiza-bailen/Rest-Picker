# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Restaurant'
        db.create_table('restaurants_restaurant', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('desc', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('menu', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('web', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('post_code', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('food', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['restaurants.Food'])),
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['restaurants.City'])),
        ))
        db.send_create_signal('restaurants', ['Restaurant'])

        # Adding model 'Food'
        db.create_table('restaurants_food', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal('restaurants', ['Food'])

        # Adding model 'City'
        db.create_table('restaurants_city', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal('restaurants', ['City'])


    def backwards(self, orm):
        # Deleting model 'Restaurant'
        db.delete_table('restaurants_restaurant')

        # Deleting model 'Food'
        db.delete_table('restaurants_food')

        # Deleting model 'City'
        db.delete_table('restaurants_city')


    models = {
        'restaurants.city': {
            'Meta': {'object_name': 'City'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'restaurants.food': {
            'Meta': {'object_name': 'Food'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'restaurants.restaurant': {
            'Meta': {'object_name': 'Restaurant'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['restaurants.City']"}),
            'desc': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'food': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['restaurants.Food']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'menu': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'post_code': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'web': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['restaurants']