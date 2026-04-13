from django.http import HttpResponseForbidden
from django.shortcuts import redirect
from .models import Profile


def admin_only(view_func):
    def wrapper(request, *args, **kwargs):

        profile, created = Profile.objects.get_or_create(
            user=request.user,
            defaults={'role': 'student'}
        )

        if profile.role != 'admin':
            return HttpResponseForbidden("Access Denied")

        return view_func(request, *args, **kwargs)

    return wrapper


def role_required(allowed_roles):
    def decorator(view_func):
        def wrapper(request, *args, **kwargs):

            profile, created = Profile.objects.get_or_create(
                user=request.user,
                defaults={'role': 'student'}
            )

            if profile.role in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return redirect('students:dashboard')

        return wrapper
    return decorator