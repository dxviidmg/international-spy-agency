from django.db import models

class Hit(models.Model):
    state_choices =(
        ("NotAssigned","NotAssigned"),
        ("Assigned","Assigned"),
        ("Failed", "Failed"),
        ("Completed", "Completed")
    )

    hitman = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    description = models.CharField(max_length=100)
    target_name = models.CharField(max_length=100)
    state = models.CharField(max_length=15, choices=state_choices, default="NotAssigned")
    assigned_by = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)