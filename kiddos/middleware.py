# -*- coding: utf-8 -*-
##############################################################################
#
#    Chelsu,
#    Copyright (C) 2019-2021 Chelsu (<https://github.com/loghmanb/Chelsu>).
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

import threading

from django.contrib.auth.middleware import get_user
from django.utils.deprecation import MiddlewareMixin
from django.utils.functional import SimpleLazyObject
from django.conf import settings
from django.utils import translation


def get_db_from_subdomain(request) -> str:
    host_name = request.get_host()
    subdomain, *rest = host_name.split(".")
    if len(rest) > 1 and not subdomain.isdigit():
        return subdomain
        

def get_db(request):
    if not hasattr(request, "_cached_db"):
        db = get_db_from_subdomain(request)
        if db:
            request._cached_db = db
        elif not hasattr(request, "auth") or request.auth is None:
            return None
        else:
            request._cached_db = hasattr(request.auth, "db") and request.auth.db
    return request._cached_db


class EnviormentMiddleware(MiddlewareMixin):
    def process_request(self, request):
        curr_thread = threading.current_thread()
        curr_thread.env = dict(
            user=SimpleLazyObject(lambda: get_user(request)),
            db=SimpleLazyObject(lambda: get_db(request)),
        )
        request.db = get_db(request)

    def process_response(self, request, response):
        curr_thread = threading.current_thread()
        if hasattr(curr_thread, "env"):
            del curr_thread.env
        return response
