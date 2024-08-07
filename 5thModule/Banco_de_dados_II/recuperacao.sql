	create database recuperacao;
	use recuperacao;

	create table equipamentos (
		id_equipamento int auto_increment primary key,
		nome_equipamento varchar(255)
	);

	create table exercícios (
		id_ex int auto_increment primary key,
		nome_exercicio varchar(255),
		equipamento int,
		foreign key 
			(equipamento) 
		references 
			equipamentos(id_equipamento)
	);

	create table aluno (
		id_aluno int auto_increment primary key,
		nome_aluno varchar(255),
		qtd_treinos_iniciados int
	);

	create table treino (
		id_treino int auto_increment primary key,
		data_inicio date,
		aluno int,
		foreign key 
			(aluno) 
		references 
			aluno(id_aluno)
	);

	create table ex_treino (
		id_ex_treino int auto_increment primary key,
		treino int,
		exercicio int,
		serie int,
		repeticoes int,
		foreign key 
			(treino) 
		references 
			treino(id_treino),
		foreign key 
			(exercicio) 
		references 
			exercicio(id_ex)
	);
	insert into 
		equipamentos 
	values 
		(0, 'Adnominal paralelo'), 
		(0, 'Barra fixa'), 
		(0,'Barra guiada')
	;
	insert into 
		exercicios 
	values 
		(0, 'Abnominal roll up', 1), 
		(0, 'Flexão de corpo', 2), 
		(0,'Agachamento sumo', 3), 
		(0, 'Andominal com elevação de quadril', 1)
	;
	insert into 
		aluno 
	values 
		(0, 'Maria', 0), 
		(0, 'José', 0)
	;
	insert into 
		treino 
	values 
		(0, '20230101', 1), 
		(0, '20221022', 2), 
		(0,'20230202', 1)
	;
	insert into 
		ex_treino 
	values 
		(0, 1, 1, 2, 10), 
		(0, 1, 2, 3, 8), 
		(0, 1, 3, 4, 10), 
		(0, 2, 4, 1, 25), 
		(0, 2, 1, 1, 15), 
		(0, 3, 1, 1, 30), 
		(0, 3, 2, 5, 60)
	;

select * from aluno;
-- a)	Mostre os exercícios e seus respectivos equipamentos utilizados nos treinos realizados pelo aluno José.
	select 
		aluno.nome_aluno, exercicios.nome_exercicio, equipamentos.nome_equipamento
	from 
		aluno, exercicios, equipamentos, treino, ex_treino
	where 
		treino.id_treino = ex_treino.treino and
        ex_treino.exercicio = exercicios.id_ex and
        exercicios.equipamento = equipamentos.id_equipamento and
        treino.aluno = aluno.id_aluno and
		aluno.nome_aluno = 'José'
	;

-- b)	Qual o equipamento mais utilizado nos treinos dos alunos da academia.
	select 
		equipamentos.nome_equipamento, count(*) as quantidade_utilizada
	from 
		treino, ex_treino, exercicios, equipamentos
	where 
		treino.id_treino = ex_treino.treino and
		ex_treino.exercicio = exercicios.id_ex and
		exercicios.equipamento = equipamentos.id_equipamento
	group by 
		equipamentos.nome_equipamento
	order by 
		quantidade_utilizada desc
	limit 1
    ;

-- c)	Quantos “Abnominal roll up” a aluna Maria já realizou de acordo com os treinos montados pelo professor da academia. 
-- 		(considerar as séries e repetições) ou seja, se  o professor pediu pra fazer 2 séries de 10 ela deverá ter executado 20 vezes o exercício.
select 
    sum(ex_treino.serie * ex_treino.repeticoes) as total_repetições
from 
    aluno, treino, ex_treino, exercicios
where 
    aluno.id_aluno = treino.aluno and
    treino.id_treino = ex_treino.treino and
    ex_treino.exercicio = exercicios.id_ex and
    aluno.id_aluno = 1 and
    exercicios.id_ex = 1 and
    ex_treino.exercicio = exercicios.id_ex;

-- 3-	Crie as triggers para contar a quantidade de treinos iniciados pelos alunos. (campo já criado na tabela alunos) 
	-- 	CREATE DEFINER=`root`@`localhost` TRIGGER `treino_AFTER_INSERT` AFTER INSERT ON `treino` FOR EACH ROW 
	-- 	BEGIN
	-- 		update 
	-- 			aluno 
	-- 		set 
	-- 			qtd_treinos_iniciados = qtd_treinos_iniciados + 1 where id_aluno = new.aluno
	-- 		;
	-- 	END

-- 4-	Crie um stored procedure para que quando a pessoa colocar o ID do exercício ela traga o nome dele e o equipamento utilizado. 
	-- 	CREATE DEFINER=`root`@`localhost` PROCEDURE `buscar_exercicio_equipamento`(IN id_exercicio INT)
	-- 	begin
	-- 		select 
	-- 			exercicios.nome_exercicio, 
	-- 			equipamentos.nome_equipamento
	-- 		from 
	-- 			exercicios, equipamentos
	-- 		where 
	-- 			exercicios.equipamento = equipamentos.id_equipamento and
	-- 			exercicios.id_ex = id_exercicio
	-- 		;
	-- 	END

select * from treino;
select * from aluno;
insert into treino values (0, '20240419', 2);
insert into treino values (0, '20240419', 1);

call buscar_exercicio_equipamento(1);