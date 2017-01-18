from django.db import models

# Create your models here.

class text1(models.Model):
	text1 = models.CharField(max_length=1000000000, default=' ')

