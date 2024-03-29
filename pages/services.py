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

from typing import Any, Dict, List
from .consts import *
from . import models


def get_website_settings():
    data = {
        SETTINGS_PHONE_NO: '+ 123 456 789',
        SETTINGS_EMAIL: 'youremail@email.com',
        SETTINGS_ADDRESS: '1234 Fake Street st., My City, My State',
        SETTINGS_TWITTER: 'my_twitter_account',
        SETTINGS_INSTAGRAM: 'my_instagram_account',
        SETTINGS_FACEBOOK: 'my_facebook_account',
        SETTINGS_WEBSITE: 'yoursite.com',
        SETTINGS_BLOG_SECTION_TEXT: '',
        SETTINGS_ENDORSEMENT_SECTION_TEXT: '',
        SETTINGS_PRICING_SECTION_TEXT: '',
        SETTINGS_CERTIFIEF_TEACHER_COUNT: 0,
        SETTINGS_CERTIFIEF_TEACHER_TEXT: '',
        SETTINGS_CERTIFIEF_TEACHER_SECTION_TEXT: '',
        SETTINGS_SPECIAL_EDUCATION_TEXT: '',
        SETTINGS_BOOK_LIBRARY_TEXT: '',
        SETTING_CERTIFICATION_TEXT: '',
        SETTINGS_REQUEST_A_QUOTE_TEXT: '',
        SETTINGS_SUCCESSFUL_KIDS: 0,
        SETTINGS_AWARDS_WON: 0,
        SETTINGS_NO_OF_EXCPERIENCES: 0,
        SETTINGS_EXCPERIENCES_MESSAGE: '',
        SETTINGS_OUR_COURSES_TEXT: '',
        SETTINGS_TEACHING_YOUR_CHILD: '',
        SETTINGS_ABOUT_PAGE: '',
        SETTINGS_ABOUT_ARTICLE: False,
        SETTINGS_WEBSITE_TITLE: 'KiddosDjango School - Sample Djnago website',
        SETTINGS_WEBSITE_NAME: 'Kiddos School',
    }
    data.update({setting.name: setting.value
                 for setting in models.Setting.objects.all()})
    data['latest_blog_posts'] = models.BlogPost.objects.order_by(
        '-create_date')[:2]
    return data


def get_custom_form():
    result: Dict[str, List[Dict[str, Any]]] = {}
    custom_form_data = models.CustomFormData.objects.all().order_by("-list_order", "-id")
    for record in custom_form_data:
        form_name = record.custom_form.name.lower().replace(" ", "_")
        if form_name not in result:
            result[form_name] = []
        data = CustomFormRecordData(
            record.id, record.custom_form, record.data)
        result[form_name].append(data)
    return result


class CustomFormRecordData:
    def __init__(self, record_id: int, custom_form: models.CustomForm, data: Dict[str, Any]) -> None:
        data['id'] = record_id
        data['custom_form'] = custom_form
        self._data = data

    def __getattr__(self, name: str) -> Any:
        return self._data.get(name)
