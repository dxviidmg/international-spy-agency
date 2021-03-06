from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Hit(models.Model):
    state_choices =(
        ("NotAssigned","NotAssigned"),
        ("Assigned","Assigned"),
        ("Failed", "Failed"),
        ("Completed", "Completed")
    )

    hitman = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE, related_name='hitman')
    description = models.CharField(max_length=100)
    target_name = models.CharField(max_length=100)
    state = models.CharField(max_length=15, choices=state_choices, default="NotAssigned")
    assigned_by = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE, related_name='assigned_by')


    def get_absolute_url(self):
        return reverse('hits:hit-update', kwargs={'pk' : self.pk})
