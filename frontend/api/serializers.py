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

from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import serializers

from pages.models import BlogPost


# BlogPost Serializer
class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ('id', 'title', 'short_desc', 'body')


class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(label='Username')
    password = serializers.CharField(label='Password')

    def validate(self, data):
        user = authenticate(**data)
        if user:
            if user.is_active:
                return user
            else:
                raise serializers.ValidationError('User is not active!')
            raise serializers.ValidationError(
                'User credential is not correct!')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email')
