This is just for memory some commands:

## Install dependencies

```bash
$ virtualenv --python=python3 ./venv
$ source ./venv/bin/activate
(venv)$ pip install -r requirements.txt
```

# create the new App `mayApp` processes:
1st: python manage.py startapp myApp
Will create myApp folder and some *.py files.

2rd: register the app to setting.py `INSTALLED_APPS`

3rd: define the Model in the models.py 

4th: create the tables in the database.

    4.1 create the generate migration file : python manage.py makemigrations myApp
        only create the 0001_intial.py under the migration folder, not table in the database.
    
    4.2 do the migration: python manage.py migrate
    
5th: when we have the database tables, then we can create some data in the terminal
```
   5.1 get to the Django shell: python manage.py shell
   5.2 try these : myApp/databaseDemo.py 
```    

6th: start the server:

    python manage.py runserver 127.0.0.1:8081

7h: create the admin user:
   
     python manage.py createsuperuser
     user: admin pass: admin
     
     Chinse: LANGUAGE_CODE = 'zh-hans'
     
8 manage my own tables in admin
    
    8.1 modify the myApp/admin.py, register your table there. 
    8.2 moidfy the amdin page yourself.
    Just check this file: myApp/admin.py
         