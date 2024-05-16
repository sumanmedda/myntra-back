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
    return Response({"status":200,"message": "Items Fetched", "items":serializer.data},)
  
  # Create Items
  def post(self, request):
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
    return Response({"status":201,"message": "Item Created"},)
  

  # // Demo Data
  # {
  #               "id": 1,
  #               "image": "https://drive.google.com/thumbnail?id=1JA0PCO16JPNtlpy4j7VdZtEF-AZkVdk8",
  #               "company": "Apple",
  #               "item_name": "iphone15",
  #               "original_price": 69999,
  #               "current_price": 49500,
  #               "discount_percentage": 20,
  #               "return_period": 7,
  #               "delivery_date": "2024-05-17",
  #               "description": "DYNAMIC ISLAND COMES TO IPHONE 15 — Dynamic Island bubbles up alerts and Live Activities — so you don’t miss them while you’re doing something else. You can see who’s calling, track your next ride, ch",
  #               "rating": 5
  #           },