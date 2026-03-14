# urls.py
from django.urls import path
from .views import LocationListAPI, location_list_page

urlpatterns = [
    path('locations/', location_list_page, name='location_list_page'),  # HTML page
    path('api/locations/', LocationListAPI.as_view(), name='api_locations'),  # JSON API
]