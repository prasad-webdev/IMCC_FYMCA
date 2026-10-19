/* filtering data from tables */
/* WHERE , SELECT DISTINCT , AND , OR , IN , NOT IN , BETWEEN , LIKE , LIMIT , IS NULL */

create database organization;
use organization;

create table employee(emp_id int not null primary key, first_name varchar(20), last_name varchar(20), gender char, role varchar(15), dept varchar(20), manager_id varchar(10));
desc employee;

INSERT INTO employee VALUES (101, 'Prasad', 'Deshmukh', 'M', 'Developer', 'IT', 'M11');
INSERT INTO employee VALUES (102, 'Sneha', 'Patil', 'F', 'HR Exec', 'HR', 'M12');
INSERT INTO employee VALUES (103, 'Amit', 'Shinde', 'M', 'Lead', 'IT', 'M13');
INSERT INTO employee VALUES (104, 'Pooja', 'Kulkarni', 'F', 'Analyst', 'Finance', 'M14');
INSERT INTO employee VALUES (105, 'Rohan', 'More', 'M', 'Tester', 'QA', 'M15');

SELECT * FROM employee;