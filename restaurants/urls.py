from django.conf.urls import patterns, url
from django.views.generic import ListView, DetailView
from restaurants.models import Food, Restaurant

urlpatterns = patterns('restaurants.views',
    url(r'^$',
        ListView.as_view(
            queryset=Food.objects.all(),
            template_name='restaurants/index.html'),
        name='index'),
    url(r'^food/(?P<food_id>\d+)/$', 'choose_town', name='choose_town'),
    url(r'^food/(?P<food_id>\d+)/town/(?P<town_id>\d+)/$', 'choose_restaurant', name='choose_restaurant'),
    url(r'^rest/(?P<pk>\d+)/$',
        DetailView.as_view(
            model=Restaurant,
            template_name='restaurants/restaurant.html'),
        name='restaurant'),
)
