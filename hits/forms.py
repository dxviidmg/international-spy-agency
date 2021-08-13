from django.forms import ModelForm
from hits.models import Hit
from django.contrib.auth.models import User


class HitUpdateFormHitman(ModelForm):
    class Meta:
        model = Hit
        fields = ['state']

class HitUpdateFormManager(ModelForm):
    class Meta:
        model = Hit
        fields = ['hitman']


