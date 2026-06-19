from django.contrib import admin
from .models import Organization

admin.site.register(Organization)


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "email",
        "created_at"
    )