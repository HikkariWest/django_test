from django.db import models

# Create your models here.
class Post(modes.Model):
	CATEGORIES = [
	(0, 'Все'),
	(1, 'Игровые новости'),
	(2, 'Технологии'),
	(3, 'Софт'),
	(4, 'Новости киноиндустрии'),
	]
	title = models.CharField(max_length = 200)
	content = models.TextField(blank = True)
	category = models.SmallIntegerField(choices = CATEGORIES, default = 0)
	draft = models.BooleanField(default = True)

	class Meta:
		ordering = ('id', 'draft')

	def __str__(self):
		return self.title