import uuid               
from django.db import models

class Profile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=250, unique=True)

    gender = models.CharField(max_length=20)
    gender_probability = models.FloatField()
    gender_size = models.IntegerField()

    age = models.IntegerField()
    age_group = models.CharField(max_length=20)
    
    country = models.CharField(max_length=20)
    country_probability = models.FloatField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# Create your models here.
