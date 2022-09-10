from django import template

register=template.Library()
#define user defined filters
def first_three_upper(value):
    result=value[:3].upper()
    return result

def last_three_upper(value):
    result=value[-3:].upper()
    return result

@register.filter(name='uid')
def user_name(mail):
    i=mail.find('@')
    result=mail[:i]
    return result

@register.filter(name='domain')
def domain_name(mail):
    i=mail.find('@')
    result=mail[i+1:]
    return result

register.filter('f3upper',first_three_upper)
register.filter('l3upper',last_three_upper)
#register.filter('uid',user_name)
#register.filter('domain',domain_name)

#calculate total for given list
@register.filter(name='tot')
def total(mylist):
    result=sum(mylist)
    return result

@register.filter(name='pass')
def passed_subjects(mylist):
    count=0
    for i in mylist:
        if i>=35:
            count+=1
    return count

#custom filters with arguments
@register.filter(name='passed')
def passed_subjects(mylist, arg=35):
    count=0
    for i in mylist:
        if i>=arg:
            count+=1
    return count

@register.filter()
def failed(mylist, arg=35):
    count=0
    for i in mylist:
        if i<arg:
            count+=1
    return count
