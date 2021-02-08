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

CREATE TABLE recipes_substeps (
    id SERIAL PRIMARY KEY,
    step_id INTEGER,
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

CREATE TABLE steps_ingredients (
    id SERIAL PRIMARY KEY,
    step_id INTEGER REFERENCES recipes_steps ON DELETE CASCADE,
    ingredient_id INTEGER REFERENCES ingredients,
    measurement_id INTEGER REFERENCES measurements,
    amount REAL
);