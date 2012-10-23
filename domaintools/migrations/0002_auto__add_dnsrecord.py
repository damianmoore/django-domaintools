# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'DnsRecord'
        db.create_table('domaintools_dnsrecord', (
            ('id', self.gf('django.db.models.fields.CharField')(max_length=50, primary_key=True)),
            ('ip', self.gf('django.db.models.fields.CharField')(max_length=16, blank=True)),
            ('key', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('last_change', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal('domaintools', ['DnsRecord'])


    def backwards(self, orm):
        # Deleting model 'DnsRecord'
        db.delete_table('domaintools_dnsrecord')


    models = {
        'domaintools.dnsrecord': {
            'Meta': {'object_name': 'DnsRecord'},
            'id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '16', 'blank': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'last_change': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'})
        },
        'domaintools.domain': {
            'Meta': {'object_name': 'Domain'},
            'expiry_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True'}),
            'last_check': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['domaintools']