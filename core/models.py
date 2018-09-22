from django.db import models

# Create your models here.
class interested(models.Model):
	TYPE_LIST = (
		('evaluation', 'Evaluation'),
		('psychiatrist', 'Psychiatrist'),
		)
	
	email_address 			=			models.EmailField(max_length=254, blank=False, null=False)

	interested_in			=			models.CharField(max_length=20, choices=TYPE_LIST, default=TYPE_LIST[0][0])

	timestamp				=			models.DateTimeField(auto_now=False, auto_now_add=True)
	updated					=			models.DateTimeField(auto_now=True, auto_now_add=False)

	def __str__(self):
		return(self.email_address)

	class Meta:
		ordering	 		=			["-timestamp", "-updated"]
		verbose_name 		= 			"Interested Person"
		verbose_name_plural = 			"Interested People"

