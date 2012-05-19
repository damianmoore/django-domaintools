from django.contrib import admin
from models import Domain

class DomainAdmin(admin.ModelAdmin):
    list_display = ('id', 'expiry_date', 'days_remaining', 'last_check',)
    ordering = ('expiry_date',)

admin.site.register(Domain, DomainAdmin)

