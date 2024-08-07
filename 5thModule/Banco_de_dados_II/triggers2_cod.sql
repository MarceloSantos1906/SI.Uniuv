show tables;
select * from produtos;
select * from compras;
select * from vendas;
select * from bkp_produtos;
select * from bkp_vendas;
insert into compras (data_compra, produto, qtd) values ('20240417', 0, 10);
delete from compras where id_compra = 7;
insert into vendas (data_venda, produto, qtd) values ('20240417', 0, 5);
delete from vendas;
delete from produtos;

INSERT INTO 
	produtos (id_produto, nome_prod, preco, estoque)
SELECT 
	id_produto, nome_produto, preco, estoque
FROM 
	bkp_produtos
where
	id_produto = 0
;

create table bkp_compras(id_bkp int auto_increment, id_compra int, data_compra date, produto int, qtd int, data_excl date, hr_excl time, usuario varchar(45), primary key(id_bkp));
create table bkp_vendas(id_bkp int auto_increment, id_venda int, data_venda date, produto int, qtd int, data_excl date, hr_excl time, usuario varchar(45), primary key(id_bkp));

create view funcionario2 as select * from produtos where preco > 0;
select * from funcionario2;

call busca_prod(0);

