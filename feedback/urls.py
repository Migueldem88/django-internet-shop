from django.urls import path
from . import views

app_name = 'feedback'
urlpatterns = [
    path('create/', views.feedback_create, name='feedback_create'),
    ]