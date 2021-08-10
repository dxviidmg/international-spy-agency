from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from hits.models import Hit
from accounts.models import Profile
from django.db.models import Q


class HitListView(ListView):
    model = Hit

    def get_queryset(self):
        profile = Profile.objects.get(user=self.request.user)
        type_user = profile.type_user
        if type_user == 'Boss':
            queryset = Hit.objects.all()

        elif type_user == 'Manager':
            hitmen_profiles = Profile.objects.filter(boss=self.request.user)
            hitmen_ids = hitmen_profiles.values_list("user", flat=True)
            queryset = Hit.objects.filter(Q(hitman__id__in=hitmen_ids) | Q(hitman=self.request.user))

        elif type_user == 'Hitman':
            queryset = Hit.objects.filter(hitman=self.request.user)

        return queryset
