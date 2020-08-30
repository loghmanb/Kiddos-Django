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

from django.shortcuts import render as _render

from . import models
from . import services


def render(request, template, data=None):
    if data is None:
        data = {}
    data.update(services.get_website_settings())
    return _render(request, template, data)


def index(request):
    return render(request, 'pages/index.html')


def about(request):
    return render(request, 'pages/about.html')


def blog(request):
    return render(request, 'pages/blog.html')


def blog_single(request, id):
    return render(request, 'pages/blog_single.html')


def contact(request):
    return render(request, 'pages/contact.html')


def courses(request):
    courses = models.Course.objects.all()
    return render(request, 'pages/courses.html', {'courses': courses})


def pricing(request):
    return render(request, 'pages/pricing.html')


def teacher(request):
    teachers = models.Teacher.objects.filter(is_published=True)
    return render(request, 'pages/teacher.html', {'teachers': teachers})
