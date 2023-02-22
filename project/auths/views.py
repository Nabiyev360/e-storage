from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout

class LoginView(View):
    def get(self, request):
        return render(request, 'auths/auth-login.html')

    def post(self, request):
        login_form = AuthenticationForm(data=request.POST)
        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            if user.is_staff:
                return redirect('/')
            else:
                return redirect('/customer/')
        else:
            return render(request, 'auths/auth-login.html')

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/auth/login/')