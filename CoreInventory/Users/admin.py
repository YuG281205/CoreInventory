
from django.contrib import admin
from .models import User
from LocationApp.models import Location
from WarehouseApp.models import Warehouse
from StockApp1.models import Stock
from ReceiptApp1.models import Receipt
admin.site.register(User)

class LocationAdmin(admin.ModelAdmin):
    list_display = ('id', 'district', 'state', 'pincode')  # columns in admin list
    search_fields = ('name', 'state', 'pincode')        # enable search
    list_filter = ('state',)                             # filter by state

admin.site.register(Location, LocationAdmin)

admin.site.register(Warehouse)

admin.site.register(Stock)

admin.site.register(Receipt)