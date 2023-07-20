# Search_app

Search App is a Django web application that allows users to search for dishes, view restaurant details, and import data from a CSV file.

## Features

- Search for dishes by name
- Display search results with minimum prices
- Pagination for search results
- View detailed information about a restaurant
- Import data from a CSV file to populate the database

## Installation

1. Clone the repository:
```
git clone https://github.com/your-username/search_app.git
```

2. Navigate to the project directory:
```
 cd search_app
```

3. Install the project dependencies:
```
 pip install -r requirements.txt
```

4. Run the migrations:
```
python manage.py migrate
```

5. Start the development server:
```
python manage.py runserver
```

6. Access the application at [http://localhost:8000](http://localhost:8000)

7. To import the csv file keep it in the location:
```
Search_app\search_app\file.csv
```
After that go:
```
http://127.0.0.1:8000/import/
```

This will import the csv file onto the databse.


## Usage

- On the homepage, enter a dish name in the search input and click the "Search" button.
- The search results will be displayed, showing the dish name, restaurant name, and price.
- Use the pagination links at the bottom to navigate through the search results.
- Click on the "View Details" link to see more information about a restaurant.
- To import data from a CSV file, click on the "Import CSV" button and follow the instructions.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

