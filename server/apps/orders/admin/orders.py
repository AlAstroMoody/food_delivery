from django.contrib import admin

from apps.orders.models import Order, DishInOrder, Status


class DishInOrderInline(admin.TabularInline):
    model = DishInOrder
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created',
                    'status', 'total_price', 'comments')
    inlines = [DishInOrderInline]


@admin.register(DishInOrder)
class DishInOrderAdmin(admin.ModelAdmin):
    list_display = ('order', 'dish', 'count', 'price_per_item', 'total_price')


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = 'name', 'is_active'
