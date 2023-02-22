from django.shortcuts import redirect


def logged_staff_only (view_func):
    def wrapper_function(request, *args, **kwargs):
        user = request.user
        if user.is_anonymous:
            return redirect('/auth/login')
        elif user.is_authenticated and user.is_staff:
            return view_func(request, *args, **kwargs)
        else:
            return redirect('/customer/')
    return wrapper_function
