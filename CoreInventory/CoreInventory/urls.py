from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('Users.urls')),
    path('location/',include('LocationApp.urls')),
    path('warehouse/',include('WarehouseApp.urls')),
    path('stock/',include('StockApp1.urls')),
    path('receipt/',include('ReceiptApp1.urls')),
]