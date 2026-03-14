from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ReceiptViewSet, receipt_list

router = DefaultRouter()
router.register(r'receipts', ReceiptViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('view/', receipt_list,name='recipt_page'),
    
]