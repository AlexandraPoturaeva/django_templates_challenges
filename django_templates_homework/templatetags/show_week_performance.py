from django import template

register = template.Library()


@register.inclusion_tag('level_2/show_week_performance.html')
def show_week_performance(performance):
    weeks = [performance[f'week{num}_completed'] for num in range(1, 4)]
    return {'weeks': weeks}
