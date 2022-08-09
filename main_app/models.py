from django.db import models

# Create your models here.
class Card(models.Model):
  name = models.CharField(max_length=100)
  nation = models.CharField(max_length=100)
  position = models.CharField(max_length=100)
  team = models.CharField(max_length=100)

  def __str__(self):
    return self.name