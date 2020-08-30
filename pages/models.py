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


class TeacherPosition(models.Model):
    class Meta:
        db_table = 'kiddos_teacher_position'

    name = models.CharField(_('Name'), max_length=50, blank=False, null=False)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    class Meta:
        db_table = 'kiddos_teacher'

    full_name = models.CharField(_('Full Name'), max_length=60)
    position = models.ForeignKey(TeacherPosition, on_delete=models.DO_NOTHING,
                                 related_name='+', verbose_name=_('Position'))
    short_desc = models.CharField(_('Short Description'), max_length=256)
    photo = models.ImageField(verbose_name=_('Photo'), upload_to='photos/%Y/%m/%d/',
                              null=True, blank=True)
    twitter = models.CharField(_('Twitter Account'), max_length=30,
                               blank=True, null=True)
    facebook = models.CharField(_('Facebook Account'), max_length=30,
                                blank=True, null=True)
    googleplus = models.CharField(_('Google+ Account'), max_length=30,
                                  blank=True, null=True)
    instagram = models.CharField(_('Instagram Account'), max_length=30,
                                 blank=True, null=True)
    is_published = models.BooleanField(_('Is published!'), default=True)

    def __str__(self):
        return self.full_name


class PricingPlan(models.Model):
    class Meta:
        db_table = 'kiddos_pricingplan'

    name = models.CharField(_('Name'), max_length=30, blank=False, null=False)
    price = models.FloatField(_('Price'), null=False)
    duration = models.IntegerField(_('Duration'), null=False)
    short_desc = models.CharField(_('Short Description'), max_length=256,
                                  blank=False, null=False)
    image = models.ImageField(verbose_name=_('Image'), upload_to='images/%Y/%m/%d',
                              null=False)
    plan_cls = models.CharField(_('Plan Style Class'), max_length=20,
                                blank=True, null=True)

    def __str__(self):
        return self.name
