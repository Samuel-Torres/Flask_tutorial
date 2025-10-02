Step 1: Creat Virtual Environment File .venv


Step 2: Activate the environment:
. .venv/bin/activate

Step 3:

Run installation command:
pip install Flask


Running Flask:
flask --app {name of root directory here: in this project main.py so have to run: main here} run
ex: flask --app main run 
optional = --debug
Add --debug to enable with debugger. 

If you have the debugger disabled or trust the users on your network, you can make the server publicly available simply by adding --host=0.0.0.0 to the command line:

from pythonflask root directory:
from flaskProject.endpoints.users.users import users

$ flask run --host=0.0.0.0
This tells your operating system to listen on all public IPs.

% Run with auto reload abilities
flask --app flaskProject/app run --reload