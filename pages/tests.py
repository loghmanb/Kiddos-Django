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

from django.test import TestCase

from .models import BlogPost, PostComment


class KiddosTestCase(TestCase):
    def setUp(self):
        blog_post = BlogPost.objects.create(
            title="Test post",
            short_desc="Test short description",
            body="test body",
            tags="Tag1|Tag2")
        PostComment.objects.create(
            name='Test comment 1',
            blog_post=blog_post,
            email='test@test.com',
            message='Test message 1',
            is_published=True
        )
        PostComment.objects.create(
            name='Test comment 2',
            blog_post=blog_post,
            email='test@test.com',
            message='Test message 2',
        )

    def test__BlogPost__tag_list__property(self):
        blog_post = BlogPost.objects.get(title="Test post")
        self.assertEqual(blog_post.tag_list, ['Tag1', 'Tag2'])

    def test__BlogPost__published_comments__property(self):
        blog_post = BlogPost.objects.get(title="Test post")
        comments = PostComment.objects.filter(blog_post__id=blog_post.id,
                                              is_published=True)
        self.assertEqual(list(blog_post.published_comments), list(comments))
