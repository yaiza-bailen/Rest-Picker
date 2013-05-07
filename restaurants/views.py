from django.shortcuts import render
from restaurants.models import Restaurant, Town 

# Create your views here.
def choose_town(request, food_id):
    rest_list = Restaurant.objects.filter(food=food_id)
    town_list=[]
    for r in rest_list:
        c = Town.objects.get(id=r.town.id)
        if c not in town_list:
            town_list.append(c)
    return render(request, 'restaurants/choose_town.html', {'food_id':food_id, 'town_list':town_list})

def rest_list(request,food_id,town_id):
    rests = Restaurant.objects.filter(food__id=food_id, town__id=town_id)
    return render(request, 'restaurants/choose_restaurant.html', {'rests':rests})

