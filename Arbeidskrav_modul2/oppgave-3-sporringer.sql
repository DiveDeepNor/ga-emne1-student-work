/* Oppgave 3 */

   /* Deloppgave 1 */
    /* Produktoversikt */
select * from products
         where price > 750 and stock  > 10
         order by price desc

   /* Deloppgave 2 */
    /* Kunder i utvalgte byer */
select * from customers
    where city IN ('Oslo', 'Bergen', 'Trondheim')
    order by city, last_name

   /* Deloppgave 3 */
    /* Bestillinger i en periode */
select order_id, order_date, quantity, stats from orders
    where order_date >= '2025-07-01' and order_date  < '2025-08-01'
    order by order_date;

   /* Deloppgave 4 */
    /* Full bestillingsoversikt */
SELECT
    o.order_id,
    c.first_name,
    c.last_name,
    p.product_name,
    o.quantity,
    p.price,
    o.order_date,
    o.status
FROM orders AS o
         JOIN customers AS c
              ON o.customer_id = c.customer_id
         JOIN products AS p
              ON o.product_id = p.product_id
ORDER BY o.order_date;

   /* Deloppgave 5 */
    /* Beregnet verdi */
SELECT
    o.order_id,
    c.first_name,
    c.last_name,
    p.product_name,
    o.quantity,
    p.price,
    o.order_date,
    o.status,
    p.price * o.quantity AS total_value
FROM orders AS o
         JOIN customers AS c
              ON o.customer_id = c.customer_id
         JOIN products AS p
              ON o.product_id = p.product_id
ORDER BY total_value DESC ;

   /* Deloppgave 6 */
    /* Bestillinger med høy verdi */
SELECT
    c.first_name,
    c.last_name,
    p.product_name,
    o.quantity,
    p.price,
    p.price * o.quantity AS total_value
FROM orders AS o
         JOIN customers AS c
              ON o.customer_id = c.customer_id
         JOIN products AS p
              ON o.product_id = p.product_id
WHERE p.price * o.quantity > 2000
ORDER BY total_value DESC;

   /* Deloppgave 7 */
    /* Bestillinger per status */
SELECT
    status,
    COUNT(*) AS number_of_orders
FROM orders
GROUP BY status
ORDER BY number_of_orders DESC;

   /* Deloppgave 8 */
    /* Gjennomsnittspris per kategori */
SELECT
    category,
    AVG(price) AS average_price
FROM products
GROUP BY category
ORDER BY average_price DESC;

   /* Deloppgave 9 */
    /* Bestillinger per kunde */
SELECT
    c.customer_id,
    c.first_name,
    c.last_name,
    COUNT(o.order_id) AS number_of_orders
FROM customers AS c
         LEFT JOIN orders AS o
                   ON c.customer_id = o.customer_id
GROUP BY
    c.customer_id,
    c.first_name,
    c.last_name
ORDER BY number_of_orders DESC;

   /* Deloppgave 10 */
    /* Antall solgte produkter */
SELECT
    p.product_id,
    p.product_name,
    COALESCE(SUM(o.quantity), 0) AS totalt_ordered_units
FROM products AS p
         LEFT JOIN orders AS o
                   ON p.product_id = o.product_id
GROUP BY
    p.product_id,
    p.product_name
ORDER BY totalt_ordered_units DESC;

   /* Deloppgave 11 */
    /* Beregnet verdi per produkt */
SELECT
    p.product_name,
    COALESCE(SUM(o.quantity), 0) AS totalt_ordered_units,
    COALESCE(SUM(o.quantity * p.price), 0) AS total_value
FROM products AS p
         LEFT JOIN orders AS o
                   ON p.product_id = o.product_id
GROUP BY
    p.product_id,
    p.product_name
ORDER BY total_value DESC;

   /* Deloppgave 12 */
    /* Kunder med flere bestillinger */
SELECT
    c.first_name,
    c.last_name,
    COUNT(o.order_id) AS number_of_orders
FROM customers AS c
         JOIN orders AS o
              ON c.customer_id = o.customer_id
GROUP BY
    c.customer_id,
    c.first_name,
    c.last_name
HAVING COUNT(o.order_id) > 1
ORDER BY number_of_orders DESC;

   /* Deloppgave 13 */
    /* Kunder uten bestillinger */
SELECT
    c.customer_id,
    c.first_name,
    c.last_name
FROM customers AS c
         LEFT JOIN orders AS o
                   ON c.customer_id = o.customer_id
WHERE o.order_id IS NULL;

   /* Deloppgave 14 */
    /* Produkter uten bestillinger */
SELECT
    p.product_id,
    p.product_name
FROM products AS p
         LEFT JOIN orders AS o
                   ON p.product_id = o.product_id
WHERE o.order_id IS NULL;


   /* Deloppgave 15 */
    /* Utforskingsoppgave */
SELECT
    c.customer_id,
    c.first_name,
    c.last_name,
    SUM(o.quantity * p.price) AS samlet_bestillingsverdi
FROM customers AS c
         JOIN orders AS o
              ON c.customer_id = o.customer_id
         JOIN products AS p
              ON o.product_id = p.product_id
GROUP BY
    c.customer_id,
    c.first_name,
    c.last_name
ORDER BY samlet_bestillingsverdi DESC
LIMIT 1;
    /* Forklaring:
       Fant ut at i MYSQL har man en funksjon som heter LIMIT 1.
       Brukte denne til å begrense til maks 1 rad etter at jeg hadde
       beregnet frem samlet bestillingsverdi på de ulike kundene*/

