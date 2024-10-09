# superheroes
This project displays superheroes along with their strengths. It uses a RESTful API to create route for GET, POST and PATCH request. The application includes a databse to persist data and utilize Flask-SQLAlchemy for database mangement.

# Project set up
1. Enter virtual enviroment:
         pipenv install
         pipenv shell
2. Install dependencies:
        pip install Flask
        pip install Flask-migrate
        pip install marshmallow
        pip install Flask-Restful    
        pip install requests  
3. Run the project
    cd server
    python app.py