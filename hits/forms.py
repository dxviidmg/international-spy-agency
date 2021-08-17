from django.forms import ModelForm, ModelChoiceField
from hits.models import Hit
from django.contrib.auth.models import User
from accounts.models import Profile


class HitUpdateFormHitman(ModelForm):
    class Meta:
        model = Hit
        fields = ['state']

class HitUpdateFormManager(ModelForm):

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        profile = kwargs.pop('profile')

        if profile.type_user == 'Manager':
            hitmen_profiles = Profile.objects.filter(boss=user, state="Active")
            hitmen_id = hitmen_profiles.values("user")
            hitmen = User.objects.filter(id__in=hitmen_id)
        elif profile.type_user == 'Boss':
            hitmen = User.objects.all().exclude(id=user.id)

        super(HitUpdateFormManager, self).__init__(*args, **kwargs)

        self.fields['hitman'] = ModelChoiceField(queryset=hitmen)

    class Meta:
        model = Hit
        fields = ['hitman']



class HitCreateForm(ModelForm):

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        profile = kwargs.pop('profile')

        if profile.type_user == 'Manager':
            hitmen_profiles = Profile.objects.filter(boss=user, state="Active")
            hitmen_id = hitmen_profiles.values("user")
            hitmen = User.objects.filter(id__in=hitmen_id).exclude(id=user.id)
        elif profile.type_user == 'Boss':
            hitmen = User.objects.all().exclude(id=user.id)

        super(HitCreateForm, self).__init__(*args, **kwargs)

        self.fields['hitman'] = ModelChoiceField(queryset=hitmen)

    class Meta:
        model = Hit
        fields = ['hitman', "description", "target_name", "state"]




