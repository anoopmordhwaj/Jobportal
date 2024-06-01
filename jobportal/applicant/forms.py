from django import forms
from .models import Applied_jobs

class PDFFileForm(forms.ModelForm):
    class Meta:
        model = Applied_jobs
        fields = [  'applicant_resume', 'applicant_coverletter' ]