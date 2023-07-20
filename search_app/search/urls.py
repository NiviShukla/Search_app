from django.urls import path
from .views import import_dish_data, search_dish , restaurant_details

urlpatterns = [
    path('import/', import_dish_data, name='import_dish_data'),
    path('', search_dish, name='search_dish'),
    path('restaurant/<int:restaurant_id>/', restaurant_details, name='restaurant_details'),
]