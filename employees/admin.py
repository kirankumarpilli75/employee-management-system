from django.contrib import admin
from .models import Employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        'employee_code',
        'full_name',
        'email',
        'department',
        'designation',
        'salary',
        'date_of_joining',
    )
    list_filter = ('department', 'date_of_joining')
    search_fields = ('full_name', 'email', 'designation', 'phone_number')
    ordering = ('-created_at',)
    date_hierarchy = 'date_of_joining'
    list_per_page = 25
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        ('Personal Information', {
            'fields': ('full_name', 'email', 'phone_number', 'profile_photo')
        }),
        ('Employment Details', {
            'fields': ('department', 'designation', 'salary', 'date_of_joining')
        }),
        ('Record Info', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )

    @admin.display(description='Employee ID')
    def employee_code(self, obj):
        return obj.employee_code


admin.site.site_header = 'Employee Management System'
admin.site.site_title = 'EMS Admin'
admin.site.index_title = 'Administration Dashboard'
