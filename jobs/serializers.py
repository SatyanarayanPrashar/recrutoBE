from rest_framework import serializers
from .models import JobApplicants, Jobs

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jobs
        fields = '__all__'

class JobApplicantsSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobApplicants
        fields = ['job_id', 'applicant_ids']