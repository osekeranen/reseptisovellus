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

INSERT INTO measurements (name, abbreviation)
SELECT 'maustemitta', 'mm'
WHERE NOT EXISTS (SELECT 1 FROM measurements WHERE name='maustemitta');

INSERT INTO measurements (name, abbreviation)
SELECT 'teelusikka', 'tl'
WHERE NOT EXISTS (SELECT 1 FROM measurements WHERE name='teelusikka');

INSERT INTO measurements (name, abbreviation)
SELECT 'ruokalusikka', 'rkl'
WHERE NOT EXISTS (SELECT 1 FROM measurements WHERE name='ruokalusikka');

INSERT INTO measurements (name, abbreviation)
SELECT 'desilitra', 'dl'
WHERE NOT EXISTS (SELECT 1 FROM measurements WHERE name='desilitra');

INSERT INTO measurements (name, abbreviation)
SELECT 'litra', 'l'
WHERE NOT EXISTS (SELECT 1 FROM measurements WHERE name='litra');

INSERT INTO measurements (name, abbreviation)
SELECT 'gramma', 'g'
WHERE NOT EXISTS (SELECT 1 FROM measurements WHERE name='gramma');

INSERT INTO measurements (name, abbreviation)
SELECT 'kilogramma', 'kg'
WHERE NOT EXISTS (SELECT 1 FROM measurements WHERE name='kilogramma');

INSERT INTO measurements (name, abbreviation)
SELECT 'pussi', 'pss'
WHERE NOT EXISTS (SELECT 1 FROM measurements WHERE name='pussi');

INSERT INTO measurements (name, abbreviation)
SELECT 'purkki', 'prk'
WHERE NOT EXISTS (SELECT 1 FROM measurements WHERE name='purkki');

INSERT INTO measurements (name, abbreviation)
SELECT 'paketti', 'pkt'
WHERE NOT EXISTS (SELECT 1 FROM measurements WHERE name='paketti');

INSERT INTO measurements (name, abbreviation)
SELECT 'tölkki', 'tlk'
WHERE NOT EXISTS (SELECT 1 FROM measurements WHERE name='tölkki');

INSERT INTO measurements (name, abbreviation)
SELECT 'rasia', 'rs'
WHERE NOT EXISTS (SELECT 1 FROM measurements WHERE name='rasia');

CREATE TABLE steps_ingredients (
    id SERIAL PRIMARY KEY,
    step_id INTEGER REFERENCES recipes_steps ON DELETE CASCADE,
    ingredient_id INTEGER REFERENCES ingredients,
    measurement_id INTEGER REFERENCES measurements,
    amount REAL
);