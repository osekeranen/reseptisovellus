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