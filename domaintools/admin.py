from django.contrib import admin
from models import Domain, DnsRecord


class DomainAdmin(admin.ModelAdmin):
    list_display = ('id', 'expiry_date', 'days_remaining', 'last_check',)
    ordering = ('expiry_date',)

admin.site.register(Domain, DomainAdmin)


class DnsRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'ip', 'key', 'last_change',)
    ordering = ('id',)

admin.site.register(DnsRecord, DnsRecordAdmin)
