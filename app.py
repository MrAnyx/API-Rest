
# Librairies
from flask import Flask, jsonify
import pymysql
from dotenv import load_dotenv, find_dotenv
import os


# Variables
load_dotenv(find_dotenv())
appqhsklhfjksdhlfkjhqdlksjfhlqksjdhflkjqsdhfjkqdhlkfjqhldjsfldjshfljkqsfhlkqlqjhdjqhfh = Flask(__name__)
app.config['DEBUG'] = True
app.env = "dev"




# connection à la base de données
def connection():
	return pymysql.connect(host = os.getenv("DB_HOST"),
		user = os.getenv("DB_USER"),
		password = os.getenv("DB_PASS"),
		db = os.getenv("DB_NAME"),
		charset = "utf8mb4",
		cursorclass = pymysql.cursors.DictCursor)



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



# Lancement de l'application
if __name__ == "__main__":
	app.run()
