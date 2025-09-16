-- Products table
CREATE TABLE IF NOT EXISTS products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    unit VARCHAR(50) NOT NULL,
    quantity INTEGER NOT NULL DEFAULT 0,
    price DECIMAL(10,2) NOT NULL
);

-- Customers table  
CREATE TABLE IF NOT EXISTS customers (
    id SERIAL PRIMARY KEY,
    cpf VARCHAR(14) NOT NULL UNIQUE,
    name VARCHAR(255) NOT NULL,
    street VARCHAR(255) NOT NULL,
    neighborhood VARCHAR(255) NOT NULL,
    city VARCHAR(255) NOT NULL,
    state VARCHAR(255) NOT NULL,
    uf VARCHAR(2) NOT NULL,
    phone VARCHAR(20) NOT NULL,
    email VARCHAR(255) NOT NULL
);

-- Sales table
CREATE TABLE IF NOT EXISTS sales (
    id SERIAL PRIMARY KEY,
    date VARCHAR(10) NOT NULL,
    customer_id INTEGER NOT NULL,
    total_sale DECIMAL(10,2) NOT NULL DEFAULT 0,
    FOREIGN KEY (customer_id) REFERENCES customers(id)
);

-- Sale Items table
CREATE TABLE IF NOT EXISTS sale_items (
    id SERIAL PRIMARY KEY,
    sale_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    unit_price DECIMAL(10,2) NOT NULL,
    total_item DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (sale_id) REFERENCES sales(id) ON DELETE CASCADE,
    FOREIGN KEY (product_id) REFERENCES products(id)
);

-- Sample data
INSERT INTO products (name, unit, quantity, price) VALUES 
('Laptop', 'un', 10, 2500.00),
('Mouse', 'un', 50, 25.00),
('Keyboard', 'un', 30, 75.00);

INSERT INTO customers (cpf, name, street, neighborhood, city, state, uf, phone, email) VALUES 
('123.456.789-00', 'João Silva', 'Rua A, 123', 'Centro', 'São Paulo', 'São Paulo', 'SP', '11987654321', 'joao@email.com'),
('987.654.321-00', 'Maria Santos', 'Rua B, 456', 'Vila Nova', 'Rio de Janeiro', 'Rio de Janeiro', 'RJ', '21987654321', 'maria@email.com');

INSERT INTO sales (date, customer_id, total_sale) VALUES 
('2024-01-15', 1, 2525.00),
('2024-01-16', 2, 100.00);

INSERT INTO sale_items (sale_id, product_id, quantity, unit_price, total_item) VALUES 
(1, 1, 1, 2500.00, 2500.00),
(1, 2, 1, 25.00, 25.00),
(2, 3, 1, 75.00, 75.00),
(2, 2, 1, 25.00, 25.00);
