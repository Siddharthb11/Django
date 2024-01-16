from django.db import models

# Create your models here.
class Products_Table(models.Model):
    name = models.CharField(max_length=30)
    price = models.FloatField()

    def __str__(self):
        msg = "Product "+self.name+" added successfully!" #nit baghun type kar
        return msg