insert into alunos (id_aluno, nome_aluno)
 values('1', 'Maria');
select * from alunos;
insert into alunos values('8', 'JOSÉ', 'experimental');
select * from alunos;
insert into exercicios (nome_ex) values ('supino'),('remada baixa'),('crunch');
select * from exercicios;
insert into instrutores values(0,'marcos'),(0,'aline');
select * from instrutores;
insert into treino values
(0,'20240311','1','1'),
(0,'20240301','1','2'),
(0,'20240308','8','2');
select * from treino;
insert into ex_treino values
(0,'1','1','5','10'),
(0,'1','2','3','20'),
(0,'2','3','5','30');
select * from ex_treino;
update alunos set tipo='pagante' where id_aluno='8';
select * from alunos;
update instrutores set telefone='(42) 988 880 000' where id_instrutor='1';
select * from instrutores;
update treino set 
data_in='20240313',
instrutor='2'
where id_treino='1';
select * from treino;
delete from ex_treino where treino='1';
select * from ex_treino;
delete from treino where id_treino='1';
select * from treino;

select * from exercicios;
delete from ex_treino where exercicio='3';
delete from exercicios where id_ex='3';