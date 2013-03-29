from datetime import datetime
import string
import random
from django.db import models
import expiry

DAYS_BETWEEN_RECHECK = 7


class Domain(models.Model):
    id = models.CharField(max_length=50, primary_key=True, help_text='Domain name')
    expiry_date = models.DateField(blank=True, null=True)
    last_check = models.DateTimeField(blank=True, null=True)

    def update_expiry_date(self):
        self.expiry_date = expiry.domain_renewal_date(self.id)
        self.last_check = datetime.now()
        self.save()

    def days_remaining(self):
        if not self.last_check or (datetime.now() - self.last_check).days > 7:
            self.update_expiry_date()
        if not self.expiry_date:
            return 0
        return expiry.get_days_remaining(self.expiry_date)

    def save(self):
        super(Domain, self).save()
        self.days_remaining()

    def __unicode__(self):
        return self.id


class DnsRecord(models.Model):
    id = models.CharField(max_length=50, primary_key=True, help_text='Domain/subdomain name')
    ip = models.CharField(max_length=16, blank=True)
    key = models.CharField(max_length=50, blank=True)
    last_change = models.DateTimeField(blank=True, null=True)

    def generate_key(self, size=50, chars=string.ascii_uppercase + string.ascii_lowercase + string.digits):
        return ''.join(random.choice(chars) for x in range(size))

    def save(self):
        if not self.key:
            self.key = self.generate_key()
        self.last_change = datetime.now()
        super(DnsRecord, self).save()
