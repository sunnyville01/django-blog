from django.contrib.auth import logout # Added now
from django.contrib import messages # Added now
from django.core.urlresolvers import reverse_lazy
from django.views import generic

from . import forms


class SignUpView(generic.CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy("login")
    template_name = "accounts/signup.html"

class LogoutView(generic.RedirectView):
    url = reverse_lazy('posts:list')
    def get(self, request, *args, **kwargs):
        logout(request)
        messages.add_message(self.request, messages.SUCCESS, 'You have been logged out.')
        return super().get(request, *args, **kwargs)

