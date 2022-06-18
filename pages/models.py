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

from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _

from .utils import *


class Website(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.name

class ElementTemplate(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False, unique=True)
    structure = models.TextField(blank=False, null=False)
    website = models.ForeignKey('Website', on_delete=models.CASCADE, null=True, blank=True)

class Setting(models.Model):
    class Meta:
        db_table = 'kiddos_settings'

    name = models.CharField('Name', primary_key=True,
                            max_length=50, blank=False, null=False)
    value = models.TextField('Value', blank=True, null=True)

    def __str__(self):
        return '%s = "%s"' % (self.name, self.value)


class Course(models.Model):
    class Meta:
        db_table = 'kiddos_courses'

    name = models.CharField('Name', max_length=50, blank=False, null=False)
    class_time = models.CharField('Class Time', max_length=20, blank=False,
                                  null=False)
    short_desc = models.CharField('Short Description', max_length=256)
    active = models.BooleanField('Is Active?!', default=True)
    image = models.ImageField('Image', upload_to='images/%Y/%m/%d/',
                              validators=[validate_image_size])

    def __str__(self):
        return '%s [%s]' % (self.name, self.class_time)


class BlogPost(models.Model):
    """
    Stores a single blog post related to :model:`pages.Teacher`.
    """
    class Meta:
        db_table = 'kiddos_blog_post'
        indexes = [
            models.Index(name='search_on_blog_pots',
                         fields=['is_published', 'title', 'short_desc']),
        ]
        ordering = ('-create_date',)

    title = models.CharField('Title', max_length=128, blank=False, null=False,
                             help_text='Enter title of blog post')
    short_desc = models.CharField('Short Description', max_length=256)
    body = models.TextField(
        'Body', help_text='HTML tags can be used to decorating the text')
    tags = models.CharField(_('Tags'), max_length=128,
                            blank=True, null=False, default='')
    image = models.ImageField('Image', upload_to='images/%Y/%m/%d/',
                              validators=[validate_image_size])
    is_published = models.BooleanField(_('Is published!'), default=True)
    author = models.ForeignKey('pages.Teacher', on_delete=models.DO_NOTHING,
                               related_name='+', null=True,
                               verbose_name=_('Author'))
    create_date = models.DateTimeField(verbose_name=_('Creation Date'),
                                       auto_now_add=True, blank=True)
    create_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='+',
        blank=True,
        null=True,
        verbose_name=_('Created by'),
    )

    @property
    def tag_list(self):
        return self.tags and self.tags.split('|') or []

    @property
    def published_comments(self):
        return PostComment.objects.filter(blog_post__id=self.id,
                                          is_published=True)

    def __str__(self):
        return '%s [written by %s]' % (self.title, self.create_user)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('blog-single', args=[str(self.id)])


class PostComment(models.Model):
    """
    Stores a single comment of blog post, related to :model:`pages.BlogPost`
    """
    class Meta:
        db_table = 'kiddos_post_comment'

    name = models.CharField(_('Name'), max_length=100, blank=False, null=False)
    blog_post = models.ForeignKey(BlogPost, related_name='comments',
                                  on_delete=models.CASCADE, null=False,
                                  verbose_name=_('Blog Post'),)
    email = models.EmailField(_("Email"), max_length=100, null=False,
                              blank=False)
    website = models.CharField(_('Website'), max_length=100, blank=True,
                               null=True)
    message = models.TextField(_('Message'), null=False)
    create_date = models.DateTimeField(_('Create Date'), auto_now_add=True,
                                       null=False)
    is_published = models.BooleanField(_('Is published!'), default=False,
                                       null=False)


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
                              null=True, blank=True,
                              validators=[validate_image_size])
    twitter = models.CharField(_('Twitter Account'), max_length=30,
                               blank=True, null=True)
    facebook = models.CharField(_('Facebook Account'), max_length=30,
                                blank=True, null=True)
    googleplus = models.CharField(_('Google+ Account'), max_length=30,
                                  blank=True, null=True)
    instagram = models.CharField(_('Instagram Account'), max_length=30,
                                 blank=True, null=True)
    is_published = models.BooleanField(_('Is published!'), default=True,
                                       null=False)
    publish_on_index = models.BooleanField(_('Is published on index page?!'),
                                           default=True, null=False)

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
    image = models.ImageField(verbose_name=_('Image'), upload_to='images/%Y/%m/%d/',
                              null=False, validators=[validate_image_size])
    plan_cls = models.CharField(_('Plan Style Class'), max_length=20,
                                blank=True, null=True)

    def __str__(self):
        return self.name


