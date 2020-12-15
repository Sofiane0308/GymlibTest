from django.urls import path
from jobqueue import views

urlpatterns = [
    path('jobs', views.jobs, name="jobs"),
    path('job', views.job, name="job"),
]