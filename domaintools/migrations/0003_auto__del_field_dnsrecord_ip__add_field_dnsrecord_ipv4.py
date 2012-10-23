# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'DnsRecord.ip'
        db.delete_column('domaintools_dnsrecord', 'ip')

        # Adding field 'DnsRecord.ipv4'
        db.add_column('domaintools_dnsrecord', 'ipv4',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=16, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'DnsRecord.ip'
        db.add_column('domaintools_dnsrecord', 'ip',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=16, blank=True),
                      keep_default=False)

        # Deleting field 'DnsRecord.ipv4'
        db.delete_column('domaintools_dnsrecord', 'ipv4')


    models = {
        'domaintools.dnsrecord': {
            'Meta': {'object_name': 'DnsRecord'},
            'id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True'}),
            'ipv4': ('django.db.models.fields.CharField', [], {'max_length': '16', 'blank': 'True'}),
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