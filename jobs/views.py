from rest_framework.exceptions import NotFound
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination

from jobs.serializers import JobSerializer
from .models import Jobs

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
    def delete(self, request, pk):
        job = Jobs.objects.get(pk=pk)
        job.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        