USE productos;

CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    sku VARCHAR(100) NOT NULL,
    stock INTEGER default 100
);


INSERT INTO products (product_name, sku) VALUES ('iPhone 15 Pro', 'ipYWO9738URRROW1');
INSERT INTO products (product_name, sku) VALUES ('iPhone 16 Pro', 'ipYWO9738UEI3000');
INSERT INTO products (product_name, sku) VALUES ('GoPro HERO13 Black', 'GO98728-FT');
INSERT INTO products (product_name, sku) VALUES ('Revell 85-4313 69 Boss 302 Mustang', 'RV09y7376401923');
INSERT INTO products (product_name, sku) VALUES ('Sparmax Tc2000 Compressor', 'PX-2829837485');
INSERT INTO products (product_name, sku) VALUES ('Fender Squier Debut Series Stratocaster', '839499384-xxxx');
INSERT INTO products (product_name, sku) VALUES ('Sennheiser HD 350BT', 'S-939383944');