class Endorsement(models.Model):
    class Meta:
        db_table = 'kiddos_endorsement'

    person = models.CharField(_('Person'), max_length=50,
                              blank=False, null=False)
    role = models.CharField(_('Role'), max_length=20, blank=False, null=False)
    note = models.TextField(_('Note'), blank=False, null=False)
    is_published = models.BooleanField(_('Is published'),
                                       default=True, null=False)
    photo = models.ImageField(_('Photo'), upload_to='photos/%Y/%m/%d',
                              null=True, validators=[validate_image_size])


class Gallery(models.Model):
    class Meta:
        db_table = 'kiddos_gallery'

    name = models.CharField(_('Name'), max_length=50, blank=False, null=False)
    photo = models.ImageField(_('Photo'), upload_to='photo/gallery/',
                              null=False, validators=[validate_image_size])
    is_published = models.BooleanField(_('Is Published!'),
                                       default=True, null=False)
    create_date = models.DateTimeField(_('Create Date'), auto_now_add=True,
                                       null=False)


class Page(models.Model):
    class Meta:
        db_table = 'kiddos_page'

    name = models.CharField(_('Name'), max_length=256, null=False, blank=False)
    short_desc = models.CharField(_('Short Description'), max_length=512,
                                  null=False, blank=False)
    body = models.TextField(_('Body'))
    publish_on_index = models.BooleanField(_('Publish on Index page'),
                                           default=False, null=False)
    is_published = models.BooleanField(_('Is Published'),
                                       default=False, null=False)
    image = models.ImageField(_('Image'), upload_to='images/%Y/%m/%d/',
                              validators=[validate_image_size])


class Subscription(models.Model):
    class Meta:
        db_table = 'kiddos_subscription'

    email = models.EmailField(_("Email"), unique=True,
                              null=False, max_length=100)


class ReuestForQuote(models.Model):
    class Meta:
        db_table = 'kiddos_rfq'

    first_name = models.CharField(_('First Name'), max_length=20, null=False)
    last_name = models.CharField(_('Last Name'), max_length=20, null=False)
    course = models.ForeignKey(Course, related_name='+', null=True,
                               verbose_name=_('Course'), on_delete=models.DO_NOTHING)
    email = models.EmailField(_("Email"), blank=True,
                              null=True, max_length=100)
    phone = models.CharField(_('Phone'), max_length=20,
                             null=False, blank=False)
    message = models.TextField(_('Message'), null=False)
    is_done = models.BooleanField(_('Is done?!'), default=False)
    create_date = models.DateTimeField(_('Create Date'), auto_now_add=True,)


class Message(models.Model):
    class Meta:
        db_table = 'message'

    full_name = models.CharField(_('Full Name'), max_length=50, null=False)
    email = models.EmailField(_("Email"), blank=True,
                              null=True, max_length=100)
    subject = models.CharField(_('Subject'), max_length=150, null=False)
    message = models.TextField(_('Message'), null=False)
    create_date = models.DateTimeField(_('Create Date'), auto_now_add=True,)


class CustomForm(models.Model):
    class Meta:
        db_table = 'kiddos_custom_form'

    name = models.CharField(_('Name'), max_length=50, null=False)
    structure = models.JSONField()

    def __str__(self) -> str:
        return self.name


class CustomFormData(models.Model):
    class Meta:
        db_table = 'kiddos_custom_form_data'

    custom_form = models.ForeignKey(CustomForm, on_delete=models.CASCADE)
    data = models.JSONField()
    list_order = models.IntegerField()
