from django.core.management.base import BaseCommand
from jobData.models import JobData
from django.conf import settings
import requests
import json


URL = 'https://jobs.github.com/positions.json?description=api'

class Command(BaseCommand):
   
    def handle(self, *args, **options):
        response = requests.get(URL)
        data_list = response.json()
        JobData.objects.all().delete()
        self.stdout.write('Refreshing the data')
        for sample in data_list:
            try:
                refreshing = JobData(
                    vac_id = sample['id'],
                    vac_type = sample['type'],
                    url = sample['url'],
                    created_at = sample['created_at'],
                    company = sample['company'],
                    company_url = sample['company_url'],
                    location = sample['location'],
                    title = sample['title'],
                    description = sample['description'],
                    how_to_apply = sample['how_to_apply'],
                    company_logo = sample['company_logo'],
                    )   
                refreshing.save()
            except:
                self.stdout.write('Failed to add data')
        
        self.stdout.write('Added data')
