Init:
-----

$ pip install -r requirements.txt
$ python migrate.py db init
$ python migrate.py db migrate
$ python migrate.py db upgrade


Add new resource:
-----------------

$ python generator.py Book
$ python migrate.py db migrate
$ python migrate.py db upgrade
Edit app.py and add reference to Book resource and its routes
$ python app.py
Then navigate to: http://localhost:8081/service/api/book
