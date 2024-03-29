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

from typing import Any
from django.shortcuts import get_object_or_404, redirect, render as _render
from django.views.decorators.http import require_safe
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.db.models import Q
from django.template.response import TemplateResponse

from . import consts, models, services, forms

NO_PER_PAGE = 6

MAIL_SENDER = ''


def render(request, template, data=None):
    if data is None:
        data = {}
    data.update(services.get_website_settings())
    return _render(request, template, data)


def index(request):
    """
    Display home page.

    **Context**

    ``sample_courses``
        An instance of :model:`pages.Course`.

    **Template:**

    :template:`pages/index.html`
    """
    data = {"edit_mode": 'edit' in request.GET}
    data.update(services.get_website_settings())
    # fast_links = models.Page.objects.filter(publish_on_index=True,
    #                                        is_published=True)
    endorsements = models.Endorsement.objects.filter(is_published=True)
    recent_blog_posts = models.BlogPost.objects.filter(
        is_published=True).defer('body')[:3]
    sample_courses = models.Course.objects.filter(active=True)[:4]
    courses = models.Course.objects.filter(active=True)
    teachers = models.Teacher.objects.filter(publish_on_index=True)
    pricing_plans = models.PricingPlan.objects.all()
    gallery = models.Gallery.objects.filter(is_published=True)
    if data[consts.SETTINGS_ABOUT_ARTICLE]:
        data['article'] = models.Page.objects.get(
            pk=data[consts.SETTINGS_ABOUT_ARTICLE])
    data.update({
        # 'fast_links': fast_links,
        'endorsements': endorsements,
        'recent_blog_posts': recent_blog_posts,
        'sample_courses': sample_courses,
        'courses': courses,
        'teachers': teachers,
        'pricing_plans': pricing_plans,
        'gallery': gallery,
    })
    data.update(services.get_custom_form())
    return _render(request, 'pages/index.html', data)


def blog(request):
    blog_posts = models.BlogPost.objects.filter(
        is_published=True).defer('body')
    search = request.POST and request.POST.get('search')
    if search:
        '''
        blog_posts = blog_posts.filter(
            Q(title__icontains=search)
            | Q(short_desc__icontains=search)
            | Q(body__icontains=search)
        )
        '''
        from .documents import BlogPostDocument
        from elasticsearch_dsl import Q as _Q
        blog_posts = BlogPostDocument.search().query(
            _Q('multi_match', query=search,
               fields=['title', 'short_desc', 'body', 'tags'])
        ).to_queryset()
    else:
        search = ''
    paginator = Paginator(blog_posts, NO_PER_PAGE)
    page = int(request.GET.get('page', 1))
    pages = range(max(1, page-2), min(page+2, paginator.num_pages)+1)
    return render(request, 'pages/blog.html', {
        'search': search,
        'blog_posts': paginator.get_page(page),
        'count': paginator.count,
        'page_no': page,
        'pages': pages,
        'num_pages': paginator.num_pages, })


def blog_single(request, id):
    blog_post = get_object_or_404(models.BlogPost, pk=id)
    data = {'blog_post': blog_post}
    form = forms.PostReplyForm(request.POST or None)
    if request.POST:
        if form.is_valid():
            comment = models.PostComment(
                **dict(form.cleaned_data, blog_post=blog_post)
            )
            comment.save()
            data['comment'] = 'recieved'
    data['form'] = form
    return render(request, 'pages/blog-single.html', data)


def contact(request):
    data = {}
    form = forms.MessageForm(request.POST or None)
    if request.POST:
        if form.is_valid():
            message = models.Message(
                **form.cleaned_data)
            message.save()
            data['status'] = 'recieved'
    data['form'] = form
    return render(request, 'pages/contact.html', data)


def courses(request, id=None):
    if id is None:
        courses = models.Course.objects.filter(active=True)
        return render(request, 'pages/courses.html', {'courses': courses})
    course = get_object_or_404(models.Course, pk=id)
    return render(request, 'pages/course.html', {'course': course})


def pricing(request):
    pricing_plans = models.PricingPlan.objects.all()
    return render(request, 'pages/pricing.html',
                  {'pricing_plans': pricing_plans})


def teacher(request, id=None):
    if id is None:
        teachers = models.Teacher.objects.filter(is_published=True)
        return render(request, 'pages/teachers.html', {'teachers': teachers})
    teacher = get_object_or_404(models.Teacher, pk=id)
    return render(request, 'pages/teacher.html', {'teacher': teacher})


def page(request, id):
    page = get_object_or_404(models.Page, pk=id)
    return render(request, 'pages/page.html', {'page': page})


def subscribe_me(request):
    email = request.POST['email']
    data = {'email': email}
    if models.Subscription.objects.filter(email=email).exists():
        data['error'] = 'Email "%s" is already subscribed!' % (email,)
    else:
        if MAIL_SENDER:
            send_mail('Subscribtion to Kiddos-Django',
                      "Subscribe to Kiddos-Django",
                      MAIL_SENDER,
                      [email],
                      fail_silently=False,
                      html_message='''
<h2>Congratulation</h2>
<p>You successfully were Subscribed!</p>''')
        subscrition = models.Subscription(email=email)
        subscrition.save()
    return render(request, 'pages/subscribtion.html', data)


def request_a_quote(request):
    if not request.POST:
        return redirect(request, 'index')
    rfq = models.ReuestForQuote(
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
        course_id=None if request.POST['course'] == '-1' else request.POST['course'],
        phone=request.POST['phone'],
        message=request.POST['message'],
    )
    rfq.save()
    return render(request, 'pages/rfq.html', {
        'first_name': request.POST['first_name'],
        'last_name': request.POST['last_name'],
    })


def custom_form_data_list(request, form_name):
    custom_form = models.CustomForm.objects.get(name=form_name)
    columns = list(custom_form.structure.keys())
    rows = models.CustomFormData.objects.filter(custom_form_id=custom_form.id)
    return TemplateResponse(request, 'pages/custom-form-data-list.html', 
                            {
                                'columns': columns, 
                                'rows': rows
                            })


def custom_form_data(request, form_name, id):
    custom_form_data_record = get_object_or_404(models.CustomFormData, pk=id)
    data = {'custom_form_data': custom_form_data_record}
    data["custom_form"] = custom_form_data_record.custom_form
    form = forms.CustomFormData(
        custom_form_data_record.custom_form.id, request.POST or None)
    if request.POST:
        if form.is_valid():
            custom_form_data_record.data = form.cleaned_data
            custom_form_data_record.save()
    else:
        form.data = custom_form_data_record.data
    data['form'] = form
    return render(request, 'pages/custom-form-data.html', data)


def page_not_found_404_error(request, exception=None,
                             template='pages/404.html'):
    return render(request, template)
