use concurso2;
select * from candidatos;
# 1-	Candidatos que moram em união da vitória ou porto união e irão fazer a prova para programador.
select candidatos.nome, cidades.nome_cidade, cargos.Nome_cargo from candidatos, cidades, cargos where
candidatos.cidade = cidades.id_cidade and
candidatos.cargo_pretendido = cargos.id_cargo and
cargos.Nome_cargo = 'programador' and
cidades.nome_cidade  in ('união da vitória', 'porto união')
;

# 2-	Média salarial dos inscritos para o cargo de programador e irão fazer a prova na UNIUV
select candidatos.nome, candidatos.sobrenome, cidades.nome_cidade, round(avg(candidatos.salario)) as 'med sal', local_prova.Nome_local from 
candidatos inner join cidades inner join cargos inner join local_prova where
candidatos.cidade = cidades.id_cidade and
candidatos.cargo_pretendido = cargos.id_cargo and
cargos.Nome_cargo = 'programador' and
cidades.nome_cidade  in ('união da vitória', 'porto união') and
local_prova.Nome_local = 'uniuv'
group by candidatos.nome, candidatos.sobrenome, cidades.nome_cidade;
;

# 3-	Quantidade de Inscritos por cargo
select count(candidatos.id_candidato) as 'qtd insc', cargos.Nome_cargo from 
	candidatos inner join cargos on
		candidatos.cargo_pretendido = cargos.id_cargo
group by cargos.Nome_cargo
;

# 4-	Média salarial dos inscritos por cargo.
select round(avg(c.salario)) as 'med sal', ca.Nome_cargo from candidatos c inner join cargos ca on
	c.cargo_pretendido = ca.id_cargo
group by ca.Nome_cargo
;

# 5-	O local de prova vai ganhar 10% do valor arrecado em inscrições. Quanto cada local irá receber.
select round((c.valor_inscricao)) as 'valor arrecadado', l.Nome_local, round(sum(c.valor_inscricao)*0.1) as 'valor a receber' from cargos c, local_prova l
group by l.Nome_local, c.valor_inscricao
;

# 6-	Pessoas que estimam um maior salário ao realizar o concurso.
select * from candidatos, cargos;
select
	candidatos.nome, candidatos.sobrenome, candidatos.salario as 'salario atual', cargos.Nome_cargo as 'cargo pretendido', cargos.salario_cargo 'salario pretendido'
from 
	candidatos, cargos
where
	candidatos.cargo_pretendido = cargos.id_cargo and
    candidatos.salario < cargos.salario_cargo
order by
	candidatos.salario asc
;

# 7-	2 cargos com maior concorrência
select count(candidatos.cargo_pretendido) as 'qtd', cargos.Nome_cargo from candidatos inner join cargos on
	candidatos.cargo_pretendido = cargos.id_cargo
group by cargos.Nome_cargo having
qtd > 2
;

# 8-	Mulheres que se inscrevem para o(s) cargo(s) de Tecnologia
select c.nome, c.sobrenome, c.sexo, ca.Nome_cargo from candidatos c inner join cargos ca on
	c.cargo_pretendido = ca.id_cargo where
	c.sexo = 'f'
;

# 9-	Cargos com maior valor arrecadado em inscrições
select * from candidatos, cargos;
select round(sum(cargos.valor_inscricao)) as 'valor_arrecadado', cargos.Nome_cargo from candidatos inner join cargos on
	candidatos.cargo_pretendido = cargos.id_cargo
group by cargos.Nome_cargo
order by valor_arrecadado desc
;

# 10-	Vagas por candidatos no cargo de professor
select * from candidatos where candidatos.cargo_pretendido = 1;
select
	round(cargos.vagas/count(candidatos.cargo_pretendido)) as 'vagas/candidatos', cargos.Nome_cargo, cargos.vagas
from
	candidatos inner join cargos on
		candidatos.cargo_pretendido = cargos.id_cargo
group by 
	cargos.Nome_cargo, cargos.vagas
having
	cargos.Nome_cargo = 'Professor'
;

# 11-	Cargo com o número de inscrições abaixo da média se comparado com outros cargos
select * from candidatos, cargos;
select
	count(candidatos.id_candidato) as 'n_insc', cargos.Nome_cargo
from
	candidatos
inner join cargos on
	candidatos.cargo_pretendido = cargos.id_cargo
group by
	cargos.Nome_cargo
having
	count(candidatos.id_candidato) < (
		select avg(cnt) from (
			select count(candidatos.id_candidato) as cnt from candidatos
            group by candidatos.cargo_pretendido
            )
		as subquerry
		)
