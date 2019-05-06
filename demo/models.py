from django.db import models

# Create your models here.
'''how to create model
open model.py
'''
class Movie(models.Model):
	actor=models.CharField(max_length=30)
	actor_movie=models.CharField(max_length=50)
	movie_type=models.CharField(max_length=20)
	movie_logo=models.CharField(max_length=100)
	def __str__(self):
		return self.actor + '----' + self.actor_movie
class Song(models.Model):
	movie=models.ForeignKey(Movie,on_delete=models.CASCADE)
	file_type=models.CharField(max_length=50)
	song_name=models.CharField(max_length=100)
	is_favourite=models.BooleanField(default=False)
	def __str__(self):
		return self.song_name
'''how to activate model
python manage.py makemigrations
python manage.py migrate
how to go django database api
python manage.py shell
from demo.models import Movie,Song
Movie.objects.all() show all records
how to insert records
a=Movie(actor="xyz",actor_movie="xyz",movie_logo="xyz",movie_type="xyz")
a.save()
Movie.object.all()
a=Movie(actor="xy",actor_movie="yz",movie_logo="xz",movie_type="xyz")
a.save()
Movie.object.all()
a.actor
a.id
a.pk
exit()
How to filtering database
save in models
def_str_(self):
	return self.actor + '----' + self.actor_movie


def_str_(self):
	return self.song_name
cmd
from demo.models import Movie,Song
movie.object.all()	

movie.object.filter(id=1)	

'''
	