from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.models import User
from accounts.models import Profile
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class HitmenListView(ListView):
    model = User

    def get_queryset(self):
        profile = Profile.objects.get(user=self.request.user)
        type_user = profile.type_user
        if type_user == 'Boss':
            queryset = User.objects.all()

            print(queryset)

        elif type_user == 'Manager':
            hitmen_profiles = Profile.objects.filter(boss=self.request.user)
            users = hitmen_profiles.values("user")

        elif type_user == 'Hitman':
            print('error')

        return queryset


class HitmanUpdateView(UpdateView):
    model = Profile
    fields = ['state', 'boss']
#    template_name = 'hits/hit_form.html'

#    def get_form_class(self):
#        profile = Profile.objects.get(user=self.request.user)#

#        if profile.type_user == 'Hitman':
#            return HitUpdateFormHitman
#        else:
#            return HitUpdateFormManager