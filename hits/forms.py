from django.forms import ModelForm, ChoiceField
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
        super(HitUpdateFormManager, self).__init__(*args, **kwargs)

        self.fields['hitman'] = ChoiceField(choices=tuple([(hitman.pk, hitman.last_name.capitalize()+" "+hitman.first_name.capitalize()) for hitman in hitmen]))

    class Meta:
        model = Hit
        fields = ['hitman']


