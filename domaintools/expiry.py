import subprocess
from datetime import date, datetime, timedelta


def get_command_output(arg_list):
    return subprocess.Popen(arg_list, stdout=subprocess.PIPE).communicate()[0]


def get_value(data, search):
    start_point = data.find(search)
    end_point = data.find('\n', start_point)
    data = data[start_point+len(search):end_point].strip()
    if ' ' in data: # May have a time stamp which we will remove
        data = data[:data.find(' ')]
    return data
    
    
def get_date_from_string(string):
    return datetime.strptime(string, '%d-%b-%Y')
    
    
def get_days_remaining(datetime_object):
    if type(datetime_object) == date:
        datetime_object = datetime(datetime_object.year, datetime_object.month, datetime_object.day)
    return (datetime_object - datetime.now()).days
    

RENEWAL_STRINGS = ['Renewal date:','Expiration Date:','Expiry date:']    
def domain_renewal_date(domain):
    data = get_command_output(['whois', domain])
    for renewal_string in RENEWAL_STRINGS:
        if renewal_string in data:
            date_string = get_value(data, renewal_string)
            datetime_object = get_date_from_string(date_string)
            return datetime_object
    return None
    
    
def domain_days_remaining(domain):
    datetime_object = domain_renewal_date(domain)
    days_remaining = get_days_remaining(datetime_object)
    return days_remaining

