from django import template
register = template.Library()

@register.filter
def get_value(monte_carlo_list, index):
    return monte_carlo_list[int(index)]
