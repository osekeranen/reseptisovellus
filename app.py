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
    result = db.session.execute("SELECT name FROM recipes WHERE id="+str(id))
    name = result.fetchone()[0]
    result = db.session.execute("SELECT recipes.id, recipes_steps.step, recipes_steps.description, steps_ingredients.amount, measurements.abbreviation, ingredients.partitive FROM recipes LEFT JOIN recipes_steps ON recipes.id = recipes_steps.recipe_id LEFT JOIN steps_ingredients ON recipes_steps.id = steps_ingredients.step_id LEFT JOIN measurements ON steps_ingredients.measurement_id = measurements.id LEFT JOIN ingredients ON steps_ingredients.ingredient_id = ingredients.id WHERE recipes.id="+str(id))
    ingredients = result.fetchall()
    result = db.session.execute("SELECT recipes.id, recipes_steps.step, recipes_steps.description, recipes_substeps.step, recipes_substeps.description FROM recipes LEFT JOIN recipes_steps ON recipes.id = recipes_steps.recipe_id LEFT JOIN recipes_substeps ON recipes_steps.id = recipes_substeps.step_id WHERE recipes.id="+str(id))
    steps = result.fetchall()
    return render_template("recipe.html", name=name, ingredients=ingredients, steps=steps)
