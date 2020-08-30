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


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'short_desc', 'tags', 'is_published',
                    'create_user', 'create_date',)
    list_display_links = ('id', 'title',)
    list_filter = ('create_user', 'is_published',)
    search_fields = ('id', 'title', 'short_desc', 'create_user__username',
                     'create_user__first_name__icontains',
                     'create_user__last_name__icontains')
    list_per_page = 25


class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'class_time', 'active')
    list_display_links = ('id', 'name',)
    list_filter = ('active',)
    list_editable = ('active',)
    search_fields = ('name',)
    list_per_page = 25


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'position', 'is_published')
    list_display_links = ('id', 'full_name')
    list_filter = ('position', 'is_published')
    list_editable = ('position', 'is_published',)
    search_fields = ('full_name',)
    list_per_page = 25


class PricingPlanAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'duration')
    list_display_links = ('id', 'name',)
    search_fields = ('name',)
    list_per_page = 25


admin.site.register(models.Setting)

admin.site.register(models.BlogPost, BlogPostAdmin)

admin.site.register(models.Course, CourseAdmin)

admin.site.register(models.TeacherPosition)

admin.site.register(models.Teacher, TeacherAdmin)

admin.site.register(models.PricingPlan, PricingPlanAdmin)
