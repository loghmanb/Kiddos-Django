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

from django.shortcuts import get_object_or_404, render as _render
from django.core.paginator import Paginator

from . import models
from . import services
from .consts import SETTINGS_ABOUT_ARTICLE

NO_PER_PAGE = 6


def render(request, template, data=None):
    if data is None:
        data = {}
    data.update(services.get_website_settings())
    return _render(request, template, data)


def index(request):
    data = services.get_website_settings()
    fast_links = models.Page.objects.filter(publish_on_index=True,
                                            is_published=True)
    endorsements = models.Endorsement.objects.filter(is_published=True)
    recent_blog_posts = models.BlogPost.objects.filter(
        is_published=True).order_by('-create_date')[:3]
    sample_courses = models.Course.objects.filter(active=True)[:4]
    teachers = models.Teacher.objects.filter(publish_on_index=True)
    pricing_plans = models.PricingPlan.objects.all()
    gallery = models.Gallery.objects.filter(is_published=True
                                            ).order_by('-create_date')
    if data[SETTINGS_ABOUT_ARTICLE]:
        data['article'] = models.Page.objects.get(
            pk=data[SETTINGS_ABOUT_ARTICLE])
    data.update({
        'fast_links': fast_links,
        'endorsements': endorsements,
        'recent_blog_posts': recent_blog_posts,
        'sample_courses': sample_courses,
        'teachers': teachers,
        'pricing_plans': pricing_plans,
        'gallery': gallery,
    })
    return _render(request, 'pages/index.html', data)


def about(request):
    data = services.get_website_settings()
    if data[SETTINGS_ABOUT_ARTICLE]:
        data['article'] = models.Page.objects.get(
            pk=data[SETTINGS_ABOUT_ARTICLE])
    return _render(request, 'pages/about.html', data)


def blog(request):
    blog_posts = models.BlogPost.objects.filter(
        is_published=True).order_by('-create_date')
    paginator = Paginator(blog_posts, NO_PER_PAGE)
    page = int(request.GET.get('page', 1))
    pages = range(max(1, page-2), min(page+2, paginator.num_pages)+1)
    return render(request, 'pages/blog.html',
                  {'blog_posts': paginator.get_page(page),
                   'count': paginator.count,
                   'page_no': page,
                   'pages': pages,
                   'num_pages': paginator.num_pages, })


def blog_single(request, id):
    blog_post = get_object_or_404(models.BlogPost, pk=id)
    return render(request, 'pages/blog-single.html', {'blog_post': blog_post})


def contact(request):
    return render(request, 'pages/contact.html')


def courses(request):
    courses = models.Course.objects.filter(active=True)
    return render(request, 'pages/courses.html', {'courses': courses})


def pricing(request):
    pricing_plans = models.PricingPlan.objects.all()
    return render(request, 'pages/pricing.html',
                  {'pricing_plans': pricing_plans})


def teacher(request):
    teachers = models.Teacher.objects.filter(is_published=True)
    return render(request, 'pages/teacher.html', {'teachers': teachers})


def page(request, id):
    page = get_object_or_404(models.Page, pk=id)
    return render(request, 'pages/page.html', {'page': page})


def page_not_found_404_error(request, exception=None,
                             template='pages/404.html'):
    return render(request, template)
