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

from django.urls import path

from . import views, forms

urlpatterns = [
    path('', views.index, name='index'),
    path('about', forms.AboutPage.as_view(), name='about'),
    path('blog', views.blog, name='blog'),
    path('blog/<int:id>', views.blog_single, name='blog-single'),
    path('page/<int:id>', views.page, name='page'),
    path('contact', views.contact, name='contact'),
    path('courses', views.courses, name='courses'),
    path('courses/<int:id>', views.courses, name='course'),
    path('pricing', views.pricing, name='pricing'),
    path('teachers', views.teacher, name='teachers'),
    path('teachers/<int:id>', views.teacher, name='teacher'),
    path('request-a-quote', views.request_a_quote, name='request-for-quote'),
    path('subscribe-me', views.subscribe_me, name='subscribe-me'),
    path('custom-form-data/<form_name>',
         views.custom_form_data_list, name='custom-form-data-list'),
    path('custom-form-data/<form_name>/<int:id>',
         views.custom_form_data, name='custom-form-data')
]
