from django.contrib import admin
from .models import employee_data


# Register your models here.


class emp_admin(admin.ModelAdmin):
    list_display = ['emp_id', 'emp_name', 'emp_sal', 'emp_city']

admin.site.register(employee_data, emp_admin)
