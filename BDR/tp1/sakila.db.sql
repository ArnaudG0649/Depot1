/*
SELECT *
FROM film 
ORDER BY release_year DESC, title asc
*/

/*
SELECT *
FROM actor 
WHERE last_name = 'JACKMAN'
*/

/*
SELECT * 
From category
*/

/*
SELECT last_name ,COUNT(*) 
From actor
GROUP BY last_name
*/

/*
SELECT * 
FROM category
*/

/*
SELECT 
  avg(rental_duration) AS moyenne, 
  min(rental_duration) AS min, 
  max(rental_duration) AS max
FROM film
*/

/*
SELECT release_year ,Count(*) 
FROM film
GROUP BY release_year
*/

/*
SELECT timediff(return_date,rental_date)
FROM rental
*/

--9
/*
SELECT F.film_id, F.title, F.language_id, L.name
FROM film F, language L
WHERE F.language_id = L.language_id 
*/ 

--Requêtes imbriquées
/*
SELECT title 
FROM
(
    SELECT F.film_id, F.title, F.language_id, L.name
    FROM film F, language L
    WHERE F.language_id = L.language_id 
)
WHERE film_id=73 
*/

--AM (meilleure)
/*
SELECT *
FROM film
WHERE language_id IN (
  SELECt language_id
  FROM language
  where name='English' OR name='Japanese'
)
*/




