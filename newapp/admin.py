from django.contrib import admin

from .models import customer


class CustomerView(admin.ModelAdmin):
    list_display = ('name', 'age', 'mobile')


admin.site.register(customer, CustomerView)
                                                                                                              