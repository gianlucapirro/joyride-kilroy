from django.contrib import admin
from .models import Registrant
import csv
from django.http import HttpResponse

def export_to_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="registrants.csv"'

    writer = csv.writer(response)
    writer.writerow([
            "First Name",
            "Last Name",
            "Email",
            "Phone",
            "Roadtrip",
            "Email Friend1",
            "Email Friend2",
    ])

    for registrant in queryset:
        writer.writerow([
            registrant.first_name,
            registrant.last_name,
            registrant.email,
            registrant.phone,
            registrant.roadtrip,
            registrant.email_friend1,
            registrant.email_friend2,
        ])

    return response

export_to_csv.short_description = "Export to CSV"

@admin.register(Registrant)
class RegistrantAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
        "email",
        "phone",
        "roadtrip",
        "email_friend1",
        "email_friend2",
    )
    actions = [export_to_csv]
