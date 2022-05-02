from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=50)
    
    def __str__(self):
        return self.title


class Ad(models.Model):
    title = models.CharField(max_length=50)
    describe = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=11, decimal_places=2)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    def __str__(self):
        return self.title
