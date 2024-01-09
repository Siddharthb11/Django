from django.contrib import admin
from movies import models

# Register your models here.
class MoviesAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "release_date", "in_theater", "rating", "language"]

admin.site.register(models.Movies_Table, MoviesAdmin)