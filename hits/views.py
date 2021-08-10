from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from hits.models import Hit
from accounts.models import Profile

class HitListView(ListView):
    model = Hit

    def get_queryset(self):
        profile = Profile.objects.get(user=self.request.user)
        type_user = profile.type_user
        if type_user == 'Boss':
            queryset = Hit.objects.all()
        elif type_user == 'Manager':
            print('manager')
    

        return queryset
