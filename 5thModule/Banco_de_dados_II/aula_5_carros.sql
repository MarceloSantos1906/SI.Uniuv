create database pessoas_aula_5;
use pessoas_aula_5;
create table dados(
id varchar(100) primary key,
nome varchar(100),
marca_carro varchar(100),
ano varchar(100),
cor_carro varchar(100),
valor_carro varchar(100)
);

SELECT * FROM dados;
select count(*) from dados;
#1 - * Mostre o nome das pessoas que tem carros da marca Honda, da cor red e que custem 50000, 60000 ou 70000 mil reais*
select * from dados where valor_carro='50000';
select * from dados where valor_carro='60000';
select * from dados where valor_carro='70000';
select nome, marca_carro from dados where(
marca_carro='honda' and
cor_carro='red' and
valor_carro in ('50000', '60000', '70000')
);

#2 - * Quais o nomes da pessoas que tem a letra e na quinta posição em seu nome
select id, nome from dados where(
nome like '____e%'
);
#2.1 ou que o que contenham a letra "e" em qualquer posição do nome*
select id, nome from dados where(
nome like '%e%'
);

#3 - * Carros dos anos 2000 
select id, marca_carro, ano from dados where(
ano='2000'
);
#3.1 ou que sejam entre os anos 2010 e 2014 *
select id, marca_carro, ano from dados where(
ano between '2010' and '2014'
);

#4 - * Carros que não são das marcas Mercedes-Benz, Saturn, Hyundai ou Honda e que custem entre 45000 e 80000*
select id, marca_carro, valor_carro from dados where(
marca_carro in ('Mercedes-Benz', 'Saturn', 'Hyundai', 'Honda') and
valor_carro between '45000' and '80000'
);

#5 - * Carros que contenham a letra "a" na Marca e que as cores não contenham a letra "e"
select id, marca_carro, cor_carro from dados where(
marca_carro like '%a%' and
cor_carro not like '%e%'
);

#6 -*Nome das pessoas que tem uma Lamborghini que custa mais que 100000* e a cor não seja "Yellow"
select id, nome, marca_carro, valor_carro, cor_carro from dados where(
marca_carro='Lamborghini' and
valor_carro >= '100000' and
cor_carro!='yellow'
);
	