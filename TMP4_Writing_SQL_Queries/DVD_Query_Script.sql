USE sakila;

#Single Table Queries
# 1) Getting a list of all film titles alphabetized by title.
SELECT title 
FROM film
ORDER BY title ASC;

# 2) Finding the description, release year, length, and rating for the movie “KENTUCKIAN GIANT”.
SELECT description, release_year, length, rating 
FROM film
WHERE title = "KENTUCKIAN GIANT";

# 3) Find the first last name of each employee.
SELECT last_name, first_name 
FROM staff;

# 4) Repeating the query above, but this time, but concatenating the results into one column 
#    with the format last name, first name and the output column being named “name”.
SELECT CONCAT(first_name, ' ', last_name) AS name 
FROM staff;

# 5) Get the number of customers, with the column being named “num_customers”
SELECT COUNT(customer_id) AS num_customers 
FROM customer;

# 6) Get the number of customers who are active vs inactive in the system.
SELECT active AS customer_activity, COUNT(customer_id) AS numb_customers 
FROM customer
GROUP BY active;

# 7) Get the average amount a customer spends on a rental.
SELECT customer_id, ROUND(AVG(amount), 2) AS avg_rental_amount
FROM payment
GROUP BY customer_id;

# 8) Get maximum amount any customer has spent on a rental.
SELECT customer_id, MAX(amount) AS max_rental_amount
FROM payment
GROUP BY customer_id;

# 9) Get a list of the actors. The results should include only one column with the format last name, first name. 
# The column should be named “actor_name” The results should be sorted be sorted alphabetically by the last name (ascending).
SELECT CONCAT(last_name, ", ", first_name) AS actor_name
FROM actor
ORDER BY actor_name ASC;

# 10) Repeat this query above, but the results should be in reverse order.
SELECT CONCAT(last_name, ", ", first_name) AS actor_name
FROM actor
ORDER BY actor_name DESC;

# 11) Repeat the query again, this time get only actors whose last names start with ‘M’ or ‘V’. 
# Order the results alphabetically by last name (ascending).
SELECT CONCAT(last_name, ", ", first_name) AS actor_name
FROM actor
WHERE last_name LIKE 'M%' OR last_name LIKE 'V%'
ORDER BY actor_name ASC;

# 12) Repeat the query again, this time get only actors whose last names start with leters between ‘M’ and ‘V’ inclusive. 
# Order the results alphabetically by last name (ascending).
SELECT CONCAT(last_name, ", ", first_name) AS actor_name
FROM actor
WHERE last_name BETWEEN 'M%' AND 'W%'
ORDER BY actor_name ASC;

# 13) Get a list of each customer ID and the number of rentals they have in their history. Name this column Number of Rentals.
SELECT customer_id, COUNT(rental_id) AS "Number of Rentals"
FROM rental
GROUP BY customer_id;


# Mult-table Queries
# [1] Get a list of category names and a count of movies that fall into that category.  
#     Name the category column “category” the count column “num_films”
#     Order the results alphabetically (ascending). Use the WHERE clause to join the tables.
SELECT category.name AS category, COUNT(film_id) AS num_films
FROM category, film_category
WHERE film_category.category_id = category.category_id
GROUP BY category.name
ORDER BY category.name ASC;

# [2] Repeat the query above using a JOIN clause instead of the WHERE clause.
SELECT category.name as category, COUNT(DISTINCT film_id) AS num_films
FROM category
JOIN film_category ON film_category.category_id = category.category_id
GROUP BY category.name
ORDER BY category.name ASC;

# [3] Get a list of country names and a count of the cities that are in that country. 
# 	  Name the count column “num_cities”. Order the results alphabetically (ascending). 
#     Use the WHERE clause to join the tables.
SELECT country.country, COUNT(city.city_id) AS num_cities
FROM country, city
WHERE country.country_id = city.country_id
GROUP BY country.country_id
ORDER BY country ASC;


# [4] Repeat the query above using a JOIN clause instead of the WHERE clause.
SELECT country.country, COUNT(city.city_id) AS num_cities
FROM country
JOIN city ON country.country_id = city.country_id
GROUP BY country.country_id
ORDER BY country ASC;

# [5] Get a list of each customer’s last name and first name and the number of rentals they have.
#     Name the count column “num_rentals”. Order the result by the number of rentals in descending order. 
#     The highest number of rentals should be at the top. 
#     Sort any ties (same number of rentals) by last name (ascending). Use the WHERE clause to join the tables.
SELECT CONCAT(customer.last_name, ", ", customer.first_name) AS customer_name, COUNT(DISTINCT rental.rental_id) AS num_rentals
FROM customer, rental
WHERE customer.customer_id = rental.customer_id
GROUP BY customer.customer_id
ORDER BY COUNT(rental_id) DESC, customer.last_name ASC;

# [6] Repeat the query above using a JOIN clause instead of the WHERE clause.
SELECT CONCAT(customer.last_name, ", ", customer.first_name) AS customer_name, COUNT(DISTINCT rental.rental_id) AS num_rentals
FROM customer
JOIN rental ON customer.customer_id = rental.customer_id
GROUP BY customer.customer_id
ORDER BY COUNT(rental_id) DESC, customer.last_name ASC;


