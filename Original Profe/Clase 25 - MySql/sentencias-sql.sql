create database if not exists `test-test`;
drop database `test-test`;

use codo;
show tables;
describe customers;
describe products;

create table if not exists customers(
	id int not null auto_increment primary key,
    name varchar(25) not null,
    dni varchar(10) not null,
    is_deleted boolean not null default false,
    deleted_at timestamp default null
);

alter table customers add phone varchar(20) not null;
alter table customers modify phone int not null;
alter table customers drop column phone;
drop table if exists customers;

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

insert into products (description,price,is_deleted) values
('Bagel de salmón', 100.00,0),
('Hamburguesa clásica' ,200.00,0),
('Sandwich veggie', 300.00,0),
('Ensalada veggie', 400.00,0),
('Veggie avocado', 500.00,0),
('Focaccia BLT', 100.00,0),
('Sandwich de queso', 200.00,0),
('Hamburguesa especial', 500.00,0);

insert customers (name, dni) values
("Jorge Juarez", 340001111),
("Gastón García", 32000222),
("Laura Lopez", 31000222),
("Roberto Ramirez", 34000333),
("Lucas Latino", 43000999);

insert into orders (total, customer_id) values
(800, 1), (1300, 2), (500, 2), (1200, 3), (2400, 4), (200, 4), (100, 5);
      
insert into order_details (order_id, product_id, quantity) values
	(10000, 104, 1), (10000, 102, 1), (10001, 107, 2),
	(10001, 102, 1), (10002, 104, 1), (10003, 103, 3),
    (10004, 107, 4), (10004, 101, 2), (10005, 100, 2),
    (10006, 100, 1);


select * from customers;
select * from orders;

select name, dni
from customers c
where c.dni > 34200000
order by dni desc;

update customers
set dni = 34000111
where name like "Jorge%";

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

