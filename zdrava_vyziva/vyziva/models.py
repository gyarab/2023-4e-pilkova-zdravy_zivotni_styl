from django.db import models

class Recept(models.Model):
    name = models.CharField(max_length=200)
    slug =models.SlugField()
    image_url = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True)
    ingredients = models.TextField(blank=True)
    autor = models.ForeignKey('Autor', blank=True, null=True, on_delete=models.SET_NULL)
    day_time = models.ManyToManyField('DayTime', blank=True, null=True)
    avg_rating = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.year})"

    def genres_display(self):
        return ", ".join([i.name for i in self.genres.all()])


class Autor(models.Model):
    name = models.CharField(max_length=200, default="Daniela Pilková")
    slug = models.SlugField()
    age = models.IntegerField(max_length=200)
    photo_url = models.CharField(max_length=255, blank=True, null=True)
    author_info = models.TextField()

class DayTime(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name}"
    
class Comment(models.Model):
    recepe = models.ForeignKey(Recept, on_delete=models.CASCADE)
    author = models.CharField(max_length=255, blank=True)
    text = models.TextField(blank=True)
    rating = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Coach(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    info = models.TextField(blank=True)