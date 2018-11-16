from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models import CASCADE, PROTECT


class Invitation(models.Model):
    from_user = models.ForeignKey(User, related_name="invitations_sent", on_delete=PROTECT)
    to_user = models.ForeignKey(User, related_name="invitations_received", on_delete=PROTECT)
    message = models.CharField(max_length=300)
    timestamp = models.DateTimeField(auto_now_add=True)