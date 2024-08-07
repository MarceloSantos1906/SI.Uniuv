show tables;
#1 Mostre o nome do cliente, sua cidade e seu estado da venda com identificação 1
select * from  clientes, cidades, estados, vendas;
select 
	clientes.nome_cliente, cidades.nome_cidade 
from 
	clientes, cidades, estados, vendas
where
	clientes.cidades_id_cidade = cidades.id_cidade and
    cidades.estado = estados.uf_estado and
    vendas.cliente = clientes.id_cliente and
    vendas.id_venda = 1
;

#2 Quais as marcas e modelos do carros vendidos em abril de 2024
select * from carros, modelos, marcas, vendas;
select 
	marcas.nome_marca, 
    modelos.nome_modelo, 
    vendas.data_venda 
from
	carros, 
    modelos, 
    marcas, 
    vendas
where
	carros.modelo = modelos.id_modelo and
    modelos.marca = marcas.id_marca and
    vendas.carro = carros.id_carro and
    vendas.data_venda >= '20240401' and
    vendas.data_venda <= '20240430'
;

#3 Qual o total de vendas por vendedores
select * from carros, vendas, vendedores;
select * from vendedores;
select 
	round(sum(carros.valor)) as 'total de vendas', 
    vendedores.nome_vendedor
from 
	carros,
    vendas,
    vendedores
where
	vendas.carro = carros.id_carro and
    vendas.vendedor = vendedores.id_vendedor
group by
	vendedores.nome_vendedor
order by
	'total de vendas' desc
;

#4 qual a média de vendas (valor) das vendas realizadas em abril de 2024
select * from carros, vendas;
select 
	round(avg(carros.valor)) as med_valor
from
	carros, vendas
where
	vendas.carro = carros.id_carro and
    vendas.data_venda >= '20240401' and
    vendas.data_venda <= '20240430'
;

#5 qual o cliente que realizou mais compras
select * from clientes;
select * from vendas;
select 
	clientes.nome_cliente,
    count(vendas.id_venda) as qnt_vendas
from 
	clientes,
    vendas
where
	vendas.cliente = clientes.id_cliente
group by
	clientes.nome_cliente
;

#6 qaul o vendedor que menos realizou vendas (quantidade de vendas)
select * from vendedores, vendas;
select
	vendedores.nome_vendedor,
    count(vendas.id_venda) as qtd_vendas
from 
	vendedores,
    vendas
where
	vendas.vendedor = vendedores.id_vendedor
group by
	vendedores.nome_vendedor
order by
	qtd_vendas asc
limit 1
;

#7 qual o valor vendido por vendedor
select * from carros, vendas, vendedores;
select
	round(sum(carros.valor)) as total_vend,
    vendedores.nome_vendedor
from
	carros,
    vendas,
    vendedores
where
	vendas.carro = carros.id_carro and
    vendas.vendedor = vendedores.id_vendedor
group by
	vendedores.nome_vendedor
order by
	total_vend desc
;

#8 mostre a quantidade de vendas realizadas por estado
select * from vendas, clientes, estados, cidades;
select * from clientes;
select * from cidades;
select * from estados;
select
	estados.nome_estado,
    count(vendas.id_venda) as qtd_vendas
from
	vendas,
    clientes,
    cidades,
    estados
where
	vendas.cliente = clientes.id_cliente and
    clientes.cidades_id_cidade = cidades.id_cidade and
    cidades.estado = estados.uf_estado
group by
	estados.nome_estado
;

#9 quantidade de vendas realizadas por marca
select * from vendas, carros, modelos, marcas;
select 
	marcas.nome_marca,
    round(count(vendas.id_venda)) as total_vendas
from
	vendas,
    carros,
    modelos,
	marcas
where
	vendas.carro = carros.id_carro and
    carros.modelo = modelos.id_modelo and
    modelos.marca = marcas.id_marca
group by
	marcas.nome_marca
;

#10 qual o modelo mais vendido
select * from vendas, carros, modelos;
select 
	modelos.nome_modelo,
    round(count(vendas.id_venda)) as total_vendas
from
	vendas,
    carros,
    modelos
where
	vendas.carro = carros.id_carro and
    carros.modelo = modelos.id_modelo
group by
	modelos.nome_modelo
order by
	total_vendas desc
limit 1
;
#11qual a marca e modelo do carro com maior valor
#12 qual carro foi comprado pelo Marcelo
#13 quantas vendas o vendedor Pedro já fez
#14 marcas de carros com ano de fabricação  entre 2000 e 2008
#15 Qual a venda com maior valor realizada para a cidade de Curitiba
#16 Quais as vendas realizadas em abril para o estado de SC
#17 quantas vendas foram realizadas para o estado do PR
#18 qual a média (valor) de vendas por cidade
#19 qual o cliente e seu estado da venda com id igual a 2
#20 Some o valor das vendas realizadas pelo vendedor marcos
#21 Mostre o carro mais vendido da Fiat
#22 Qual o maior valor de venda onde os clientes são do PR
#23 QUantas vendas o vendedor com id 3 realizou
#24 Mostre a  qtd de vendas por cliente
#25 Mostre a quantidade de vendas por modelo
#26 Quantos carros entre os anos 1990 e 2000 foram vendidos
#27 mostre o nome da marca, seu modelo e valor dos carros comprados pelos clientes de SC
#28 calcule a média de valor dos carros por marca, ignore nesse calculo a marca Fiat
#29 quantos carros cada marca tem
#30 quais as marcas de carro com os 3 carros mais caros