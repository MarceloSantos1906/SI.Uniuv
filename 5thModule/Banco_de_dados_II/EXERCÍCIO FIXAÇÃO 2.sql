show tables;
-- 1- Quem é o dono do animal chamado Thor
select * from animais, donos;
select 
	animais.nome_animal, donos.nome_dono 
from 
	animais, donos
where
	animais.dono = donos.id_dono and
    animais.nome_animal = 'thor'
;

-- 2- Qual a "especialidade" dos veterinários das consultas no mês de abril de 2024.
select * from consultas;
select * from veterinarios, especialidades_veterinarios, especialidades, consultas;
select 
	veterinarios.nome_veterinario, especialidades.nome_especialidade, consultas.data_consulta
from
	veterinarios, especialidades_veterinarios, especialidades, consultas
where
	veterinarios.id_veterinario = especialidades_veterinarios.veterinario and
    especialidades_veterinarios.especialidade = especialidades.id_especialidade and
    consultas.veterinario = veterinarios.id_veterinario and
    consultas.data_consulta >= '2024-04-01' and
    consultas.data_consulta <= '2024-04-30'
;

-- 3- Qual o nome e raça dos cachorros
select * from animais, especies, racas;
select 
	animais.nome_animal, racas.nome_raca 
from
	animais, especies, racas
where
	animais.especie = especies.id_especie and
    animais.raca = racas.id_raca and
    especies.nome_especie = 'cachorros'
;

-- 4- Qual o nome e especialidade do veterinário que realizou a consulta com id = 03
select * from veterinarios, especialidades_veterinarios, especialidades, consultas;
select * from consultas;
select
	veterinarios.nome_veterinario, especialidades.nome_especialidade
from
	veterinarios, especialidades_veterinarios, especialidades, consultas
where
	veterinarios.id_veterinario = especialidades_veterinarios.veterinario and
    especialidades_veterinarios.especialidade = especialidades.id_especialidade and
    consultas.veterinario = veterinarios.id_veterinario and
    consultas.id_consulta = 3
;
    
-- 5- Quais os nomes dos animais e seus respectivos donos das consultas realizadas entre 01/04/24 e 04/04/24
select * from animais, donos, consultas;
select 
	animais.nome_animal, donos.nome_dono, consultas.data_consulta
from
	animais, donos, consultas
where
	animais.dono = donos.id_dono and
    animais.id_animal = consultas.animal and
    consultas.data_consulta >= '2024-04-01' and
    consultas.data_consulta <= '2024-04-04'    
;

-- 6- Quantos cada donos gastou em consultas em 2024
select * from donos, consultas;
select * from donos;
select 
	donos.nome_dono, sum(consultas.valor_consulta) as 'total gasto'
from
	donos, consultas, animais
where 
	donos.id_dono = animais.dono and
	consultas.animal = animais.id_animal
group by
	donos.nome_dono
;