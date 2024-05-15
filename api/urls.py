from django.urls import path
from .views import ItemsViews

urlpatterns = [
    path('items/', ItemsViews.as_view(), name='all-items'),
    path('create-items/', ItemsViews.as_view(), name='create-items')
]
