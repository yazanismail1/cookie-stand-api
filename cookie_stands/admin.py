from django.contrib import admin
from .models import CookieStand

# Register your models here.
class CookieStandAdmin(admin.ModelAdmin):
    list_display = ("location", "owner", "description", "hourly_sales", "minimum_customers_per_hour", "maximum_customers_per_hour", "average_cookies_per_sale")
    prepopulated_fields = {"slug": ("location",)}

admin.site.register(CookieStand, CookieStandAdmin)

