from django.shortcuts import render, get_object_or_404
from restaurants.models import Restaurant, Town 

# Create your views here.
def choose_town(request, food_id):

    rest_list = Restaurant.objects.filter(food=food_id)
    town_list=[]
    for r in rest_list:
        t = Town.objects.get(id=r.town.id)
        if t not in town_list:
            rests = Restaurant.objects.filter(food__id=food_id, town__id=t.id)
            town_list.append({'town':t, 'count':len(rests)})
    return render(request, 'restaurants/choose_town.html', {'food_id':food_id, 'town_list':town_list})

def choose_restaurant(request,food_id,town_id):
    rests = Restaurant.objects.filter(food__id=food_id, town__id=town_id)
    return render(request, 'restaurants/choose_restaurant.html', {'rests':rests})

def restaurant(request, rest_id, message=''):
    rest = Restaurant.objects.get(id=rest_id)
    rest_menu = rest.menu.split(';')
    rest_menu = [e for e in rest_menu if e not in ('',' ')]
    return render(request, 'restaurants/restaurant.html', {'restaurant':rest, 'rest_menu':rest_menu, 'message':message})

def vote(request, rest_id):
    rest = get_object_or_404(Restaurant, pk=rest_id)

    votes = rest.votes
    submitted = request.POST['note_utilisateur']
    average = (votes + int(submitted))/2
    rest.votes = average
    rest.save()

    rest_menu = rest.menu.split(';')
    rest_menu = [e for e in rest_menu if e not in ('',' ')]

    message='Thanks for your vote!'

    return render(request, 'restaurants/restaurant.html', {'restaurant':rest, 'rest_menu':rest_menu, 'message':message})
