from django.contrib import admin
from .models import Order, OrderDetail, Detail

# Inline для связи Order ↔ OrderDetail
class OrderDetailInline(admin.TabularInline):  # Можно также использовать StackedInline
    model = OrderDetail
    extra = 1
    autocomplete_fields = ['detail']

# Админ для Order — с Inline
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_number', 'customer', 'created_at', 'priority', 'status', 'deadline')
    search_fields = ('customer',)
    inlines = [OrderDetailInline]  # <-- Вот это главное!

# Админ для OrderDetail
@admin.register(OrderDetail)
class OrderDetailAdmin(admin.ModelAdmin):
    list_display = ('order', 'detail', 'quantity', 'status')
    search_fields = ('detail__name',)

# Админ для Detail
@admin.register(Detail)
class DetailAdmin(admin.ModelAdmin):
    list_display = ('number', 'name', 'material', 'prep_time', 'piece_time')
    search_fields = ('name', 'number')