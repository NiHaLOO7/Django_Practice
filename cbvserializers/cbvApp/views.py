from django.shortcuts import render
from .models import Student
from django.http import Http404

from .serializers import StudentSerializer

from rest_framework.response import Response
from rest_framework import status, generics, mixins
from rest_framework.decorators import APIView
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from rest_framework import filters

"""
# filters is just like "like" in sql..
# '^' is to match first letter
# '=' Exact match
# '@' Full text search(not recommended currently)
# '$' regular expression search
# How to pass => search_fields = ['^id','=name','$score'].. 
# These criterions should be passed in url itself
"""


from django_filters.rest_framework import DjangoFilterBackend


# Override the pagination to customize it
class StudentViewPagination(PageNumberPagination):
    page_size = 1

# Create your views here.

# Views with viewsets .. It supports both urls with or without primary key
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = StudentViewPagination #LimitOffsetPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['name','score']
    search_fields = ['id','name']
    ordering_fields = ['name','score']
    ordering = ['id']
    # Default ordering on simple search without setting the url




'''
# ============================================================================================ #

# Views with generics ApiViews
class StudentList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


# ============================================================================================ #
'''
'''
# ============================================================================================ #


# Views With Mixins
class StudentList(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self,request):
        return self.list(request)

    def post(self,request):
        return self.create(request)
 

class StucentDetail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self,request,pk):
        return self.retrieve(request,pk)

    def put(self,request,pk):
        return self.update(request,pk)

    def delete(self,request,pk):
        return self.destroy(request,pk)


# ============================================================================================ #
'''
'''
# ============================================================================================ #


# Class Based Views
class StudentList(APIView):
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
class StudentDetail(APIView):
    def get_object(self,pk):
        try:
            return Student.objects.get(pk=pk)
        except:
            raise Http404

    def get(self,request,pk):
        student = self.get_object(pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def put(self,request,pk):
        student = self.get_object(pk)
        serializer = StudentSerializer(student,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        student = self.get_object(pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ============================================================================================ #
'''