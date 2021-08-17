from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.models import User
from accounts.models import Profile
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import views as auth_views
from django.views import generic
from django.urls import reverse_lazy

from .forms import LoginForm, RegisterForm
from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator


class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'accounts/login.html'


class RegisterView(generic.CreateView):
    model = User
    form_class = RegisterForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('accounts:login')

    
class HitmenListView(ListView):
    model = User

    def get_queryset(self):
        profile = Profile.objects.get(user=self.request.user)
        type_user = profile.type_user
        if type_user == 'Boss':
            queryset = User.objects.all()

        elif type_user == 'Manager':
            hitmen_profiles = Profile.objects.filter(boss=self.request.user)
            users = hitmen_profiles.values("user")

        elif type_user == 'Hitman':
            raise PermissionDenied

        return queryset


class HitmanUpdateView(UpdateView):
    model = Profile
    fields = ['state', 'boss']

    @method_decorator(permission_required('Hit.can_change_profile',raise_exception=True))
    def dispatch(self, request, pk):
        return super(HitmanUpdateView, self).dispatch(request)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['hitman_user'] = self.object.user
        return context