from django.db import models

# Create your models here.
   
class Employer_details(models.Model):        
    employer_name = models.CharField(max_length=50)
    company_name = models.CharField(max_length=50)
    employer_no = models.IntegerField(default=0)
    employer_email = models.EmailField()
    employer_age = models.BigIntegerField(default=0)
    employer_address = models.CharField(max_length=400)
    employer_gender = models.CharField(max_length=15)

    def __str__(self) -> str:
        return self.employer_name

class Job(models.Model):
    company_name = models.CharField(max_length=100)
    company_desc =  models.CharField(max_length=400)
    company_location =  models.CharField(max_length=100)
    job_role =  models.CharField(max_length=400)
    job_desc =  models.CharField(max_length=400)
    salary = models.IntegerField(default=0)
    requied_experience = models.IntegerField(default=0)
    post_date = models.DateField()
    application_last_day = models.DateField()
    skill_required = models.CharField(max_length=200)
    dis_type = models.CharField(max_length=100)


    def __str__(self) -> str:
        return self.job_role