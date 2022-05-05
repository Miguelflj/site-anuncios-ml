from django.contrib import admin

# Register your models here.
from ml_anuncios import models

admin.site.register(models.Category)
admin.site.register(models.Ad) 