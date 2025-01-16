from django.db import models


class Categoty(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name


class Post(models.Model):
    image = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250, null=True, blank=True)
    category = models.ForeignKey(
        Categoty, on_delete=models.CASCADE, null=True, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    rate = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)


    def __str__(self):
        return f"{self.title} - {self.description}"
