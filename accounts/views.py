from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.shortcuts import redirect
from django.views import View

from .forms import StyledAuthenticationForm


class CustomLoginView(LoginView):
    """Renders the login page and logs the user in on valid credentials."""
    template_name = 'accounts/login.html'
    authentication_form = StyledAuthenticationForm
    redirect_authenticated_user = True

    def form_valid(self, form):
        messages.success(self.request, f'Welcome back, {form.get_user().username}!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Invalid username or password. Please try again.')
        return super().form_invalid(form)


class CustomLogoutView(View):
    """Logs the user out and redirects to the login page with a message."""

    def get(self, request):
        logout(request)
        messages.info(request, 'You have been logged out successfully.')
        return redirect('accounts:login')
