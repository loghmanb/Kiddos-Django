# -*- coding: utf-8 -*-
##############################################################################
#
#    KiddosDjango,
#    Copyright (C) 2020 Loghman Barari (<https://github.com/loghmanb/KiddosDjango>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from django import forms
from django.views.generic.base import TemplateView
from django.utils.translation import gettext as _
from django.template.response import TemplateResponse

from . import consts, models, services


class BaseForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(BaseForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class RequestForQuoteForm(forms.Form):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone = forms.CharField(required=True)
    message = forms.Textarea()


class MessageForm(BaseForm):
    subject = forms.CharField(required=True)
    full_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(required=True,
                              widget=forms.Textarea(
                                  attrs={'rows': 7, 'cols': 30}))


class SubscriptionForm(forms.Form):
    email = forms.EmailField()


class PostReplyForm(forms.Form):
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    website = forms.URLField(required=False)
    message = forms.CharField(required=False,
                              widget=forms.Textarea(
                                  attrs={'rows': 10, 'cols': 30}))


def create_form_field(structure):
    field_type = structure.pop('type')
    if field_type == 'text':
        structure['widget'] = forms.Textarea()
    elif field_type == "bool":
        structure['required'] = False
    klass = {
        'char': forms.CharField,
        'choice': forms.ChoiceField,
        'bool': forms.BooleanField,
    }.get(field_type, forms.CharField)
    return klass(**structure)


class CustomFormData(forms.Form):
    def __init__(self, custom_form_id, *args, **kwargs):
        super(CustomFormData, self).__init__(*args, **kwargs)

        custom_form = models.CustomForm.objects.get(pk=custom_form_id)

        for field in custom_form.structure:
            self.fields[field] = create_form_field(
                custom_form.structure[field])


class AboutPage(TemplateView):
    template_name = 'pages/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(services.get_website_settings())
        context.update(article=models.Page.objects.get(
            pk=context[consts.SETTINGS_ABOUT_ARTICLE]))
        return context
