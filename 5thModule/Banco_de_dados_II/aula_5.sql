use concurso;
SELECT * FROM candidatos;
select nome, sobrenome from candidatos; #1
select nome, salario from candidatos where '2000' >= salario and salario >= '1000'; #2
select * from candidatos where estado='sc'; #3
select * from candidatos where sexo='m' and '90' > peso and peso >= '45' and idade >= '25'; #4
select * from candidatos where estado='pr' and cidade!='união da vitória'; #5
select * from candidatos where estado in ('pr','sc','rs') and idade < '20' and sexo='m'; #6
select * from candidatos where estado in ('pr','sc') and idade < '18'; #7

#8 e 9 não tem altura

select nome, sobrenome, endereco from candidatos where 	id_candidato in ('1', '3', '5', '7'); #10

select * from candidatos where (
sexo='f' and 
estado='pr' and 
idade in ('21', '25') and 
peso in ('50', '100', '150')
);

select nome, salario from candidatos where (
salario between '1000' and '2000'
); #2

SELECT * FROM candidatos order by salario desc;
SELECT * FROM candidatos where 
estado='pr' and 
sexo='m'
order by idade desc 
limit 1
;

SELECT * FROM candidatos where (
nome like 'a%'
);

SELECT * FROM candidatos where (
nome like '___a%' or 
nome like '___e%' or 
nome like '___i%' or 
nome like '___o%' or 
nome like '___u%'
);

select * from candidatos; 
select cidade, round(avg(salario)) as 'avg' 
from candidatos 
group by cidade
having avg > '1000'
order by avg desc;

#1 Qual a média de idade das mulheres entre 20 e 40 ano
select * from candidatos; 
select id_candidato, nome, sexo, round(avg(idade)) from candidatos where
sexo='f' and
idade between '20' and '40'
group by id_candidato, nome, sexo
;
#2 Quais as 3 pessoas com pesos entre 50 e 100 kg que possuem as letras a ou e em seus nomes ou sobrenomes
select * from candidatos; 
select id_candidato, nome, sobrenome, peso from candidatos where
peso between '50' and '100' and
nome like '%a%' or 
nome like '%e%' or 
sobrenome like '%a%' or
sobrenome like '%e%'
limit 3
;

#3 quantas pessoas moram no PR ou SC e tem 20 30 ou 40 anos 
select * from candidatos; 
select estado, count(*) as qtd from candidatos where
estado in ('pr', 'sc') and
idade in ('20', '30', '40')
group by estado
;

#4 qual a Média de peso por sexo
select * from candidatos; 
select sexo, round(avg(peso)) as avg_peso from candidatos
group by sexo
;
#5 Qual é a soma dos salários dos homens entre 20 e 50 anos que não moram nas cidades Curitiba ou Toledo
select * from candidatos; 
select sexo, cidade, idade, round(avg(salario)) as avg_salario from candidatos
group by sexo, cidade, idade
having cidade not in ('Curitiba', 'Toledo')
order by avg_salario desc
;

#6 Os paranaenses que ganham mais que 1000 reais precisaram pagar 5% de imposto sobre o seus salários, mostre o nome e o valor a ser pago
select * from candidatos; 
select nome, round(salario*0.05) as 'valor a pagar' from candidatos where
salario > '1000'
;

#7 Qual a mulher mais velha entre as pessoas com salario entre 800 e 1500 reais
select * from candidatos; 
select nome, sobrenome, salario from candidatos where
salario between 800 and 1500
order by salario desc
limit 1
;

#8 pessoas que ganham acima da média salarial
select * from candidatos; 
select nome, sobrenome, round(salario) from candidatos where
salario > (select avg(salario) from candidatos);

#9 Conte qtas pessoas de cada cidade se inscreveu
select * from candidatos; 
select cidade, count(*) as 'count' from candidatos
group by cidade
;

#10 mostre os homens de curitiba com os 3 salários mais baixos
select * from candidatos; 
select nome, sobrenome, sexo, cidade, salario from candidatos where
sexo='m' and 
cidade='curitiba'
order by salario asc
limit 3
;

select