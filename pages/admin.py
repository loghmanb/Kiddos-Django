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

from django.contrib import admin

from . import models


class SettingAdmin(admin.ModelAdmin):
    list_display = ('name', 'value')
    list_display_links = ('name', 'value',)
    search_fields = ('name',)
    list_per_page = 25


admin.site.register(models.Setting, SettingAdmin)


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'short_desc', 'tags', 'is_published',
                    'create_user', 'create_date',)
    list_display_links = ('id', 'title',)
    list_filter = ('create_user', 'is_published',)
    search_fields = ('id', 'title', 'short_desc', 'create_user__username',
                     'create_user__first_name__icontains',
                     'create_user__last_name__icontains')
    list_per_page = 25


admin.site.register(models.BlogPost, BlogPostAdmin)


class PostCommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'website', 'is_published',
                    'blog_post', 'create_date')
    list_display_links = ('id', 'name', 'email', 'website',)
    list_editable = ('is_published',)
    list_filter = ('is_published',)
    search_fields = ('name', 'email', 'website',)
    list_per_page = 25


admin.site.register(models.PostComment, PostCommentAdmin)


class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'class_time', 'active')
    list_display_links = ('id', 'name',)
    list_filter = ('active',)
    list_editable = ('active',)
    search_fields = ('name',)
    list_per_page = 25


admin.site.register(models.Course, CourseAdmin)


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'position',
                    'is_published', 'publish_on_index', )
    list_display_links = ('id', 'full_name')
    list_filter = ('position', 'is_published', 'publish_on_index', )
    list_editable = ('position', 'is_published', 'publish_on_index', )
    search_fields = ('full_name',)
    list_per_page = 25


admin.site.register(models.TeacherPosition)
admin.site.register(models.Teacher, TeacherAdmin)


class PricingPlanAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'duration')
    list_display_links = ('id', 'name',)
    search_fields = ('name',)
    list_per_page = 25


admin.site.register(models.PricingPlan, PricingPlanAdmin)


class EndorsementAdmin(admin.ModelAdmin):
    list_display = ('id', 'person', 'is_published')
    list_display_links = ('id', 'person',)
    search_fields = ('person',)
    list_per_page = 25


admin.site.register(models.Endorsement, EndorsementAdmin)


class GalleryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'photo', 'is_published')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 25


admin.site.register(models.Gallery, GalleryAdmin)


class PageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'publish_on_index')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_filter = ('publish_on_index',)
    list_per_page = 25


admin.site.register(models.Page, PageAdmin)


class RequestForQuoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'phone',
                    'email', 'course', 'is_done', 'create_date')
    list_display_links = ('id', 'first_name', 'last_name', 'phone', 'email')
    search_fields = ('first_name', 'last_name', 'phone', 'email',)
    list_filter = ('is_done', 'course')
    list_per_page = 25


admin.site.register(models.ReuestForQuote, RequestForQuoteAdmin)


class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'subject', 'email', 'create_date')
    list_display_links = ('id', 'full_name', 'subject', 'email')
    search_fields = ('full_name', 'subject', 'email',)
    list_per_page = 25


admin.site.register(models.Message, MessageAdmin)


class CustomFormAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 25


admin.site.register(models.CustomForm, CustomFormAdmin)


class CustomFormDataAdmin(admin.ModelAdmin):
    list_display = ('id', 'custom_form', 'list_order')
    list_display_links = ('id', 'custom_form')
    search_fields = ('custom_form',)
    list_per_page = 25


admin.site.register(models.CustomFormData, CustomFormDataAdmin)



class ElementTemplateAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'website')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 25


admin.site.register(models.ElementTemplate, ElementTemplateAdmin)


class WebsiteAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

admin.site.register(models.Website, WebsiteAdmin)