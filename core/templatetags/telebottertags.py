from django import template
register = template.Library()


@register.inclusion_tag('core/card.html')
def as_card(data):
    """ generates a bootstrap card from dictionary
    """
    return data
