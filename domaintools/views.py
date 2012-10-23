from django.http import HttpResponse
from django.utils import simplejson
from django.views.decorators.csrf import csrf_exempt

from models import DnsRecord


def dynamic_dns_read(request, domain):
    data = {}
    dns_record = DnsRecord.objects.get(id=domain)
    data['id'] = dns_record.id
    data['ip'] = dns_record.ip
    data['last_change'] = dns_record.last_change.isoformat()
    return HttpResponse(simplejson.dumps(data), mimetype="application/json")


@csrf_exempt
def dynamic_dns_update(request, domain):
    '''
    Updates a domain to use a new IP address. If the IP should be the machine
    that performs the update, just supply your secret key as a POST parameter
    like this:
      curl http://localhost:8000/domain/update/a.example.com/ --data "key=ZHXPu3RTfs3oAexrwBTi8DGN5lmiH3t1pc9iGG1NZsp75UeM84"
    Otherwise provide an 'ip' as another parameter:
      curl http://localhost:8000/domain/update/a.example.com/ --data "key=ZHXPu3RTfs3oAexrwBTi8DGN5lmiH3t1pc9iGG1NZsp75UeM84&ip=1.2.3.4"
    '''
    data = {}
    status = 400
    dns_record = None
    updated = False

    if 'key' not in request.POST:
        data['error'] = 'Bad request'
    else:
        try:
            dns_record = DnsRecord.objects.get(id=domain)
        except DnsRecord.DoesNotExist:
            pass  # We don't want to give away which domains are managed so we will return an auth failure
        if not dns_record or request.POST['key'] != dns_record.key:
            data['error'] = 'Authentication failure'
            status = 403
        else:
            if 'ip' in request.POST:
                ip = request.POST['ip']
            else:
                ip = request.META['REMOTE_ADDR']
            if ip != dns_record.ip:
                dns_record.ip = ip
                dns_record.save()
                updated = True
            data['id'] = dns_record.id
            data['ip'] = dns_record.ip
            data['last_change'] = dns_record.last_change.isoformat()
            data['updated'] = updated
            status = 200
    return HttpResponse(simplejson.dumps(data), mimetype="application/json", status=status)
