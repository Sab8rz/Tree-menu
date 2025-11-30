from django import template
from ..models import MenuPoint


register = template.Library()


@register.inclusion_tag('tree_menu/menu.html', takes_context=True)
def draw_menu(context, menu_name):
    points = list(MenuPoint.objects.filter(menu_name=menu_name).select_related('parent').order_by('id'))
    if not points:
        return {'points': [], 'menu_name': menu_name, 'curr_url': context['request'].path}

    tree = {p.id: {'point': p, 'url': p.get_absolute_url(), 'children': []} for p in points}
    root_points = []

    for p in points:
        if (parent_id := p.parent_id) in tree:
            tree[parent_id]['children'].append(p.id)
        else:
            root_points.append(p.id)

    def has_active_descendant(node_id, curr_url):
        node = tree[node_id]
        if node['url'] == curr_url:
            return True
        return any(has_active_descendant(child_id, curr_url) for child_id in node['children'])

    def build_node(node_id, curr_url):
        node = tree[node_id]
        is_active = node['url'] == curr_url
        is_expanded = is_active or has_active_descendant(node_id, curr_url)

        return {
            'point': node['point'],
            'url': node['url'],
            'is_active': is_active,
            'children': [build_node(child_id, curr_url) for child_id in node['children']] if is_expanded else []
        }

    res = [build_node(root_id, context['request'].path) for root_id in root_points]
    return {'points': res, 'menu_name': menu_name, 'curr_url': context['request'].path}