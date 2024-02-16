from django.db import models
from django.contrib.auth.models import User

UNITS = [
    ("kg","kilogramů"),
    ("g","gramů"),
    ("dkg","dekagramů"),
    ("cup","cup"),
    ("cups","cups"),
    ("ml","mililitrů"),
    ("l","litrů"),
    ("polévková lžíce","polévková lžíce"),
    ("polévkových lžic","polévkových lžic"),
    ("kávová lžička","kávová lžička"),
    ("kávových lžiček","kávových lžiček"),
    ("kusy","kusy"),
    ("kus","kus"),
    ("kusů","kusů"),
    ("špetka","špetka"),
    ("hrst", "hrst"),
    ("hrsti","hrsti")
] 

class Recept(models.Model):
    name = models.CharField(max_length=200)
    slug =models.SlugField()
    image_url = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True)
    ingredients = models.ManyToManyField('Ingredients', blank=True, null=True)
    autor = models.ForeignKey('Autor', blank=True, null=True, on_delete=models.SET_NULL)
    day_time = models.ManyToManyField('DayTime', blank=True, null=True)
    avg_rating = models.FloatField(blank=True, null=True)
    quatntity = models.CharField(max_length=200, choices=UNITS, default="")
    calories = models.IntegerField(max_length=200)


    def __str__(self):
        return f"{self.name} ({self.autor})"

    def day_time_display(self):
        return ", ".join([i.name for i in self.day_time.all()])
    
    def ingredients_display(self):
         out = ""
         for i in self.ingredients.all():
            out += f"{i.quantity}{i.name}\n "
         return out


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

class Ingredients(models.Model):
    ingredient = models.CharField(max_length=200)
    

    def __str__(self):
        return f"{self.quatntity} {self.ingredient}"
    
class Comment(models.Model):
    recipe = models.ForeignKey(Recept, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE )
    text = models.TextField(blank=True)
    rating = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Coach(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    info = models.TextField(blank=True)

