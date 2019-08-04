# spotdraft-exercise

A simple favorites app that lets us view/favorite Star Wars data. The data is loaded from the JSON API https://swapi.co/. 

## Running the Server

1. Install the requirements with the command `pip install -r requirements.txt`
2. Run the migrations with the command `python manage.py migrate`
2. Run the server with the command `python manage.py runserver`

The API will now be available http://localhost:8000/api

## Testing the app

Run the test cases with the command `python manage.py test`

## Endpoints

The following Endpoints are available in the API.

### List Planets

**Endpoint**: `/api/planets`

**Method**: GET

**Query Params**:

Name | Description
--- | --- 
page | Page number of the results to return. 
search | Search planets with this name.

**Response**:

Name | Description
--- | --- 
count | Total count of results found. 
next | Link to the next page of results.
previous | Link to the previous page of results.
results | List of planets.


### List Movies

**Endpoint**: `/api/movies`

**Method**: GET

**Query Params**:

Name | Description
--- | --- 
page | Page number of the results to return. 
search | Search planets with this name.

**Response**:

Name | Description
--- | --- 
count | Total count of results found. 
next | Link to the next page of results.
previous | Link to the previous page of results.
results | List of movies.


### Add Favorite Planet

**Endpoint**: `/api/planets/favorites`

**Method**: POST

**Input Data**:

Name | Description
--- | --- 
external_id | Id of the planet from the list planets result. 
name | Name of the planet.

**Response**:

Name | Description
--- | --- 
name | Name of the planet saved. 


### List Favorite Planets

**Endpoint**: `/api/planets/favorites`

**Method**: GET

**Query Params**:

Name | Description
--- | --- 
page | Page number of the results to return. 

**Response**:

Name | Description
--- | --- 
count | Total count of results found. 
next | Link to the next page of results.
previous | Link to the previous page of results.
results | List of favorite planets.

### Add Favorite Movie

**Endpoint**: `/api/planets/movies`

**Method**: POST

**Input Data**:

Name | Description
--- | --- 
external_id | Id of the planet from the list planets result. 
title | Title of the planet.

**Response**:

Name | Description
--- | --- 
title | Title of the planet saved. 


### List Favorite Movies

**Endpoint**: `/api/planets/movies`

**Method**: GET

**Query Params**:

Name | Description
--- | --- 
page | Page number of the results to return. 

**Response**:

Name | Description
--- | --- 
count | Total count of results found. 
next | Link to the next page of results.
previous | Link to the previous page of results.
results | List of favorite movies.