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

from datetime import datetime
from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _


class Setting(models.Model):
    class Meta:
        db_table = 'kiddos_settings'

    name = models.CharField('Name', primary_key=True,
                            max_length=32, blank=False, null=False)
    value = models.CharField('Value', max_length=512, blank=True, null=True)

    def __str__(self):
        return '%s: %s' % (self.name, self.value)


class Course(models.Model):
    class Meta:
        db_table = 'kiddos_courses'

    name = models.CharField('Name', max_length=50, blank=False, null=False)
    class_time = models.CharField('Class Time', max_length=20, blank=False,
                                  null=False)
    short_desc = models.CharField('Short Description', max_length=256)
    active = models.BooleanField('Is Active?!', default=True)
    image = models.ImageField('Image', upload_to='images/%Y/%m/%d/')

    def __str__(self):
        return '%s [%s]' % (self.name, self.class_time)


class BlogPost(models.Model):
    class Meta:
        db_table = 'kiddos_blog_post'

    title = models.CharField('Title', max_length=128, blank=False, null=False)
    short_desc = models.CharField('Short Description', max_length=256)
    body = models.TextField('Body')
    image = models.ImageField('Image', upload_to='images/%Y/%m/%d/')
    create_date = models.DateTimeField(verbose_name=_('Creation Date'),
                                       default=datetime.now, blank=True)
    create_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='+',
        blank=True,
        null=True,
        verbose_name=_('Created by'),
    )

    def __str__(self):
        return '%s [writter by %s]' % (self.title, self.create_user)
