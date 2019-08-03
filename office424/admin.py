from django.contrib import admin
from office424.models import *

# Register your models here.


class PersonInfoAdmin(admin.ModelAdmin):
    list_display = ['name', 'cardID', 'gender']


class TradeInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'establish', 'price', 'describe', 'finish']


admin.site.register(PersonInfo,PersonInfoAdmin)
admin.site.register(TradeInfo,TradeInfoAdmin)
