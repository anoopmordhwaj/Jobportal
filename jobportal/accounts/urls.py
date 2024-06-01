from django.contrib import admin
from accounts import views
from .views import SignupView

from django.urls import path , include


urlpatterns = [
    # path('signup/',  SignupView.as_view() , name="signup"),
    

]
