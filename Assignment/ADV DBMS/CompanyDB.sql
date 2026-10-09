CREATE DATABASE CompanyDB;
USE CompanyDB;

CREATE TABLE Employees (
    EmpID INT PRIMARY KEY,
    EmpName VARCHAR(50),
    Salary DECIMAL(10, 2),
    JoinDate DATE
);

desc Employees;

CREATE TABLE Departments (
    DeptID INT PRIMARY KEY,
    DeptName VARCHAR(100)
);

desc Departments;

ALTER TABLE Employees ADD Email VARCHAR(100);
desc Employees;

ALTER TABLE Departments ADD dept_location VARCHAR(100);
desc Departments;


ALTER TABLE Employees ADD Phone VARCHAR(15);
ALTER TABLE Employees MODIFY Phone VARCHAR(15) NOT NULL;
desc Employees;

ALTER TABLE Employees MODIFY EmpName VARCHAR(100);
desc Employees;

ALTER TABLE Departments DROP PRIMARY KEY;
desc Departments;

ALTER TABLE Departments ADD PRIMARY KEY (DeptID);
ALTER TABLE Employees ADD DeptID INT;
ALTER TABLE Employees ADD CONSTRAINT fk_emp_dept FOREIGN KEY (DeptID) REFERENCES Departments(DeptID);
SHOW CREATE TABLE Employees;


ALTER TABLE Employees RENAME COLUMN EmpName TO EmployeeName;
desc Employees;

ALTER TABLE Employees ADD Age INT;
ALTER TABLE Employees 
ADD CONSTRAINT chk_emp_salary CHECK (Salary > 0),
ADD CONSTRAINT chk_emp_age CHECK (Age >= 18);
desc Employees;
SHOW CREATE TABLE Employees;

ALTER TABLE Employees DROP COLUMN Phone;
desc Employees;

RENAME TABLE Employees TO EmployeeDetails;
desc EmployeeDetails;


ALTER TABLE EmployeeDetails DROP CHECK chk_emp_salary;
ALTER TABLE EmployeeDetails DROP CHECK chk_emp_age;
SHOW CREATE TABLE EmployeeDetails;



DROP TABLE Departments;

DROP DATABASE CompanyDB;