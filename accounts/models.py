from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


class Profile(models.Model):
    state_choices =(
        ("Active","Active"),
        ("Retired", "Retired"),
        ("Dead", "Dead")
    )

    type_user_choices =(
        ("Boss","Boss"),
        ("Manager", "Manager"),
        ("Hitman", "Hitman")
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user')
    state = models.CharField(max_length=10, choices=state_choices, default="Active")
    type_user = models.CharField(max_length=10, choices=type_user_choices, default="Hitman")
    boss = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE, related_name='boss')

    def __str__(self):
        return self.user.username + ' ' + self.type_user


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
#    instance.save()