from rest_framework.exceptions import NotFound
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination

from jobs.serializers import JobApplicantsSerializer, JobSerializer
from .models import JobApplicants, Jobs

class AllJobs(APIView):
    def get(self, request):
        paginator = PageNumberPagination()
        paginator.page_size = 7
        jobs = Jobs.objects.all()
        result_page = paginator.paginate_queryset(jobs, request)
        serializer = JobSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)
        
    def post(self, request):
        serializer = JobSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class JobDetail(APIView):
    def get(self, request, pk):
        try:
            job = Jobs.objects.get(pk=pk)
        except:
            return Response({"error": "Job does not exist"}, status=status.HTTP_404_NOT_FOUND)
        serializer = JobSerializer(job)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, request, pk):
        job = Jobs.objects.get(pk=pk)
        job.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class JobApplicantsView(APIView):
    def get(self, request):
        job_applicants = JobApplicants.objects.all()
        serializer = JobApplicantsSerializer(job_applicants, many=True)
        for instance in serializer.data:
            instance['applicant_ids'] = instance['applicant_ids'].split(',')
        return Response(serializer.data)
    
    def post(self, request):
        serializer = JobApplicantsSerializer(data=request.data)
        if serializer.is_valid():
            job_id = serializer.validated_data['job_id']
            applicant_ids = serializer.validated_data['applicant_ids']

            try:
                job_applicants_instance = JobApplicants.objects.get(job_id=job_id)
                job_applicants_instance.applicant_ids += f',{applicant_ids}'
                job_applicants_instance.save()
                return Response(JobApplicantsSerializer(job_applicants_instance).data, status=status.HTTP_200_OK)
            except JobApplicants.DoesNotExist:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class FetchApplicant(APIView):
    def get(self, request, job_id):
        try:
            applicant = JobApplicants.objects.get(job_id=job_id)
            serializer = JobApplicantsSerializer(applicant)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except JobApplicants.DoesNotExist:
            return Response({"error": "Job applicant does not exist"}, status=status.HTTP_404_NOT_FOUND)
        
    def delete(self, request, job_id):
        try:
            applicant = JobApplicants.objects.get(job_id=job_id)
            applicant.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except JobApplicants.DoesNotExist:
            return Response({"error": "Job applicant does not exist"}, status=status.HTTP_404_NOT_FOUND)