;

# 12-	Mostre um relatório com o nome do candidato, local de prova contendo nome da cidade e estado e cargo pretendido.
select * from candidatos, cargos, cidades, estados, local_prova;
select 
	candidatos.nome, candidatos.sobrenome, local_prova.nome_local, cidades.nome_cidade, estados.nome_estado 
from 
	candidatos, cargos, cidades, estados, local_prova
where
    candidatos.local_prova = local_prova.idlocal_prova and
	candidatos.cidade = cidades.id_cidade and
    cidades.uf = estados.uf_estado and
    candidatos.cargo_pretendido = cargos.id_cargo
;

# 13-	Qual estado teve o maior número de inscrições
select * from candidatos, cidades, estados;
select 
	count(candidatos.id_candidato) as qtd, estados.Nome_estado 
from 
	candidatos, cidades, estados
where
	candidatos.cidade = cidades.id_cidade and
    cidades.Uf = estados.uf_estado
group by 
	estados.Nome_estado
order by
	qtd desc
limit 1
;

# 14-	Qual a média de idade das pessoas que se inscreveram para programador, são de São Paulo ou Santa Catarina
select round(avg(c.idade)) as 'med sal', e.Nome_estado, ca.Nome_cargo from candidatos c inner join cargos ca inner join estados e inner join cidades ci on 
	c.cargo_pretendido = ca.id_cargo and
    c.cidade = ci.id_cidade and
    ci.Uf = e.uf_estado
group by e.Nome_estado, ca.Nome_cargo having
e.Nome_estado in ('São Paulo', 'Santa Catarina') and
ca.Nome_cargo = 'programador'
;

# 15-	Qual a cidade com o menor número de inscrições
select * from candidatos, cidades;
select 
	count(candidatos.id_candidato) as qtd, cidades.nome_cidade
from 
	candidatos, cidades
where
	candidatos.cidade = cidades.id_cidade
group by 
	cidades.nome_cidade
order by
	qtd asc
;

# 16-	Quantas pessoas do Paraná se inscreveram para os cargos que não são ligados a tecnologia
select * from candidatos, estados, cargos, cidades
where estados.Nome_estado = 'Paraná' and
cargos.Nome_cargo not in ('Técnico em Informática', 'Programador');
select
	sum(candidatos.id_candidato) as 'qtd', estados.Nome_estado, cargos.Nome_cargo 
from 
	candidatos inner join estados inner join cargos inner join cidades on
		candidatos.cidade = cidades.id_cidade and
		cidades.Uf = estados.uf_estado and
		candidatos.cargo_pretendido = cargos.id_cargo 
where
	estados.Nome_estado = 'Paraná' and
	cargos.Nome_cargo not in ('Técnico em Informática', 'Programador')
group by
	estados.Nome_estado, cargos.Nome_cargo
;

# 17-	Média de peso por local de prova
select * from candidatos, local_prova;
select 
	round(avg(candidatos.peso)) as 'med peso', local_prova.Nome_local
from 
	candidatos, local_prova
where
	candidatos.local_prova = local_prova.idlocal_prova
group by
	local_prova.Nome_local
;

# 18-	Candidatos que não são do SUL do país
select * from candidatos, cidades, estados;
select 
	candidatos.nome, candidatos.sobrenome, estados.Nome_estado
from 
	candidatos, cidades, estados
where
	candidatos.cidade = cidades.id_cidade and
    cidades.uf = estados.uf_estado and
    estados.Nome_estado not in ('Paraná', 'Santa Catarina', 'Rio Grande do Sul')
;

# 19-	Média de idade por estado
select * from candidatos, cidades, estados;
select 
	round(avg(candidatos.idade)) as 'med idade', estados.Nome_estado
from 
	candidatos, cidades, estados
where
	candidatos.cidade = cidades.id_cidade and
	cidades.uf = estados.uf_estado
group by
	estados.Nome_estado
;

# 20-	Quantidade de inscrições por estado
select * from candidatos, cidades, estados;
select 
	count(candidatos.id_candidato) as 'qtd', estados.Nome_estado
from 
	candidatos, cidades, estados
where
	candidatos.cidade = cidades.id_cidade and
	cidades.uf = estados.uf_estado
group by
	estados.Nome_estado
;

# 21-	Qual cargo Ana 
select candidatos.nome, candidatos.sobrenome, cargos.Nome_cargo from 
	candidatos inner join cargos on
		candidatos.cargo_pretendido = cargos.id_cargo where
        candidatos.nome = 'ana'
;
