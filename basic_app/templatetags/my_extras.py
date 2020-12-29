from django import template

# making customer tags first needs to register it

register = template.Library()

@register.filter(name='cut')
def cut(value,arg):
    """ This cuts out all values of arg from the string """
    return value.replace(arg,'')

# now needs to register again

# below is 1st way to register it, however best way to register is decorator as above fuction
# register.filter('cut',cut)