# [7] Get a list of each customer’s last name and first name and the amount of money they have spent on rentals. 
#     Name the sum column “total_spent”. Order the result by the amount in descending order. 
#     The highest amount of money spent should be at the top. 
#     Sort any ties (amount of money spent) by last name (ascending). Use the JOIN clause for this query.
SELECT CONCAT(customer.last_name, ", ", customer.first_name) AS customer_name, SUM(payment.amount) AS total_spent
FROM customer
JOIN payment ON customer.customer_id = payment.customer_id
GROUP BY customer.customer_id
ORDER BY total_spent DESC, customer.last_name ASC;

# [8] Get the number of actors in each film. 
#     Order the results (ascending) by the film title and name the column with the actor count “num_actors”.
SELECT film.title AS film_title, COUNT(film_actor.actor_id) AS num_actors
FROM film
JOIN film_actor ON film.film_id = film_actor.film_id
GROUP BY film_actor.film_id
ORDER BY film_title ASC;

# [9] Get the number of films each manager holds. 
#     Use only the manager staﬀ id to identify the manager. Name the column with the number of films “num_films”
SELECT store.manager_staff_id, COUNT(inventory.film_id) AS num_films
FROM store
JOIN inventory on inventory.store_id = store.store_id
GROUP BY store.manager_staff_id;

# [10]  Get the number of customers per manager. Use only the manager staﬀ id to identify the manager. 
#       Name the column with the number of films “num_customers”. Order by store id (ascending).
SELECT store.manager_staff_id, COUNT(customer.customer_id) AS num_customer
FROM store
JOIN customer on customer.store_id = store.store_id
GROUP BY store.manager_staff_id
ORDER BY store.store_id ASC;

# [11]  Get the title and film category of each film. Order the results by category name. 
#       Rename the “name” column so it says “category”. 
#       This query will involve joining three tables using the JOIN syntax.
SELECT title, category.name AS category
FROM film
JOIN film_category ON film.film_id = film_category.film_id
JOIN category ON film_category.category_id = category.category_id
ORDER BY category ASC, title ASC;

# [12] Get a list of each customer’s first and last name (individually, not concatenated) and their full address including city and country. 
#      Order the results by the customer’s last name. This will involve joining four tables using the JOIN syntax.
SELECT customer.first_name AS "Customer First Name", customer.last_name AS "Customer Last Name", CONCAT(address.address, ", ", city.city, ", ", country.country) AS Address
FROM customer
JOIN address ON address.address_id = customer.address_id
JOIN city ON city.city_id = address.city_id
JOIN country ON country.country_id = city.country_id
ORDER BY customer.last_name;


# [13] Repeat the query above except this time include only inactive customers from China.
SELECT customer.last_name AS "Customer Last Name", customer.first_name AS "Customer First Name", CONCAT(address.address, ", ", city.city, ", ", country.country) as "Customer Address"
FROM customer
JOIN address ON address.address_id = customer.address_id
JOIN city ON city.city_id = address.city_id
JOIN country ON country.country_id = city.country_id
WHERE country.country = "China" AND customer.active = 0
ORDER BY customer.last_name;

# [14] Get a list of the titles of every film each customer has rented. 
#      Order the results by customer last name (ascending) and title (ascending).
SELECT customer.last_name as customer_last_name, GROUP_CONCAT(film.title ORDER BY film.title ASC) AS film_list
FROM customer
JOIN rental ON customer.customer_id = rental.customer_id
JOIN inventory ON rental.inventory_id = inventory.inventory_id
JOIN film ON inventory.film_id = film.film_id
GROUP BY customer.customer_id
ORDER BY customer.last_name ASC;


# [15] Repeat the query above, but this time, include the category of each title in the results. 
#      Name the category column “category”. Order the results by the same columns (name and title)
SELECT customer.last_name AS customer_last_name, GROUP_CONCAT(film.title ORDER BY film.title) AS film_list, GROUP_CONCAT(category.name) as category
FROM customer
JOIN rental ON customer.customer_id = rental.customer_id
JOIN inventory ON rental.inventory_id = inventory.inventory_id
JOIN film ON inventory.film_id = film.film_id
JOIN film_category ON film.film_id = film_category.film_id
JOIN category ON film_category.category_id = category.category_id
GROUP By customer.customer_id
ORDER BY customer_last_name ASC;

# [16] Get a list of each customer that includes their first and last name, the number of rentals (num_rentals) they have had 
#      and the total amount (total_spent) of money they have spent on rentals. Order the results by last name (ascending)
SELECT customer.first_name, customer.last_name, COUNT(DISTINCT rental.rental_id) AS num_rentals, SUM(payment.amount) AS total_spent
FROM customer
JOIN rental ON rental.customer_id = customer.customer_id
JOIN payment ON payment.customer_id = rental.customer_id
GROUP BY customer.customer_id
ORDER BY customer.last_name ASC;

# [17] Repeat the query above, but this time add the customer’s country to the output. 
#      The order of the columns should be last_name, first_name, country, num_rentals, total_spent. 
#      Order rows by last name (ascending)
SELECT customer.last_name, customer.first_name, country.country, COUNT(DISTINCT rental.rental_id) AS num_rentals, SUM(payment.amount) AS total_spent
FROM customer
JOIN rental ON rental.customer_id = customer.customer_id
JOIN payment ON payment.customer_id = rental.customer_id
JOIN address ON address.address_id = customer.address_id
JOIN city ON city.city_id = address.city_id
JOIN country ON country.country_id = city.country_id
GROUP BY customer.customer_id
ORDER BY customer.last_name ASC;