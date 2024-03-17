from django.urls import path
from .views import AllJobs, JobDetail

urlpatterns = [
    path('', AllJobs.as_view(), name='all_jobs'),
    path('<str:pk>', JobDetail.as_view(), name='job_detail'),
]
