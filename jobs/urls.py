from django.urls import path
from .views import AllJobs, FetchApplicant, JobApplicantsView, JobDetail

urlpatterns = [
    path('', AllJobs.as_view(), name='all_jobs'),
    path('jobid=<str:pk>', JobDetail.as_view(), name='job_detail'),

    path('jobapplicants/', JobApplicantsView.as_view(), name='job_applicants'),
    path('jobapplicantIds/<int:job_id>/', FetchApplicant.as_view(), name='job_applicantid'),
]
