SELECT employeenumber,
       department,
       monthlyincome,
       RANK() OVER (
           PARTITION BY department
           ORDER BY monthlyincome DESC
       ) AS salary_rank
FROM employees;
SELECT employeenumber,
       department,
       monthlyincome,
       DENSE_RANK() OVER (
           PARTITION BY department
           ORDER BY monthlyincome DESC
       ) AS salary_rank
FROM employees;
SELECT employeenumber,
       department,
       monthlyincome,
       ROW_NUMBER() OVER (
           PARTITION BY department
           ORDER BY monthlyincome DESC
       ) AS row_num
FROM employees;
CREATE VIEW attrition_employees AS
SELECT *
FROM employees
WHERE attrition = 'Yes';
SELECT *
FROM attrition_employees;
CREATE VIEW high_salary_employees AS
SELECT employeenumber,
       department,
       jobrole,
       monthlyincome
FROM employees
WHERE monthlyincome > 10000;
SELECT *
FROM high_salary_employees;
CREATE VIEW department_salary_summary AS
SELECT department,
       ROUND(AVG(monthlyincome), 2) AS avg_salary,
       COUNT(*) AS total_employees
FROM employees
GROUP BY department;
SELECT *
FROM department_salary_summary;