from django.db import models

class Cart(models.Model):
    title = models.CharField(max_length=50)
    desc = models.TextField()
    icon = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class About(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField()
    video = models.FileField(upload_to='about/video')

class Article(models.Model):
    title = models.CharField(max_length=50)
    desc = models.TextField()
    icon = models.CharField(max_length=50)


