from django.shortcuts import render
from rest_framework.views import APIView
from .models import Items
from .serializers import ItemSerializer
from rest_framework.response import Response

# Create your views here.
class ItemsViews(APIView):
  # Get Items
  def get(self,request):
    items = Items.objects.all()
    
    serializer = ItemSerializer(items, many=True)
    return Response({"status":200,"message": "Items Fetched", "items":[serializer.data]},)
  
  # Create Items
  def post(self, request):
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
    return Response({"status":201,"message": "Item Created"},)