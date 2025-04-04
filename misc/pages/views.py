from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

# Create your views here.

class LandingView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        return render(request, 'pages/landing.html')
