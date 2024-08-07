create database prova3;
use prova3;

-- Tabela de Compra
CREATE TABLE Compra (
    compra_id INT AUTO_INCREMENT PRIMARY KEY,
    carro_id INT,
    data_compra DATE,
    preco_compra DECIMAL(10, 2),
    FOREIGN KEY (carro_id) REFERENCES Carros(carro_id)
);

-- Tabela de Venda
CREATE TABLE Venda (
    venda_id INT AUTO_INCREMENT PRIMARY KEY,
    carro_id INT,
    data_venda DATE,
    preco_venda DECIMAL(10, 2),
    FOREIGN KEY (carro_id) REFERENCES Carros(carro_id)
);

-- Tabela de Carros
CREATE TABLE Carros (
    carro_id INT AUTO_INCREMENT PRIMARY KEY,
    preco_compra DECIMAL(10, 2),
    preco_venda DECIMAL(10, 2)
);

CREATE TABLE Carros_Backup (
    backup_id INT AUTO_INCREMENT PRIMARY KEY,
    carro_id INT,
    preco_compra DECIMAL(10, 2),
    preco_venda DECIMAL(10, 2),
    acao VARCHAR(20), -- "insercao", "atualizacao" ou "exclusao"
    data_backup TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

select * from compra;
select * from venda;
select * from carros;
select * from carros_backup;
insert into compra (data_compra, preco_compra) values('20240417', 1000);
insert into venda (carro_id, data_venda, preco_venda) values(0,'20240417', 1600);
delete from carros;


-- trigger 1 ao comprar adiciona carro a tabela carro
-- trigger 2 ao vender um carro remove o carro da tabela carro

-- procedure 1 altera o valor da venda do carro que inicialmente vem com 50% acima do valor da compra
-- procedure 2 altera o valor da compra do carro
-- procedure 3 registra uma compra
-- procedure 4 altera uma venda, podendo alterar o carro, o preço da venda, e a data da venda
-- procedure 5 registra uma venda
