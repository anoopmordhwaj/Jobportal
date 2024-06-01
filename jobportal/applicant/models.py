from django.db import models

# Create your models here.

class Applicant_details(models.Model):        
    applicant_name = models.CharField(max_length=50)
    applicant_email = models. EmailField()
    applicant_no = models.IntegerField(default=0)
    applicant_age = models.BigIntegerField(default=0)
    disability_type = models.CharField(max_length=5000)
    applicant_address = models.CharField(max_length=4000)
    applicant_skills = models.CharField(max_length=4000)
    applicant_education = models.CharField(max_length=4000)
    applicant_gender = models.CharField(max_length=15)

    def __str__(self):
        return self.applicant_name
    
class Applied_jobs(models.Model):
    Applied_id = models.IntegerField(default=0)
    company_name = models.CharField(max_length=50, default='0000000')
    applicant_resume = models.FileField(upload_to="resume/",null = False, default='')
    applicant_coverletter = models.CharField(max_length=2000, null = False, default='0000000')

    def __str__(self):
        return self.applicant_coverletter[:19]
    






    
    
class Color(models.Model):
    color_name = models.CharField(max_length = 100)

    def __str__(self):
        return self.color_name
        
class Person(models.Model):
    color = models.ForeignKey(Color,null = True, blank = True,  on_delete = models.CASCADE, related_name = "color")
    name = models.CharField(max_length = 50)
    age = models.IntegerField(default = 0)
    