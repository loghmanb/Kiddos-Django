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
    }
    data.update({setting.name: setting.value
                 for setting in models.Setting.objects.all()})
    return data
