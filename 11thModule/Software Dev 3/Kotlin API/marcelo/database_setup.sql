-- Create database (run this first if database doesn't exist)
-- CREATE DATABASE basektor;

-- Connect to the database
-- \c basektor;

-- Drop tables if they exist (for clean setup)
DROP TABLE IF EXISTS sale_items CASCADE;
DROP TABLE IF EXISTS sales CASCADE;
DROP TABLE IF EXISTS customers CASCADE;
DROP TABLE IF EXISTS products CASCADE;

-- Create Products table
CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    unit VARCHAR(50) NOT NULL,
    quantity INTEGER NOT NULL DEFAULT 0,
    price DECIMAL(10,2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create Customers table
CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    cpf VARCHAR(14) NOT NULL UNIQUE,
    name VARCHAR(255) NOT NULL,
    street VARCHAR(255) NOT NULL,
    neighborhood VARCHAR(255) NOT NULL,
    city VARCHAR(255) NOT NULL,
    state VARCHAR(255) NOT NULL,
    uf VARCHAR(2) NOT NULL,
    phone VARCHAR(20) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create Sales table
CREATE TABLE sales (
    id SERIAL PRIMARY KEY,
    date VARCHAR(10) NOT NULL,
    customer_id INTEGER NOT NULL,
    total_sale DECIMAL(10,2) NOT NULL DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customers(id) ON DELETE RESTRICT
);

-- Create Sale Items table
CREATE TABLE sale_items (
    id SERIAL PRIMARY KEY,
    sale_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL CHECK (quantity > 0),
    unit_price DECIMAL(10,2) NOT NULL CHECK (unit_price >= 0),
    total_item DECIMAL(10,2) NOT NULL CHECK (total_item >= 0),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (sale_id) REFERENCES sales(id) ON DELETE CASCADE,
    FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE RESTRICT
);

-- Create indexes for better performance
CREATE INDEX idx_customers_cpf ON customers(cpf);
CREATE INDEX idx_customers_email ON customers(email);
CREATE INDEX idx_sales_customer_id ON sales(customer_id);
CREATE INDEX idx_sales_date ON sales(date);
CREATE INDEX idx_sale_items_sale_id ON sale_items(sale_id);
CREATE INDEX idx_sale_items_product_id ON sale_items(product_id);

-- Insert sample products
INSERT INTO products (name, unit, quantity, price) VALUES 
('Laptop Dell Inspiron 15', 'un', 15, 2500.00),
('Mouse Logitech MX Master', 'un', 50, 250.00),
('Keyboard Mechanical RGB', 'un', 30, 350.00),
('Monitor 24" Full HD', 'un', 20, 800.00),
('Webcam HD 1080p', 'un', 25, 150.00),
('Headset Gamer', 'un', 40, 200.00),
('SSD 500GB', 'un', 35, 400.00),
('RAM 16GB DDR4', 'un', 60, 300.00),
('Graphics Card GTX 1660', 'un', 10, 1200.00),
('Portable Charger', 'un', 80, 80.00);

-- Insert sample customers
INSERT INTO customers (cpf, name, street, neighborhood, city, state, uf, phone, email) VALUES 
('123.456.789-01', 'João Silva Santos', 'Rua das Flores, 123', 'Centro', 'São Paulo', 'São Paulo', 'SP', '11987654321', 'joao.silva@email.com'),
('987.654.321-02', 'Maria Oliveira Costa', 'Av. Brasil, 456', 'Vila Nova', 'Rio de Janeiro', 'Rio de Janeiro', 'RJ', '21987654321', 'maria.oliveira@email.com'),
('456.789.123-03', 'Pedro Souza Lima', 'Rua Principal, 789', 'Jardim América', 'Belo Horizonte', 'Minas Gerais', 'MG', '31987654321', 'pedro.souza@email.com'),
('789.123.456-04', 'Ana Paula Ferreira', 'Rua do Comércio, 321', 'Centro', 'Porto Alegre', 'Rio Grande do Sul', 'RS', '51987654321', 'ana.paula@email.com'),
('321.654.987-05', 'Carlos Eduardo Rocha', 'Av. Paulista, 654', 'Bela Vista', 'São Paulo', 'São Paulo', 'SP', '11876543210', 'carlos.eduardo@email.com');

-- Insert sample sales
INSERT INTO sales (date, customer_id, total_sale) VALUES 
('2024-01-15', 1, 2750.00),
('2024-01-16', 2, 550.00),
('2024-01-17', 3, 1200.00),
('2024-01-18', 4, 1000.00),
('2024-01-19', 5, 680.00),
('2024-01-20', 1, 400.00);

-- Insert sample sale items
INSERT INTO sale_items (sale_id, product_id, quantity, unit_price, total_item) VALUES 
-- Sale 1: João Silva Santos
(1, 1, 1, 2500.00, 2500.00),  -- Laptop
(1, 2, 1, 250.00, 250.00),    -- Mouse

-- Sale 2: Maria Oliveira Costa  
(2, 3, 1, 350.00, 350.00),    -- Keyboard
(2, 6, 1, 200.00, 200.00),    -- Headset

-- Sale 3: Pedro Souza Lima
(3, 9, 1, 1200.00, 1200.00),  -- Graphics Card

-- Sale 4: Ana Paula Ferreira
(4, 4, 1, 800.00, 800.00),    -- Monitor
(4, 6, 1, 200.00, 200.00),    -- Headset

-- Sale 5: Carlos Eduardo Rocha
(5, 7, 1, 400.00, 400.00),    -- SSD
(5, 10, 2, 80.00, 160.00),    -- Portable Charger (quantity 2)
(5, 5, 1, 150.00, 150.00),    -- Webcam

-- Sale 6: João Silva Santos (second purchase)
(6, 8, 1, 300.00, 300.00),    -- RAM
(6, 10, 1, 80.00, 80.00);     -- Portable Charger

-- Create a function to update the updated_at timestamp
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ language 'plpgsql';

-- Create triggers to automatically update the updated_at column
CREATE TRIGGER update_products_updated_at BEFORE UPDATE ON products 
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_customers_updated_at BEFORE UPDATE ON customers 
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_sales_updated_at BEFORE UPDATE ON sales 
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_sale_items_updated_at BEFORE UPDATE ON sale_items 
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

-- Create views for common queries
CREATE VIEW sales_with_customer AS
SELECT 
    s.id,
    s.date,
    s.total_sale,
    c.name as customer_name,
    c.cpf,
    c.email
FROM sales s
JOIN customers c ON s.customer_id = c.id;

CREATE VIEW sale_items_detailed AS
SELECT 
    si.id,
    si.sale_id,
    si.quantity,
    si.unit_price,
    si.total_item,
    p.name as product_name,
    p.unit as product_unit,
    s.date as sale_date,
    c.name as customer_name
FROM sale_items si
JOIN products p ON si.product_id = p.id
JOIN sales s ON si.sale_id = s.id
JOIN customers c ON s.customer_id = c.id;

-- Display table information
SELECT 'Database setup completed successfully!' as status;

-- Show table row counts
SELECT 
    'Products' as table_name, COUNT(*) as row_count FROM products
UNION ALL
SELECT 
    'Customers' as table_name, COUNT(*) as row_count FROM customers
UNION ALL
SELECT 
    'Sales' as table_name, COUNT(*) as row_count FROM sales
UNION ALL
SELECT 
    'Sale Items' as table_name, COUNT(*) as row_count FROM sale_items;
