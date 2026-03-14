from django.shortcuts import render
from .models import Receipt
from rest_framework import viewsets
from .serializers import ReceiptSerializer



def receipt_list(request):
    receipts = Receipt.objects.select_related('reference').all()

    context = {
        'receipts': receipts
    }

    return render(request, 'receipt_lists.html', context)

class ReceiptViewSet(viewsets.ModelViewSet):
    queryset = Receipt.objects.select_related('reference').all()
    serializer_class = ReceiptSerializer