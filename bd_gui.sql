-- create schema bd_gui -- cria o schema do aluno
-- use bd_gui -- seleciona a tabela do aluno
drop table aluno; -- apaga a tabela do aluno
drop table disciplina
drop table professor
/* create table aluno ( -- cria a tabela
matricula integer not null,
primary key(matricula),
CPF varchar (14) null,
unique key(CPF),
nome varchar(30) not null,
data_nasc date
);
desc aluno; -- mostra a estrutura da tabela
select*from aluno; -- mostra os dados da tabela
insert into aluno values (1, '704.559.684-70', 'Guilherme Manuel', '2009-03-07')
*/

/*create table professor (
matricula integer not null,
primary key(matricula),
professor varchar(30) not null,
formacao varchar(50) not null
);*/

/*create table disciplina (
	codigo integer not null,
	primary key(codigo),
	nome varchar(30) not null,
	CH integer,
	mat_professor integer,
    foreign key (mat_professor) references professor (matricula)
);*/

-- desc professor
-- desc disciplina

/*insert into disciplina values (1,'BD',80,null);
select*from disciplina;
insert into professor values (1,'Eric','Ciências da Computação');
select*from professor;
insert into disciplina values (2,'Web',100,1);*/


-- 06/06

create table tutor (
codigo integer not null primary key,
nome varchar(30) not null unique key,
telefone varchar(10) not null,
profissao varchar(30),
sexo char
);

create table animal (
numero integer not null primary key,
nome varchar(30) not null,
idade integer,
especie varchar(30) not null,
sexo char,
cod_tutor integer,
foreign key (cod_tutor) references tutor (codigo)
);

select*from tutor
select*from animal
desc animal
desc tutor

delete from tutor
insert into tutor values (1, "Carol", "123", null, null)
insert into animal values (1, "Thor",7, "cachorro", null, 1)
insert into animal values (2, "Judite", 8, "jabuti", "F", 1)

-- 27/06

update tutor
set sexo = "F"
where codigo = 1;

-- Com os tres ultimos abaixo podem ser usados o WHERE
-- C
-- R, SELECT
-- U, UPDATE
-- D, DELETE