from django.contrib import admin
from .models import Patient, Doctor, PatientDoctorMapping

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'contact_number', 'created_at')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('gender', 'created_at')

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'specialization', 'license_number', 'email')
    search_fields = ('first_name', 'last_name', 'specialization', 'license_number')
    list_filter = ('specialization', 'created_at')

@admin.register(PatientDoctorMapping)
class PatientDoctorMappingAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'assigned_date', 'active')
    search_fields = ('patient__first_name', 'patient__last_name', 'doctor__first_name', 'doctor__last_name')
    list_filter = ('active', 'assigned_date')
