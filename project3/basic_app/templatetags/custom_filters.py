from django import template

register = template.Library()
@register.filter(name="cutt")
def cut(value,arg):
    """
    This cuts out all the value of 'arg' from the string
    """
    return value.replace(arg,'')

# register.filter('cut',cut)
#### either register or the annotation -> passing a function itself to another function or class ####


# Seems one filter per file but not sure