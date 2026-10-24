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


/* Oppgave 4 */

   /* Deloppgave 1 */
    /*  Registrer en ny kunde */
insert into customers (first_name, last_name, email, city, registered_date) values
    ('Henrik', 'Solberg', 'henrik.solberg@example.com' , 'Lillehammer', '2026-10-24')

select * from customers
where email = 'henrik.solberg@example.com'

   /* Deloppgave 2 */
    /*  Registrer flere produkter */

insert into products (product_name, category, price, stock) values
                        ('USB-C cable', 'Accessories', 199.00, 50),
                        ('Docking station', 'Accessories', 1899.00, 12),
                        ('External SSD 2TB', 'Storage', 1999.00, 8)

select * from products
where product_name IN ('USB-C cable', 'Docking station', 'External SSD 2TB')


   /* Deloppgave 2 */
    /*  Registrer flere produkter */

insert into products (product_name, category, price, stock) values
                        ('USB-C cable', 'Accessories', 199.00, 50),
                        ('Docking station', 'Accessories', 1899.00, 12),
                        ('External SSD 2TB', 'Storage', 1999.00, 8)

select * from products
where product_name IN ('USB-C cable', 'Docking station', 'External SSD 2TB')


   /* Deloppgave 3 */
    /*  Registrer nye bestillinger */

insert into orders (customer_id, product_id, quantity, order_date, stats)
values (
        (select customer_id from customers where email = 'henrik.solberg@example.com'),
        (select product_id from products where product_name = 'Docking station'),
        1,   CURRENT_DATE, 'ordered'),
        (
         (select customer_id from customers where email = 'henrik.solberg@example.com'),
         (select product_id from products where product_name = 'USB-C cable'),
         2,   CURRENT_DATE, 'ordered'),
       (
           (select customer_id from customers where email = 'henrik.solberg@example.com'),
           (select product_id from products where product_name = 'External SSD 2TB'),
           1,   CURRENT_DATE, 'ordered');

SELECT
    c.first_name,
    c.last_name,
    p.product_name,
    o.quantity,
    o.order_date,
    o.stats
FROM orders AS o
         JOIN customers AS c
              ON o.customer_id = c.customer_id
         JOIN products AS p
              ON o.product_id = p.product_id
WHERE c.email = 'henrik.solberg@example.com';

   /* Deloppgave 4 */
    /*  Prisendring */

SELECT * from products
where category = 'Accessories';

update products
set price = price * 1.08
where category = 'Accessories';


SELECT * from products
where category = 'Accessories';

   /* Deloppgave 5 */
    /*  Lagerpåfylling */

SELECT * from products
where stock < 15;

update products
set stock = stock + 20
where stock < 15;

    /*  Tok en manuell sjekk for å se at de ble økt. Tok bare ut product_name jeg fant i første spøøring */
SELECT *
FROM products
WHERE product_name IN (
                       'Laptop Pro 15',
                       '27-inch monitor',
                      'Bluetooth speaker',
                      'Docking station',
                      'External SSD 2TB'
    );

   /* Deloppgave 6 */
    /*  Endre flere verdier */

select * from products
where product_name = 'Gaming headset';

update products
set price = price * 1.15,
    stock = stock + 10
where product_name = 'Gaming headset';

select * from products
where product_name = 'Gaming headset';

   /* Deloppgave 7 */
    /*  Oppdater ordrestatus */

select * from orders
where stats = 'Shipped' and order_date  < '2025-08-10';

update orders
set stats = 'Delivered'
where stats = 'Shipped' and order_date  < '2025-08-10';

select * from orders
where stats = 'Delivered' and order_date  < '2025-08-10';

   /* Deloppgave 8 */
    /*  Opprett og slett testdata */

/* Oppretter test data. Kunde og produkt først, så ordre. Da kunde og produkt er fremmednøkler i ordre*/
insert into customers (first_name, last_name, email, city, registered_date) values
                        ('Test', 'Name', 'test.name@test.no', 'TestCity', current_date );

insert into products (product_name, category, price, stock) VALUES
                        ('Testproduct', 'Testing', 999.99, 99);

insert into orders (customer_id, product_id, quantity, order_date, stats) VALUES
                    ((select customer_id from customers where email = 'test.name@test.no'),
                     (select product_id from products where product_name = 'Testproduct'),
                     1, current_date, 'Shipped'
                    );

/* Sjekker at kunden, produkt og ordre eksisterer*/
SELECT
    c.first_name,
    c.last_name,
    c.email,
    p.product_name,
    o.quantity,
    o.order_date,
    o.stats
FROM orders AS o
         JOIN customers AS c
              ON o.customer_id = c.customer_id
         JOIN products AS p
              ON o.product_id = p.product_id
WHERE c.email = 'test.name@test.no'
  AND p.product_name = 'Testproduct';



/* Sletter først ordre, så produkt og kunden av samme grunn som når jeg opprettet disse.*/
delete from orders
where customer_id = (select customer_id from customers where email = 'test.name@test.no');

delete from products
where product_name = 'Testproduct';

delete from customers
where email = 'test.name@test.no';


/* Sjekker at alt er slettet.*/
SELECT *
FROM customers
WHERE email = 'test.name@test.no';

SELECT *
FROM products
WHERE product_name = 'Testproduct';

SELECT *
FROM orders
WHERE customer_id IN (
    SELECT customer_id
    FROM customers
    WHERE email = 'test.name@test.no'
);



   /* Deloppgave 9 */
    /*  Bruk en transaksjon */

/* Legger inn bestilling og trekker fra på lagerhold */
BEGIN;

insert into orders (customer_id, product_id, quantity, order_date, stats) VALUES
                    (1, 1, 1, current_date, 'Delivered');
update products
set stock = stock - 1
where product_id = 1;

select * from products
where product_id = 1;



/* Sjekker lagerhold */
SELECT *
FROM products
WHERE product_id = 1;

/* Sjekker at den nye bestillingen ligger inne */
SELECT *
FROM orders
WHERE customer_id = 1
  AND product_id = 1
ORDER BY order_id DESC
LIMIT 1;

COMMIT;