from django.contrib import admin

from .models import Recept, Autor, DayTime, Coach, Comment, Ingredients


admin.site.register(Recept)
admin.site.register(Autor)
admin.site.register(DayTime)
admin.site.register(Coach)
admin.site.register(Comment)
admin.site.register(Ingredients)
