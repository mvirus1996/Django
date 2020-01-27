Requirements:-
1) Django
2) MySQL server
3) create "imp.json" file in "tables/djangotable/static" folder with the database details:-
      {
        "database_name": "<database_name>",
        "database_username": "<database_username>",
        "database_password": "<database_password>",
        "database_host": "<host_name>",
        "database_port": <port_number>
      }
      

Commands to execute:-
1) cd "<additional_path>/tables/djangotable
2) python manage.py migrate
3) python manage.py runserver
