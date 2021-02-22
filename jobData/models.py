
from django.db import models

class JobData(models.Model):
	vac_id = models.CharField('id', max_length=200)
	vac_type = models.CharField('type', max_length=200)
	url = models.URLField('url')
	created_at = models.CharField('created at', max_length=200)
	company = models.CharField('company', max_length=200)
	company_url = models.URLField('company url', null = True)
	location = models.CharField('location', max_length=200)
	title = models.CharField('title', max_length=400)
	description = models.TextField('description')
	how_to_apply = models.URLField('how to apply')
	company_logo = models.URLField('company logo', null = True)


	def __str__(self):
		return self.company


