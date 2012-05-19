from datetime import datetime
from django.db import models
import expiry

DAYS_BETWEEN_RECHECK = 7

class Domain(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    expiry_date = models.DateField(blank=True, null=True)
    last_check = models.DateTimeField(blank=True, null=True)

    def update_expiry_date(self):
        self.expiry_date = expiry.domain_renewal_date(self.id)
        self.last_check = datetime.now()
        self.save()

    def days_remaining(self):
#        import pdb; pdb.set_trace()
        if not self.last_check or (datetime.now() - self.last_check).days > 7:
            self.update_expiry_date()
        return expiry.get_days_remaining(self.expiry_date)

    def save(self):
        super(Domain, self).save()
        self.days_remaining()

    def __unicode__(self):
        return self.id

