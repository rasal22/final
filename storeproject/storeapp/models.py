from django.db import models



# Create your models here.
class features(models.Model):
    name=models.CharField(max_length=250)
    desptn=models.TextField()

    def __str__(self):
        return self.name

class courses(models.Model):
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='pics')
    desptn = models.TextField()

    def __str__(self):
        return self.name

class trainers(models.Model):
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='pics')
    desptn = models.TextField()

    def __str__(self):
        return self.name

class products(models.Model):
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='pics')
    desptn = models.TextField()

    def __str__(self):
        return self.name

