from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models import CASCADE, PROTECT


class Invitation(models.Model):
    from_user = models.ForeignKey(User, related_name="invitations_sent", on_delete=models.CASCADE)
    to_user = models.ForeignKey(
        User,
        related_name="invitations_received",
        on_delete=models.CASCADE,
        verbose_name="User to invite",
        help_text="Please select the user to invite."
    )
    message = models.CharField(
        max_length=300,
        verbose_name="Optional message",
        help_text="It's always nice to add a friendly message"
    )
    timestamp = models.DateTimeField(auto_now_add=True)