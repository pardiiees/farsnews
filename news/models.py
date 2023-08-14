from django.db import models

# Create your models here.
class newscls(models.Model):
    onvan=models.CharField(max_length=100)
    matn=models.TextField()
    nevisande=models.CharField(max_length=40)
