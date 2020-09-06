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
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    website = forms.CharField(required=False)
    message = forms.CharField(required=False,
                              widget=forms.Textarea(
                                  attrs={'rows': 10, 'cols': 30}))


class SubscriptionForm(forms.Form):
    email = forms.EmailField()


class PostReplyForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    website = forms.URLField(required=False)
    message = forms.Textarea()
