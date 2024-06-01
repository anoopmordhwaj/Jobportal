from django.contrib import admin
from employer import views
from django.urls import path

urlpatterns = [
    
    path('employer_details/', views.employer_details , name="employer_details"),
    path('employer_path/', views.employer_path , name="employer_path"),
    path('post_job/', views.post_job , name="post_job"),
    path('applied_applicant/', views.applied_applicant , name="applied_applicant"),
    path('pdf_view/<str:company>/' , views.pdf_view , name="pdf_view"),

]
