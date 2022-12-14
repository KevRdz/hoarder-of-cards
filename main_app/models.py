from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Card(models.Model):
  name = models.CharField(max_length=100)
  nation = models.CharField(max_length=100)
  position = models.CharField(max_length=100)
  team = models.CharField(max_length=100)
  user = models.ForeignKey(User, on_delete= models.CASCADE)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
      return reverse("cards_detail", kwargs={"card_id": self.id})