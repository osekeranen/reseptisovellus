CREATE TABLE recipes (
    id SERIAL PRIMARY KEY,
    name TEXT
);

CREATE TABLE recipes_steps (
    id SERIAL PRIMARY KEY,
    recipe_id INTEGER REFERENCES recipes ON DELETE CASCADE,
    step INTEGER,
    description TEXT
);

CREATE TABLE ingredients (
    id SERIAL PRIMARY KEY,
    name TEXT,
    partitive TEXT
);

CREATE TABLE measurements (
    id SERIAL PRIMARY KEY,
    name TEXT,
    abbreviation TEXT
);

CREATE TABLE recipes_ingredients (
    id SERIAL PRIMARY KEY,
    recipe_id INTEGER REFERENCES recipes ON DELETE CASCADE,
    ingredient_id INTEGER REFERENCES ingredients,
    measurement_id INTEGER REFERENCES measurements,
    amount REAL
);