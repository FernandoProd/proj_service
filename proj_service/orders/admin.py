from django.contrib import admin
from .models import Order, Detail, OrderDetail

#admin.site.register(Order)
admin.site.register(Detail)
admin.site.register(OrderDetail)


class OrderDetailInline(admin.TabularInline):  # Можно также StackedInline
    model = OrderDetail
    extra = 1

class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderDetailInline]

admin.site.register(Order, OrderAdmin)