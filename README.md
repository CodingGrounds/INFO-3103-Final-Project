# INFO-3103-Final-Project

To get running with the database:
- Install MySQL https://dev.mysql.com/doc/mysql-getting-started/en/#mysql-getting-started-installing
- Set up a user and a database for the project https://www.a2hosting.ca/kb/developer-corner/mysql/managing-mysql-databases-and-users-from-the-command-line
- Edit `src/rickbox/database/app_config.py` and update the values to match your db configuration.
- Activate the Python virtual environment: `source venv/bin/activate`
- Navigate to the `rickbox` folder: `cd src/rickbox`
- Run the Flask development server *from within the rickbox folder*: `python app.py`
