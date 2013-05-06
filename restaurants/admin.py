from django.contrib import admin
from restaurants.models import Restaurant, Food, City

class RestaurantAdmin(admin.ModelAdmin):
    fieldsets = [
            ('Description',{'fields': ['name','desc','menu']}),
            ('Address',{'fields':['address','post_code','city']}),
            ('Contact',{'fields':['web','phone']}),
            ('Food',{'fields':['food']}),
            ]

admin.site.register(Restaurant,RestaurantAdmin)
admin.site.register(Food)
admin.site.register(City)
