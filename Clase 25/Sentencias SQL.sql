SET SQL_SAFE_UPDATES = 0;

CREATE TABLE customers(
id int not null auto_increment primary key, 
name varchar(50) not null,
dni varchar(10) not null,
is_deleted boolean not null default false,
deleted_at timestamp default null
);

SHOW TABLES;
DESCRIBE customers;
SELECT * FROM customers;

ALTER TABLE customers add phone varchar (20) not null;
ALTER TABLE customers MODIFY phone int not null;
ALTER TABLE customers add phone2 varchar (20) not null;
ALTER TABLE customers DROP COLUMN phone2;

create table if not exists products(
	id int not null auto_increment primary key,
    description varchar(50) not null,
    price decimal(6,2) not null,
	is_deleted tinyint not null default 0,
    deleted_at timestamp default null
) auto_increment = 100;

create table if not exists orders(
	id int not null auto_increment,
    created_at timestamp not null default current_timestamp,
	is_deleted tinyint not null default 0,
    deleted_at timestamp default null,
    total int not null,
    customer_id int not null,
    primary key(id),
    foreign key(customer_id) references customers(id)
) auto_increment = 10000;

create table if not exists order_details(
	id int not null auto_increment,
    order_id int not null,
    product_id int not null,
    quantity int not null,
    primary key(id),
    foreign key(order_id) references orders(id),
    foreign key(product_id) references products(id)
);

ALTER TABLE customers MODIFY phone int default null;

INSERT INTO customers (name, dni) VALUES
("Eugenio Vázquez", 27957231),
("Eugenioz Blázquez", 37957231),
("Eugene Garquez", 28957231),
("Axel Vázquez", 27858231);

INSERT INTO customers (name, dni) VALUES
("Roquefort Roquez", 27952132);

insert into products (description,price,is_deleted) values
('Bagel de salmón', 100.00,0),
('Hamburguesa clásica' ,200.00,0),
('Sandwich veggie', 300.00,0),
('Ensalada veggie', 400.00,0),
('Veggie avocado', 500.00,0),
('Focaccia BLT', 100.00,0),
('Sandwich de queso', 200.00,0),
('Hamburguesa especial', 500.00,0);

SELECT * FROM products;
DESCRIBE order_details;
insert into orders (total, customer_id) values
(800, 1), (1300, 2), (500, 2), (1200, 3), (2400, 4), (200, 4), (100, 5);
  
insert into order_details (order_id, product_id, quantity) values
	(10007, 104, 1), (10007, 102, 1), (10008, 107, 2),
	(10008, 102, 1), (10009, 104, 1), (10010, 103, 3),
    (10011, 107, 4), (10011, 101, 2), (10012, 100, 2),
    (10013, 100, 1);


select * from customers;
select * from orders;
select * from products;
select * from order_details;

select name, dni
from customers c
where c.dni > 28200000
order by dni desc;

update customers
set dni = 34000111
where name like "Axel%";

select distinct name, dni
from customers
limit 3;

select description, price
from products
where description like "%hamburguesa%";

select avg(price) 'Promedio' from products
where description like "%hamburguesa%";

select
name as "Nombre cliente",
o.id as "Nro pedido",
p.description as "Producto",
o.total as "Total" from customers c
join orders o on c.id = o.customer_id
join order_details d on o.id = d.order_id
join products p on p.id = d.product_id;

select
name as "Nombre cliente",
o.id as "Nro pedido",
sum(p.price * d.quantity) as "Total" from customers c
join orders o on c.id = o.customer_id
join order_details d on o.id = d.order_id
join products p on p.id = d.product_id
group by o.id;

select
name as "Nombre cliente",
o.id as "Nro pedido",
sum(p.price * d.quantity) as "Total" from customers c
join orders o on c.id = o.customer_id
join order_details d on o.id = d.order_id
join products p on p.id = d.product_id
group by o.id
-- having count(p.id) > 1;
having sum(p.price * d.quantity) > 1200;
