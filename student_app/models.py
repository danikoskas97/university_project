from django.db import models

class Student(models.Model):
	prenom = models.CharField(max_length=20)
	nom = models.CharField(max_length=20)
	date_de_naissance = models.DateField()

	def __str__(self):
		return self.prenom


