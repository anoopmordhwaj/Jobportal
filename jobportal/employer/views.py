from django.shortcuts import render, redirect
from .models import Employer_details , Job
from django.http import FileResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
@login_required(login_url="/login/")
def employer_details(request):
        user = User.objects.filter(username = request.user).all().values()
        print(user[0].get('email'))
        current_user_email = user[0].get('email')
        # user1 = Employer_details.objects.filter(employer_email = current_user_email)
        user1 = Employer_details.objects.filter(employer_email = current_user_email).all()
        print(user1)
        if not user1.exists():
            if request.method ==  'POST':
                ed = Employer_details()

                ed.employer_name = request.POST.get('name', '')
                ed.employer_email = request.POST.get('email', '')
                ed.employer_gender = request.POST.get('gender', '')
                ed.employer_age = request.POST.get('age', '')
                ed.employer_no = request.POST.get('no', '')
                ed.employer_address = request.POST.get('address', '')
                ed.company_name = request.POST.get('company_name','')

                ed.save()
            return render(request , 'employer_details.html')
        else:
             return render(request, 'employer_path.html')

@login_required(login_url="/login/")
def employer_path(request):
    return render(request , 'employer_path.html')

@login_required(login_url="/login/")
def post_job(request):
    if request.method == "POST":
        jb = Job()
        jb.company_name = request.POST.get('cname','')
        jb.company_desc = request.POST.get('desc','')
        jb.company_location = request.POST.get('location','')
        jb.job_role = request.POST.get('role','')
        jb.job_desc = request.POST.get('jdesc','')
        jb.salary = request.POST.get('salary','')
        jb.requied_experience = request.POST.get('experience','')
        jb.post_date = request.POST.get('pdate','')
        jb.application_last_day = request.POST.get('ldate','')
        jb.skill_required = request.POST.get('skill','')
        jb.dis_type = request.POST.get('type','')

        jb.save()

    return render(request , 'post_job.html')

from applicant.models import Applicant_details, Applied_jobs

@login_required(login_url="/login/")
def applied_applicant(request):

    j = Employer_details.objects.all()
    lst = []
    for i in j:
        d = Applied_jobs.objects.filter(company_name = i.company_name).values()
        lst.append(d)
    
    params = { 'd':lst }
    return render(request, 'applied_applicant.html', params)

@login_required(login_url="/login/")
def pdf_view(request, company):
        info = Applied_jobs.objects.filter(company_name = company).values()
        for i in info: 
            resume = i['applicant_resume']

        return FileResponse(open(f'media/{resume}', 'rb'))
