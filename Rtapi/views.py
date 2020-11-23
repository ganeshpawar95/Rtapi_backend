from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from .models import Project,Scan
from .serializers import ProjectSerializer,ScanSerializer
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status

class ProjectView(APIView):
  parser_classes = (MultiPartParser, FormParser)
  def post(self, request, *args, **kwargs):
    print('request.data',request.data)
    file_serializer = ProjectSerializer(data=request.data)
    if file_serializer.is_valid():
      file_serializer.save()
      return Response({'data':file_serializer.data,'message':'Project data add successfully!'}, status=status.HTTP_201_CREATED)
    else:
      return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  def put(self, request, pk, format=None):
        tutorial = Project.objects.get(pk=pk) 
        print(tutorial)
        serializer = ProjectSerializer(tutorial, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class ProjectupdateView(APIView):
  parser_classes = (MultiPartParser, FormParser)
  def put(self, request, pk, format=None):
        print(request.data)
        tutorial = Project.objects.get(pk=pk) 
        print(tutorial)
        serializer = ProjectSerializer(tutorial, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data':serializer.data,'message':'Project data Update successfully!'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'DELETE'])
def getprojectpdata(request):
    print(request)
    if request.method == 'GET':
        tutorials = Project.objects.all()
        tutorials_serializer = ProjectSerializer(tutorials, many=True)
        return JsonResponse(tutorials_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
   
    elif request.method == 'DELETE':
        count = Project.objects.all().delete()
        return JsonResponse({'message': '{} Project were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
@api_view(['GET', 'PUT', 'DELETE'])
def project_detail(request, pk):
    try: 
        tutorial = Project.objects.get(pk=pk) 
    except Project.DoesNotExist: 
        return JsonResponse({'message': 'The Project does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        tutorial_serializer = ProjectSerializer(tutorial) 
        return JsonResponse(tutorial_serializer.data) 
 
    elif request.method == 'PUT': 
        tutorial_data = JSONParser().parse(request) 
        tutorial_serializer = ProjectSerializer(tutorial, data=tutorial_data) 
        if tutorial_serializer.is_valid(): 
            tutorial_serializer.save() 
            return JsonResponse(tutorial_serializer.data) 
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        tutorial.delete() 
        return JsonResponse({'message': 'Project was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','POST', 'DELETE'])
def Scans(request):
    print(request)
    if request.method == 'GET':
        tutorials = Scan.objects.all()
        tutorials_serializer = ScanSerializer(tutorials, many=True)
        return JsonResponse(tutorials_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        tutorial_data = JSONParser().parse(request)
        print(tutorial_data)
        tutorial_serializer = ScanSerializer(data=tutorial_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return JsonResponse({'message': 'Scan data add successfully!'}, status=status.HTTP_201_CREATED) 
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Scan.objects.all().delete()
        return JsonResponse({'message': '{} Scan were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
@api_view(['GET', 'PUT', 'DELETE'])
def scan_detail(request, pk):
    try: 
        tutorial = Scan.objects.get(pk=pk) 
    except Scan.DoesNotExist: 
        return JsonResponse({'message': 'The Scan does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        tutorial_serializer = ScanSerializer(tutorial) 
        return JsonResponse(tutorial_serializer.data) 
 
    elif request.method == 'PUT': 
        tutorial_data = JSONParser().parse(request) 
        tutorial_serializer = ScanSerializer(tutorial, data=tutorial_data) 
        if tutorial_serializer.is_valid(): 
            tutorial_serializer.save() 
            return JsonResponse({'message': 'Scan was update successfully!','data':tutorial_serializer.data}) 
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        tutorial.delete() 
        return JsonResponse({'message': 'Scan was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)