from django.http import HttpResponse, Http404
from django.shortcuts import redirect


def can_modify_lesson(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.permissions == 'uploader' or request.user.is_superuser:
            return view_func(request, *args, **kwargs)
        else:
            raise Http404("Page not found")
    return wrapper_func


def superuser_required(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_superuser:
            return view_func(request, *args, **kwargs)
        else:
            raise Http404("Page not found")
    return wrapper_func