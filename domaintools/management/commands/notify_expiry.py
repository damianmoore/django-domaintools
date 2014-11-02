from django.conf import settings
from django.core.mail import send_mail
from django.core.management.base import BaseCommand, CommandError

from domaintools.models import Domain


ALERT_SEND_DAYS = [14, 3, 1]


class Command(BaseCommand):
    help = 'Sends notifications by email when domains are going to expire.'

    def handle(self, *args, **options):
        for domain in Domain.objects.all():
            days_remaining = domain.days_remaining()
            if days_remaining < max(ALERT_SEND_DAYS):
                print 'Domain {} expires in {} days'.format(domain.id, domain.days_remaining())
                if days_remaining in ALERT_SEND_DAYS:
                    send_mail('Domain Expiring: {}'.format(domain.id),
                        'The domain {} is going to expire on {} ({} days)'.format(domain.id, domain.expiry_date, days_remaining),
                        'webmaster@epixstudios.co.uk',
                        [admin[1] for admin in settings.ADMINS])
