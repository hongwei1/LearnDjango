This is just for memory some commands:

By running makemigrations, you’re telling Django that you’ve made some changes 
to your models (in this case, you’ve made new ones) and that you’d like the changes to be stored as a migration.
   
    python manage.py makemigrations polls
    
There’s a command that will run the migrations for you and manage your database schema automatically 

    python manage.py sqlmigrate polls 0001

    
    
If you’re interested, you can also run **python manage.py check**; this checks for any problems in your project without making migrations or touching the database.
Now here is the migrate 

    python manage.py migrate
        
3 steps guide to making model changes:
   
    Change your models (in models.py).
    Run python manage.py makemigrations to create migrations for those changes
    Run python manage.py migrate to apply those changes to the database.        