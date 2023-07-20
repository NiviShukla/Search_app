import csv
from django.shortcuts import render , get_object_or_404
from .models import Restaurant, MenuItem
from django.db.models import Q
from django.core.paginator import Paginator


def import_dish_data(request):
    with open('restaurants_small.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            name = row[1]
            location = row[2]
            items = row[3]
            lat_long = row[4]
            full_details = row[5]

            restaurant, _ = Restaurant.objects.get_or_create(
                name=name,
                location=location,
                lat_long=lat_long,
                full_details=full_details
            )

            dish_items = eval(items)  # Convert the items string to a dictionary

            for dish, price in dish_items.items():
                menu_item = MenuItem.objects.create(
                    restaurant=restaurant,
                    name=dish,
                    price=float(price.split()[0]) if 'onwards' in price else float(price)
                )

    return render(request, 'search.html')



def search_dish(request):
    query = request.GET.get('query')
    results = []
    restaurants = []
    page_obj = None

    if query:
        # Perform the search based on the query
        results = MenuItem.objects.filter(name__icontains=query).select_related('restaurant').order_by('price')

        # Get the corresponding restaurants
        restaurants = [result.restaurant for result in results]

        # Paginate the results
        paginator = Paginator(results, 10)  # Display 10 results per page

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number) if page_number else paginator.get_page(1)  # Set page_obj to the first page if page_number is not provided

    return render(request, 'search.html', {'results': results, 'query': query, 'restaurants': restaurants, 'page_obj': page_obj})



def restaurant_details(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
    full_details = restaurant.full_details  # Assuming full_details is a dictionary
    return render(request, 'restaurant_details.html', {'restaurant': restaurant, 'full_details': full_details})
