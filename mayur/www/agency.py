import frappe

def get_context(context):
    vehicles = frappe.get_list(
        "Vehicle",
        fields=["model", "make", "vehicle_image"],
        filters={"is_publish": 1}
    )
    context.vehicles = vehicles
    return context