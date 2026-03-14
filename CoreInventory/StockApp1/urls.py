from django.urls import path
from .views import stock_list_page, StockListAPI

urlpatterns = [
    path('stocks/', stock_list_page, name='stock_list_page'),   # HTML page
    path('api/stocks/', StockListAPI.as_view(), name='api_stocks'),  # API
]