from django.shortcuts import render, redirect, get_object_or_404
from .models import Warehouse
from LocationApp.models import Location

def warehouse_list(request):
    warehouses = Warehouse.objects.select_related('location').all()

    context = {
        'warehouses': warehouses
    }

    return render(request, 'warehouse_list.html', context)

def add_warehouse(request):
    locations = Location.objects.all()

    if request.method == "POST":
        w_name = request.POST.get('w_name')
        w_location = request.POST.get('w_location')
        location_id = request.POST.get('location')

        location = Location.objects.get(id=location_id)

        Warehouse.objects.create(
            w_name=w_name,
            w_location=w_location,
            location=location
        )

        return redirect('warehouse_list.html')

    return render(request, 'warehouse_test.html', {'locations': locations})

def edit_warehouse(request, w_id):
    warehouse = get_object_or_404(Warehouse, w_id=w_id)
    locations = Location.objects.all()

    if request.method == "POST":
        warehouse.w_name = request.POST.get('w_name')
        warehouse.w_location = request.POST.get('w_location')

        location_id = request.POST.get('location')
        warehouse.location = Location.objects.get(id=location_id)

        warehouse.save()

        return redirect('warehouse_list.html')

    context = {
        'warehouse': warehouse,
        'locations': locations
    }

    return render(request, 'warehouse_test.html', context)

def delete_warehouse(request, w_id):
    warehouse = get_object_or_404(Warehouse, w_id=w_id)
    warehouse.delete()
    return redirect('warehouse_list.html')