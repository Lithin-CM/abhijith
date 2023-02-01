from django.db import transaction
from rest_framework import status
from .pagination import paggination
from rest_framework.views import APIView
from django.core.paginator import Paginator
from rest_framework.response import Response
from .models import *
from .serializers import *


class UserRegisterList(APIView):
    def get(self,request):
        page = request.GET.get('page',1)
        limit=request.GET.get('limit',20)
        try:
            user = User.objects.filter(is_active=True) 
            paginator = Paginator(user, limit) 
            result = paggination(page,paginator)    
            serializer = UserRegisterSerializer(result,many=True)
            return Response({"status":200,"message":"successs","data":serializer.data,
                             "count":paginator.count,"pages":paginator.num_pages},status=status.HTTP_200_OK)  
        except Exception as Err:    
            return Response({"status":500,"message":str(Err)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)      
      
    def post(self,request):
        try:
            with transaction.atomic():
                user = User(
                            org_id=request.data['org_id'],
                            name=request.data['name'],
                            description=request.data['description'],
                            media_url=request.data['media_url'],
                            status=request.data.get('status','active')
                         )
                user.save()
                return Response({"status":201,"success":"Created..."},status=status.HTTP_201_CREATED) 
        except Exception as Err:
            return Response({"status":"No data.","error":str(Err)},status=status.HTTP_500_INTERNAL_SERVER_ERROR) 
