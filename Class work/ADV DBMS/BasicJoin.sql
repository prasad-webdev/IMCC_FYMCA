/* Basics of Join queries*/

create database basicjoin;

use basicjoin;

create table employees(
	employee_id int primary key,
    ename varchar(50)
);

desc employees;

insert into employees (employee_id,ename)
values (101,'Pranav'),
(102,'Aayush'),
(103,'Gaurav'),
(104,'Rudra');

select * from employees;

create table projects(
	project_id int primary key,
    pname varchar(50),
    employee_id int,
    foreign key (employee_id)
    references employees(employee_id)
);

desc projects;

insert into projects(project_id, pname, employee_id)
values (1,'Project A', 101),
(2,'Project B', 102),
(3,'Project C', 101),
(4,'Project D', 103);

select * from projects;

insert into employees values(105,'Rohan');
insert into employees values(106,'Prasad');

/*Inner Join*/
/*Only matching records will display
from employees
& projects table*/

select * from employees;

select * from employees
join projects
on employees.employee_id = projects.employee_id;

/* Fetch the employee name and the project name
they belong to*/

select e.ename, p.pname from employees e
inner join projects p
on e.employee_id = p.employee_id;

/* Right Join*/

select e.ename, p.pname from employees e
right join projects p
on e.employee_id = p.employee_id;

select e.ename, p.pname from projects p
right join employees e
on e.employee_id = p.employee_id;

/* Left Join*/

select e.employee_id, e.ename, p.pname from employees e
left join projects p
on e.employee_id= p.employee_id;

insert into projects values(7, 'Project G',105);
insert into projects (Project_id,pname) values (9,'Project H');

/* Full outer Join using union*/
/* display all matching and non matching data from both tables*/

select * from employees
left join projects
on employees.employee_id = projects.employee_id
union
select * from employees
right join projects
on employees.employee_id = projects.employee_id;

/* Display employee names who has been assigned any project*/

select employees.ename, projects.pname from employees
left join projects on employees.employee_id = projects.employee_id
where projects.employee_id is not null;

select employees.ename, projects.pname from employees
right join projects on employees.employee_id = projects.employee_id
where projects.employee_id is not null;

/* Display employee names who has not been assigned any project*/

select employees.ename, projects.pname from employees
left join projects on employees.employee_id = projects.employee_id
where projects.employee_id is null;

select employees.ename, projects.pname from employees
right join projects on employees.employee_id = projects.employee_id
where projects.employee_id is null;