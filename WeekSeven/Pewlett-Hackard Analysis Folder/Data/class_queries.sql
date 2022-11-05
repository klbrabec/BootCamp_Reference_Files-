--Drop table if exists
DROP TABLE people;

-- Create a new table
CREATE TABLE people (
  name VARCHAR(30) NOT NULL,
  has_pet BOOLEAN DEFAULT false,
  pet_type VARCHAR(10) NOT NULL,
  pet_name VARCHAR(30),
  pet_age INT
);

--You cannot re-run code that creates objects within a database.  (unlike code that is being written un Python)
-- Best practice for you to write commands in ALL CAPS. (This may be different if the organization has a style guide in place)
-- ; ends the SQL statement that you're making.  It will still run without it - but again - this is best practice that lets others
-- know that you're done with what you're doing. 
-- varchar - this is a string - numbers and characters together. () limits the length of your fields. 
-- Common practies to limit the length of your fields 
-- better design, better security. 
-- it's important to know and understand what limitations you're putting on your data and what you're collecting/working with. 



-- Query all fields from the table
SELECT *
FROM people;

-- what do we want to select and where do we want to select it from?
-- SQL does not run from top to bottom - you have to know where your'e getting data from. 
-- SQL ORDER OF OPERATIONS 

-- Insert data into the table
INSERT INTO people (name, has_pet, pet_type, pet_name, pet_age)
VALUES ('Jacob', true, 'dog', 'Misty', 10),
  ('Ahmed', true, 'rock', 'Rockington', 100),
  ('Peter', true, 'cat', 'Franklin', 2),
  ('Dave', true, 'dog', 'Queso', 1), 
  ('Charles', true, 'dog', 'Logan', 1);
  
--you can run these without every column populated - ex name/type are not null/required - but all of the others are optional. 

-- Query only the `pet_name` field
SELECT pet_name
FROM people;

-- Filter the query to show only dogs under the age of 5
SELECT pet_type, pet_name
FROM people
WHERE pet_type = 'dog'
AND pet_age < 5;

--strings in SQL need to have single quotes surrounding them - not double quotes like in Python 


-- Drop table if exists
DROP TABLE cities;

-- Create a new table
CREATE TABLE cities (
  id SERIAL PRIMARY KEY,
  city VARCHAR(30) NOT NULL,
  state VARCHAR(30) NOT NULL,
  population INT
);

--serial Primary key will create PKs automatically - starting at the number 1 and will increment for reach record. 
-- Can be a varchar, can be an integer - but it will always be unique. 

-- Insert data into the table
INSERT INTO cities (city, state, population)
VALUES ('Alameda', 'California', 79177),
  ('Mesa', 'Arizona', 496401),
  ('Boerne', 'Texas', 16056),
  ('Boerne', 'Texas', 16056),
  ('Anaheim', 'Texas', 352497),
  ('Tucson', 'Arizona', 535677),
  ('Garland', 'Texas', 238002);

-- View the table data
SELECT *
FROM cities;

-- Use a query to view only the cities
SELECT city
FROM cities;

-- Create a query to view cities in Texas
SELECT city, state
FROM cities
WHERE state = 'Texas';

-- Create a query to view cities and states
-- with a population less than 100,000
SELECT *
FROM cities
WHERE population < 100000;

-- Create a query to view the city in California
-- with a population of less than 100,000
SELECT *
FROM cities
WHERE population < 100000
AND state = 'California';

--  Create a query to update the state for the city of Anaheim.
UPDATE cities
SET state = 'California'
WHERE city = 'Anaheim';

-- Create a query to removed the duplicate "('Boerne', 'Texas', 16056)" by id=4.
DELETE FROM cities
WHERE id = 4;

--When you delete a primary key it is 'dead' - it will not be re-used in this particular table. 
