from flask import Flask
from flask import redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy
from os import getenv

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
db = SQLAlchemy(app)

@app.route("/")
def index():
    result = db.session.execute("SELECT COUNT(*) FROM recipes")
    count = result.fetchone()[0]
    result = db.session.execute("SELECT * FROM recipes")
    recipes = result.fetchall()
    return render_template("index.html", count=count, recipes=recipes)

@app.route("/resepti/<int:id>")
def page(id):
    result = db.session.execute("SELECT name FROM recipes WHERE id='"+str(id)+"'")
    name = result.fetchone()[0]
    return render_template("recipe.html", name=name)
