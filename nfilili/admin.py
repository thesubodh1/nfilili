from django.contrib import admin
from .models import EmailRegister,DetailRegistration

class DetailRegistrationAdmin(admin.ModelAdmin):
    list_display = ("full_name","business_name","description","location","email","latitude","longitude")


admin.site.register(EmailRegister)
admin.site.register(DetailRegistration,DetailRegistrationAdmin)
