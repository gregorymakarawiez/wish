from django import template

register = template.Library()


@register.filter
def index(List, i):
    if isinstance(i,str):
        i=int(i)

    return List[i]




@register.filter
def sort(value):
    if isinstance(value, dict):
        sorted_keys = sorted(value.keys())
        sorted_list=[]
        for key  in sorted_keys:
            sorted_list.append(value[key])
        return sorted_list
    elif isinstance(value, list):
        return sorted(value)
    else:
        return value


@register.filter
def sort_dict(value):

    def generator():
        sorted_keys = sorted(value.keys())
        for key  in sorted_keys:
            yield key, value[key]

    return generator
