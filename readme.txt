Init:
-----

$ pip install -r requirements.txt
$ python migrate.py db init
$ python migrate.py db migrate
$ python migrate.py db upgrade


Add new resource:
-----------------

1. Use generator:
$ python generator.py Book

2. Modify codes according to specs
Modify model attributes/fields
Update resource mappings

3. Update data source
$ python migrate.py db migrate
$ python migrate.py db upgrade

4. Run app
$ python app.py

5. Test URL
Then navigate to: http://localhost:8081/service/api/book
