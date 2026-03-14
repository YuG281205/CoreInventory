/* Load dashboard data */

fetch("/api/dashboard-data/")
.then(response => response.json())
.then(data => {

    /* Location Data */

    document.getElementById("Location").innerText = data.location;
    document.getElementById("location_id").innerText = data.location_id;
    document.getElementById("location_name").innerText = data.location_name;
    document.getElementById("location_pincode").innerText = data.location_pincode;


    /* Warehouse Data */

    document.getElementById("Warehouse").innerText = data.warehouse;
    document.getElementById("warehouse_id").innerText = data.warehouse_id;
    document.getElementById("warehouse_name").innerText = data.warehouse_name;
    document.getElementById("warehouse_location").innerText = data.warehouse_location;
    document.getElementById("warehouse_pincode").innerText = data.warehouse_pincode;


    /* Stock Data */

    document.getElementById("Stock").innerText = data.stock;
    document.getElementById("product").innerText = data.product;
    document.getElementById("per_unit_cost").innerText = data.per_unit_cost;
    document.getElementById("on_hand").innerText = data.on_hand;
    document.getElementById("free_to_use").innerText = data.free_to_use;

})
.catch(error => {
    console.log("Error loading dashboard data:", error);
});


/* Navigation */

function openLocation(){
window.location.href = "/api/location/";
}

function openWarehouse(){
window.location.href = "/api/warehouse/";
}

function openStock(){
window.location.href = "/api/stock/";
}


/* Logout */

function logout(){
window.location.href = "/api/login/";
}