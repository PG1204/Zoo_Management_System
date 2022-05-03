create database lib;

use lib;

create table info
(
namee varchar(25),
AID varchar(25)primary key,
pswd varchar(25),
Phone_no varchar(25),
email_id varchar(25),
employee_id varchar(25) 
);

create table emp
(
namee varchar(25),
EID varchar(25)primary key,
Phone_no varchar(25),
email_id varchar(25)
);

create table animal
(
nam varchar(25),
animalID varchar(25)primary key,
speciesID varchar(30),
employee_id varchar(25) 
);

drop table info;
delete FROM animal WHERE animalID = "2" AND speciesID = "3";
SELECT * FROM lib.info;
SELECT * FROM lib.emp;
SELECT * FROM lib.animal;