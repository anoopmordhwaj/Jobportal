from django.contrib import admin
from .models import Applicant_details , Applied_jobs, Person, Color

# Register your models here
admin.site.register(Applicant_details)
admin.site.register(Applied_jobs)
admin.site.register(Person)
admin.site.register(Color)