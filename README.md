# API-Rest
A quick introduction to create a REST API using Python


## Installation
In order to create an REST API, you need to download Python 2.7+ or 3.4+ at least.
Then, you will need different packages
  - Flask
  - PyMySQL
  - python-dotenv

After this, navigate to your project using the command prompt and enter the following commands:

```bash
pip install flask
pip install PyMySQL
pip install python-dotenv
```

## API
When the installation is done, create the main file. We will call it ```app.py``` then open this file on your favorite IDE.

First, we will import the different libraries
```python
# Librairies
from flask import Flask, jsonify
import pymysql
from dotenv import load_dotenv, find_dotenv
import os
```

Then we will initialize the variables

```python
# Variables
load_dotenv(find_dotenv())
app = Flask(__name__)
app.config['DEBUG'] = True
app.env = "dev"
```

After this, we will connect our app to the database. In order to do this, you need to create a ```.env```file.
This file should look like this: 
```env
DB_HOST=your_host
DB_USER=your_user
DB_PASS=your_password
DB_NAME=your_database
```

Now that we have the ```.env```file, we can connect our app to the database. To do so, we are going to create a function that return the connection.
```python
# connection à la base de données
def connection():
	return pymysql.connect(host = os.getenv("DB_HOST"),
		user = os.getenv("DB_USER"),
		password = os.getenv("DB_PASS"),
		db = os.getenv("DB_NAME"),
		charset = "utf8mb4",
		cursorclass = pymysql.cursors.DictCursor)
```

We can now create the routes for our REST API.
```python
# Routes disponibles
@app.route("/", methods=["GET"])
def home():
	con = connection()
	with con:
		cur = con.cursor()
		sql = 'SELECT * from users'
		cur.execute(sql,())
		result = cur.fetchall()
		return jsonify(result), 200
```

Last but not least, we can run our app using those lines :
```python
# Lancement de l'application
if __name__ == "__main__":
	app.run()
```

Finally, to run our app as a REST API, you can just enter the following command on yotu command prompt :
```bash
app.py
```

If you we take a look at our database, we should have something like this:
| id | nom       | prenom  | email                   |
|:--:|-----------|---------|-------------------------|
| 1  | Dupont    | Michel  | dupont.michel@gmail.com |
| 2  | Frontino  | Alexis  | alexis.f@gmail.com      |
| 3  | Chalifour | Mathieu | challifourm@gmail.com   |

Then if you run you app and check the following url : ```http://localhost:5000/``` you qill see this :

```json
[
  {
    "email": "dupont.michel@gmail.com",
    "id": 1,
    "nom": "Dupont",
    "prenom": "Michel"
  },
  {
    "email": "alexis.f@gmail.com",
    "id": 2,
    "nom": "Frontino",
    "prenom": "Alexis"
  },
  {
    "email": "chalifourm@gmail.com",
    "id": 3,
    "nom": "Chalifour",
    "prenom": "Mathieu"
  }
]
```




