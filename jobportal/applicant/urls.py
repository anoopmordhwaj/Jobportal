from django.contrib import admin
from applicant import views
from applicant.views import PersonAPI, PersonViewSet, RegisterAPI, LoginAPI
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'people', PersonViewSet, basename="people")
urlpatterns = router.urls

urlpatterns = [
    
    path('applicant_details/', views.applicant_details , name="applicant_details"),
    path('view_jobs/', views.view_jobs , name="view_jobs"),
    path('apply_now/<int:myid>/' , views.apply_now , name="apply_now" ),
    path('job_details/<int:myid>/' , views.job_details , name="job_details" ),
    # below path is to check apis
    path('person/', views.person , name="person"),
    path('api_login/', views.api_login , name="api_login"),
    path('persons/', PersonAPI.as_view()),
    path('register/', RegisterAPI.as_view()),
    path('login/', LoginAPI.as_view()),
    path("", include(router.urls)),

] 

