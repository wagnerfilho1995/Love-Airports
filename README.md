# App Love-Airports
A SPA application dedicated to analyzing several Brazilian airports and their domestic flights.

## Quickstart

### Backend

```system
$ cd backend
```

#### to run for the first time:

1. Install Python;
2. Install dependencies:

```system
$ pip install -r requirements.txt
```

3. Install PostgreSQL;

4. Create a database in PostegreSQL;

5. Create a file `conf/secret.py` with the following information:

```python
SECRET_KEY = 'Your_secret_key'
DEBUG = True
ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '<DATABASE NAME>', # Your Postgres database name.
        'USER': '<YOUR USER>', # Your Postgres user
        'PASSWORD': 'PASSWORD', # Your Postgres password
        'HOST': 'localhost', 
        'PORT': '5432',
    }
}
```

6. Update the database:

```system
$ python manage.py migrate
```

#### Now, Run the local server

```system
$ python manage.py runserver
```
### Fill database:

1. To acess Server on browser use the url;
```
http://localhost:8000/
```

2. Acess the following endpoint to create Airports models;
```
http://localhost:8000/core/airports/build_airports_database/
```

3. Access the endpoint below to create a 20x20 trip matrix, where 
each trip is stored in the bank and the best flight option for each 
trip is also calculated;
```
http://localhost:8000/core/airports/airports_X_airports/
```



### Frontend

```system
$ cd frontend
```

#### to run for the first time:

1. Install NodeJS;

2. Install dependencies:

```system
$ npm install
```

#### Now, Run the local server

```system
$ quasar dev
```

### Software

#### Home page

The home page shows us the distribution of the number of airports throughout Brazil. There is a side menu with links to access specific pages dedicated to travel and airports. Click to browse these pages.

![alt text](https://github.com/wagnerfilho1995/Love-Airports/blob/main/Pages-imgs/Home.png?raw=true)

#### Trips

The trips page illustrates a table with information regarding the longest trips recorded in the system.

![alt text](https://github.com/wagnerfilho1995/Love-Airports/blob/main/Pages-imgs/Viagens.png?raw=true)

#### Airports

The airports page illustrates a table with information on all airports registered in the database, also describing, for each airport, its closest and farthest neighbor.

![alt text](https://github.com/wagnerfilho1995/Love-Airports/blob/main/Pages-imgs/Aeroportos.png?raw=true)

