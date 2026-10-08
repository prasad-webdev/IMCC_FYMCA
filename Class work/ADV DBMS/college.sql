-- DML Commands

create database college;
use college;

create table Employee(
    EmpID int, 
    first_name varchar(20), 
    last_name varchar(20), 
    EmpAge int, 
    Empzone varchar(10)
);

desc Employee;