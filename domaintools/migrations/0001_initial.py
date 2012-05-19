# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Domain'
        db.create_table('domaintools_domain', (
            ('id', self.gf('django.db.models.fields.CharField')(max_length=50, primary_key=True)),
            ('expiry_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('last_check', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal('domaintools', ['Domain'])


    def backwards(self, orm):
        
        # Deleting model 'Domain'
        db.delete_table('domaintools_domain')


    models = {
        'domaintools.domain': {
            'Meta': {'object_name': 'Domain'},
            'expiry_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True'}),
            'last_check': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['domaintools']
