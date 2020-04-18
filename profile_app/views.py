from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import UpdateView, CreateView, View
from profile_app.models import Customer, LoggerEditProfile
from django.urls import reverse_lazy
from profile_app.forms import SignUpForm


class SignUpView(CreateView):
    template_name = 'signup.html'
    queryset = Customer.objects.all()
    success_url = reverse_lazy('index')
    form_class = SignUpForm


class MyProfile(UpdateView):
    template_name = 'my_profile.html'
    queryset = Customer.objects.filter(is_active=True)
    fields = ('email', 'first_name', 'last_name')
    success_url = reverse_lazy('index')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(id=self.request.user.id)

    def get_user_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[-1].strip()
        else:
            ip = request.META.get('REMOTE_ADDR')

        return ip

    def post(self, request, *args, **kwargs):
        ip = self.get_user_ip(request)
        LoggerEditProfile.objects.create(user=request.user.id, ip=ip)

        return super().post(request, *args, **kwargs)
