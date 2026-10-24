/* Oppgave 1*/

   /* Lager første Databasen */

Create DATABASE if  not exists
    nettbutikk;

USE nettbutikk;


    /* Lager så customers tabell */

    Create TABLE customers (
    customer_id INT AUTO_INCREMENT NOT NULL,
    first_name varchar(50) NOT NULL,
    last_name varchar(50) NOT NULL,
    email varchar(100) NOT NULL,
    city varchar(50) NOT NULL,
    registered_date date NOT NULL,
    primary key (customer_id),
    unique (email)
)

    /* Lager så products tabell */

    Create TABLE products (
    product_id INT AUTO_INCREMENT NOT NULL,
    product_name varchar(100) NOT NULL,
    category varchar(50) NOT NULL,
    price decimal(10,2) NOT NULL,
    stock int NOT NULL,
    primary key (product_id)
)

    /* Lager så orders orders og knytter mot customer_id og product_id */
    Create TABLE orders (
    order_id INT AUTO_INCREMENT NOT NULL,
    customer_id int NOT NULL,
    product_id int NOT NULL,
    quantity int NOT NULL,
    order_date date NOT NULL,
    status varchar(20) NOT NULL,
    primary key (order_id),
    foreign key (customer_id) REFERENCES customers(customer_id),
    foreign key (product_id) REFERENCES products(product_id)
)

    /* Sjekker at alle kolonner er på plass i customers */
    SELECT *
    from customers;

    /* Sjekker at alle kolonner er på plass i products */
    SELECT *
    from products;

    /* Sjekker at alle kolonner er på plass i orders */
    SELECT *
    from orders;


/* Oppgave 2*/

    /* Legger inn products */
insert into products (product_name, category, price, stock) values
                        ('Laptop Pro 15', 'Computers', 12999.00, 8),
                        ('Wireless Mouse', 'Accessories', 399.00, 45),
                        ('Mechanical keyboard', 'Accessories', 899.00, 22),
                        ('27-inch monitor', 'Monitors', 3299.00, 14),
                        ('USB-C hub ', 'Accessories', 699.00, 30),
                        ('HD webcam', 'Accessories', 799.00 , 18),
                        ('Gaming headset', 'Audio', 1199.00 , 16),
                        ('Bluetooth speaker', 'Audio', 1499.00 , 12),
                        ('External SSD 1TB', 'Storage', 1099.00 , 25),
                        ('Laptop stand', 'Accessories', 549.00 , 35)

    /* Legger inn customers */
insert into customers (first_name, last_name, email, city, registered_date) values
                        ('Ola', 'Nordmann', 'ola.nordmann@example.com' , 'Oslo', '2025-01-15'),
                        ('Kari', 'Hansen', 'kari.hansen@example.com' , 'Bergen', '2025-02-03'),
                        ('Per', 'Johansen', 'per.johansen@example.com' , 'Trondheim', '2025-02-18'),
                        ('Anne', 'Larsen', 'anne.larsen@example.com' , 'Oslo', '2025-03-01'),
                        ('Thomas', 'Andersen', 'thomas.andersen@example.com' , 'Stavanger', '2025-03-12'),
                        ('Maria', 'Nilsen', 'maria.nilsen@example.com' , 'Kristiansand', '2025-04-05'),
                        ('Erik', 'Olsen', 'erik.olsen@example.com' , 'Bergen', '2025-04-21'),
                        ('Ingrid', 'Berg', 'ingrid.berg@example.com' , 'Tromsø', '2025-05-10')

    /* Legger inn orders */
insert into orders (customer_id, product_id, quantity, order_date, status) VALUES
                        (1, 1, 1, '2025-06-01', 'delivered'),
                        (1, 2, 2, '2025-06-01', 'delivered'),
                        (2, 4, 1, '2025-06-03', 'delivered'),
                        (3, 3, 1, '2025-06-05', 'delivered'),
                        (4, 5, 2, '2025-06-08', 'delivered'),
                        (5, 7, 1, '2025-06-10', 'delivered'),
                        (6, 8, 1, '2025-06-12', 'delivered'),
                        (7, 9, 2, '2025-06-15', 'delivered'),
                        (2, 2, 1, '2025-07-01', 'delivered'),
                        (3, 5, 1, '2025-07-04', 'delivered'),
                        (4, 4, 2, '2025-07-06', 'delivered'),
                        (5, 9, 1, '2025-07-09', 'delivered'),
                        (1, 9, 1, '2025-08-02', 'Shipped'),
                        (3, 2, 3, '2025-08-05', 'Shipped'),
                        (5, 4, 1, '2025-08-08', 'Processing'),
                        (7, 5, 2, '2025-08-10', 'Processing'),
                        (6, 3, 1, '2025-08-12', 'Shipped'),
                        (2, 6, 2, '2025-08-15', 'Processing')