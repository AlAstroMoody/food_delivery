from django.contrib import admin

from apps.promo.models import Promo


@admin.register(Promo)
class PromoAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image')
