use granja;

create table if not exists products(
	id int not null auto_increment primary key,
    description varchar(50) not null,
    category varchar(50) not null,
    price decimal(6,2) not null,
    is_deleted tinyint not null default 0,
    deleted_at timestamp default null
);

alter table products
	add icon varchar(50) default 'placeholder';
    
create table if not exists orders(
	id int not null auto_increment primary key,
    created_at timestamp not null default current_timestamp,
	is_deleted tinyint not null default 0,
    deleted_at timestamp default null,
    total decimal(6,2) not null
) auto_increment = 10000;

alter table orders
	add customer_id int not null;

insert into products (description, price, category, icon) values
('Rábano', 3.26, 'vegetales', 'raddish'),
('Alcaucil', 9.44, 'vegetales', 'artichoke'),
('Brócoli', 5.2, 'vegetales', 'broccoli'),
('Repollo', 0.95, 'vegetales', 'cabbage'),
('Cereza', 1.04, 'frutas', 'cherry'),
('Zanahoria', 4.82, 'vegetales', 'carrot'),
('Choclo', 7.53, 'vegetales', 'corn'),
('Uva', 4.94, 'frutas', 'grapes'),
('Cebolla', 6.45, 'vegetales', 'onion'),
('Naranja', 9.95, 'frutas', 'orange'),
('Pera', 2.61, 'frutas', 'peas'),
('Ananá', 1.62, 'frutas', 'pineapple'),
('Chuleta', 8.32, 'carnes', 'steak'),
('Sandía', 5.08, 'frutas', 'watermelon'),
('Salchicha', 3.69, 'embutidos', 'sausage');

create table if not exists order_details(
	id int not null auto_increment,
    order_id int not null,
    product_id int not null,
    quantity int not null,
    primary key(id),
    foreign key(order_id) references orders(id),
    foreign key(product_id) references products(id)
);

insert into orders (total, customer_id) values
(800, 1), (1300, 2), (500, 2), (1200, 3), (2400, 4), (200, 4), (100, 5);
      
insert into order_details (order_id, product_id, quantity) values
	(10000, 104, 1), (10000, 102, 1), (10001, 107, 2),
	(10001, 102, 1), (10002, 104, 1), (10003, 103, 3),
    (10004, 107, 4), (10004, 101, 2), (10005, 100, 2),
    (10006, 100, 1);