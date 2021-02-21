from app import app
from db import db
from flask import render_template, request, redirect

@app.route("/")
def index():
    result = db.session.execute("SELECT COUNT(*) FROM recipes")
    count = result.fetchone()[0]
    result = db.session.execute("SELECT * FROM recipes")
    recipes = result.fetchall()
    return render_template("index.html", count=count, recipes=recipes)

@app.route("/resepti/<int:id>")
def recipe(id):
    result = db.session.execute("SELECT name FROM recipes WHERE id="+str(id))
    name = result.fetchone()[0]
    result = db.session.execute("SELECT recipes.id, recipes_steps.step, recipes_steps.description, steps_ingredients.amount, measurements.abbreviation, ingredients.partitive FROM recipes LEFT JOIN recipes_steps ON recipes.id = recipes_steps.recipe_id LEFT JOIN steps_ingredients ON recipes_steps.id = steps_ingredients.step_id LEFT JOIN measurements ON steps_ingredients.measurement_id = measurements.id LEFT JOIN ingredients ON steps_ingredients.ingredient_id = ingredients.id WHERE recipes.id="+str(id))
    ingredients = result.fetchall()
    result = db.session.execute("SELECT recipes.id, recipes_steps.step, recipes_steps.description, recipes_substeps.step, recipes_substeps.description FROM recipes LEFT JOIN recipes_steps ON recipes.id = recipes_steps.recipe_id LEFT JOIN recipes_substeps ON recipes_steps.id = recipes_substeps.step_id WHERE recipes.id="+str(id))
    steps = result.fetchall()
    return render_template("recipe.html", name=name, ingredients=ingredients, steps=steps)

@app.route("/uusi/resepti")
def new_recipe():
    return render_template("new_recipe.html")

@app.route("/uusi/ainesosa")
def new_ingredient():
    return render_template("new_ingredient.html")

@app.route("/uusi/ainesosa/lisaa", methods=["POST"])
def create_ingredient():
    ingredient = request.form["ingredient"]
    partitive = request.form["partitive"]
    sql = "INSERT INTO ingredients (name, partitive) SELECT '" + ingredient + "', '" + partitive + "' WHERE NOT EXISTS (SELECT 1 FROM ingredients WHERE name='" + ingredient + "')"
    db.session.execute(sql)
    db.session.commit()
    return redirect("/uusi/ainesosa/lisatty")

@app.route("/uusi/ainesosa/lisatty")
def new_ingredient_result():
    return render_template("ingredient_result.html")

@app.route("/ainesosat.csv")
def get_ingredients():
    result = db.session.execute("SELECT name, partitive FROM ingredients")
    measurements = result.fetchall()
    return render_template("csv.html", title="ainesosat", list=measurements)

@app.route("/mitat.csv")
def get_measurements():
    result = db.session.execute("SELECT name, abbreviation FROM measurements")
    measurements = result.fetchall()
    return render_template("csv.html", title="mitat", list=measurements)