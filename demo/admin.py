from django.contrib import admin
from .models import Movie,Song
# Register your models here.
'''
how to access models movie,song taBLE in admin panels
.models for relative modules which we made inside of same folder
'''
admin.site.register(Movie)
admin.site.register(Song)