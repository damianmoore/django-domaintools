from datetime import datetime, date, timedelta
import string
import random
from django.db import models
import expiry

DAYS_BETWEEN_RECHECK = 7


class Domain(models.Model):
    id = models.CharField(max_length=50, primary_key=True, help_text='Domain name')
    expiry_date = models.DateField(blank=True, null=True)
    last_check = models.DateTimeField(blank=True, null=True)

    def update_expiry_date(self, save=True):
        self.expiry_date = expiry.domain_renewal_date(self.id)
        self.last_check = datetime.now()
        if save:
            self.save()

    def days_remaining(self):
        if not self.last_check \
            or (date.today() - self.last_check.date()).days > 7 \
            or self.expiry_date - timedelta(days=3) < date.today():
            self.update_expiry_date()
        if not self.expiry_date:
            return 0
        return expiry.get_days_remaining(self.expiry_date)

    def save(self):
        self.update_expiry_date(save=False)
        super(Domain, self).save()

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
