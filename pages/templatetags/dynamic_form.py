from django import template

register = template.Library()


def id_for_label(form, field_name):
    return form.auto_id % field_name


register.filter('id_for_label', id_for_label)


def form_field(form, field):
    return form.fields[field].widget.render(field, form.data.get(field))


register.filter('form_field', form_field)


def field_label(form, field):
    return form.fields[field].label or field.capitalize()


register.filter('field_label', field_label)


def field_errors(form, field):
    return form.errors.get(field) or ''


register.filter('field_errors', field_errors)


@register.inclusion_tag('pages/link_to_custom_form_data.html', takes_context=True)
def link_to_custom_form_data(context, custom_form_data):
    return {
        'form_name': custom_form_data.custom_form.name,
        'record_id': custom_form_data.id,
        'edit_mode': 'edit' in context["request"].GET,
    }
