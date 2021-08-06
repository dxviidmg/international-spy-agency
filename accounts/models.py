from django.db import models
from django.contrib.auth.models import User


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

    state = models.CharField(max_length=10, choices=state_choices, default="Active")
    type_user = models.CharField(max_length=10, choices=type_user_choices, default="Hitman")
    boss = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)

