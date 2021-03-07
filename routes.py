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

@app.route("/haku")
def query():
    query = request.args["query"]
    sql = "SELECT * FROM recipes WHERE name ILIKE :query"
    result = db.session.execute(sql, {"query":"%"+query+"%"})
    recipes = result.fetchall()
    return render_template("result.html", recipes=recipes)

@app.route("/resepti/<int:id>")
def recipe(id):
    result = db.session.execute("SELECT name FROM recipes WHERE id="+str(id))
    name = result.fetchone()[0]
    result = db.session.execute("SELECT recipes.id, recipes_ingredients.amount, measurements.abbreviation, ingredients.partitive FROM recipes LEFT JOIN recipes_ingredients ON recipes.id = recipes_ingredients.recipe_id LEFT JOIN measurements ON recipes_ingredients.measurement_id = measurements.id LEFT JOIN ingredients ON recipes_ingredients.ingredient_id = ingredients.id WHERE recipes.id="+str(id))
    ingredients = result.fetchall()
    result = db.session.execute("SELECT recipes.id, recipes_steps.step, recipes_steps.description FROM recipes LEFT JOIN recipes_steps ON recipes.id = recipes_steps.recipe_id WHERE recipes.id="+str(id))
    steps = result.fetchall()
    return render_template("recipe.html", name=name, ingredients=ingredients, steps=steps)

@app.route("/uusi/resepti")
def new_recipe():
    return render_template("new_recipe.html")

@app.route("/uusi/resepti/lisaa", methods=["POST"])
def create_recipe():
    name = request.form["name"]
    sql = "INSERT INTO recipes (name) VALUES (:name) RETURNING id"
    result = db.session.execute(sql, {"name":name})
    recipe_id = result.fetchone()[0]
    ingredients = request.form.getlist("ingredient")
    for string in ingredients:
        if string != "":
            amount = string.split()[0]
            measurement = string.split()[1]
            result = db.session.execute("SELECT id FROM measurements WHERE abbreviation='" + measurement + "'")
            measurement_id = result.fetchone()[0]
            ingredient = string.split()[2]
            result = db.session.execute("SELECT id FROM ingredients WHERE partitive='" + ingredient + "'")
            ingredient_id = result.fetchone()[0]
            sql = "INSERT INTO recipes_ingredients (recipe_id, ingredient_id, measurement_id, amount) VALUES (" + str(recipe_id) + ", " + str(ingredient_id) + ", " + str(measurement_id) + ", " + str(amount) + ")"
            db.session.execute(sql)
    steps = request.form.getlist("step")
    i = 1
    for string in steps:
        if string != "":
            sql = "INSERT INTO recipes_steps (recipe_id, description, step) VALUES (" + str(recipe_id) + ", '" + string + "', " + str(i) + ")"
            db.session.execute(sql)
            i += 1
    db.session.commit()
    return redirect("/")

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
    return redirect("/")

@app.route("/ainesosat.csv")
def get_ingredients():
    result = db.session.execute("SELECT name, partitive FROM ingredients")
    measurements = result.fetchall()
    return render_template("csv.html", title="ainesosat", list=measurements)

@app.route("/mittayksikot.csv")
def get_measurements():
    result = db.session.execute("SELECT name, abbreviation FROM measurements")
    measurements = result.fetchall()
    return render_template("csv.html", title="mitat", list=measurements)