from django.db import models

# Create your models here.
class Movies_Table(models.Model):
    name = models.CharField(max_length=20)
    release_date = models.DateField()
    the_choices = (
        ('yes','YES'),
        ('no','NO')
    )
    in_theater = models.CharField(max_length=3, choices=the_choices, default='YES')
    rating = models.FloatField()
    lang_choices = (
        ('english','ENGLISH'),
        ('hindi','HINDI'),
        ('marathi','MARATHI')
    )
    language = models.CharField(max_length=7, choices=lang_choices, default='english')


    def __str__(self):
        msg = "Movie: "+ self.name +" inserted successfully!"
        return msg