import pandas as pd
import matplotlib.pyplot as plt

# load dataset
df = pd.read_csv("../data/WA_Fn-UseC_-HR-Employee-Attrition.csv")

# show first 5 rows
print(df.head())

# remove duplicate rows
df = df.drop_duplicates()

# clean column names
df.columns = df.columns.str.lower()

# replace spaces with underscore
df.columns = df.columns.str.replace(" ", "_")

# save cleaned dataset
df.to_csv("../data/hr_cleaned.csv", index=False)

print("Cleaned dataset saved successfully")

# dataset shape
print("Rows and Columns:", df.shape)

# missing values
print("\nMissing Values:\n")
print(df.isnull().sum())

# total employees
print("\nTotal Employees:")
print(df.shape[0])

# attrition count
print("\nAttrition Count:")
print(df['attrition'].value_counts())

# average salary
print("\nAverage Salary:")
print(df['monthlyincome'].mean())

# department wise employee count
print("\nDepartment Wise Employees:")
print(df['department'].value_counts())

# attrition rate
attrition_rate = (
    df[df['attrition'] == 'Yes'].shape[0]
    / df.shape[0]
) * 100

print("\nAttrition Rate:")
print(round(attrition_rate, 2), "%")

# department wise employee count chart

dept_count = df['department'].value_counts()

plt.figure(figsize=(8,5))
dept_count.plot(kind='bar')

plt.title("Department Wise Employee Count")
plt.xlabel("Department")
plt.ylabel("Number of Employees")

plt.show()

# attrition by department

attrition_dept = df[df['attrition'] == 'Yes']['department'].value_counts()

plt.figure(figsize=(8,5))
attrition_dept.plot(kind='bar')

plt.title("Attrition by Department")
plt.xlabel("Department")
plt.ylabel("Employees Left Company")

plt.show()

# salary distribution chart

plt.figure(figsize=(8,5))

plt.hist(df['monthlyincome'], bins=20)

plt.title("Salary Distribution")
plt.xlabel("Monthly Income")
plt.ylabel("Number of Employees")

plt.show()

# overtime vs attrition

overtime_attrition = pd.crosstab(
    df['overtime'],
    df['attrition']
)

print("\nOvertime vs Attrition:\n")
print(overtime_attrition)

overtime_attrition.plot(kind='bar', figsize=(8,5))

plt.title("Overtime vs Attrition")
plt.xlabel("Overtime")
plt.ylabel("Employee Count")

plt.show()

# employee age distribution

plt.figure(figsize=(8,5))

plt.hist(df['age'], bins=15)

plt.title("Employee Age Distribution")
plt.xlabel("Age")
plt.ylabel("Number of Employees")

plt.show()

# gender distribution chart

gender_count = df['gender'].value_counts()

plt.figure(figsize=(6,5))

gender_count.plot(kind='bar')

plt.title("Gender Distribution")
plt.xlabel("Gender")
plt.ylabel("Number of Employees")

plt.show()

# average salary by department

avg_salary = df.groupby('department')['monthlyincome'].mean()

print("\nAverage Salary by Department:\n")
print(avg_salary)

plt.figure(figsize=(8,5))

avg_salary.plot(kind='bar')

plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Monthly Income")

plt.show()

# job role wise attrition

job_attrition = (
    df[df['attrition'] == 'Yes']
    ['jobrole']
    .value_counts()
)

print("\nJob Role Wise Attrition:\n")
print(job_attrition)

plt.figure(figsize=(10,5))

job_attrition.plot(kind='bar')

plt.title("Job Role Wise Attrition")
plt.xlabel("Job Role")
plt.ylabel("Employees Left Company")

plt.xticks(rotation=45)

plt.show()

# work life balance vs attrition

worklife_attrition = pd.crosstab(
    df['worklifebalance'],
    df['attrition']
)

print("\nWork Life Balance vs Attrition:\n")
print(worklife_attrition)

worklife_attrition.plot(kind='bar', figsize=(8,5))

plt.title("Work Life Balance vs Attrition")
plt.xlabel("Work Life Balance Rating")
plt.ylabel("Employee Count")

plt.show()

# export final cleaned dataset

df.to_csv("../data/hr_final_cleaned.csv", index=False)

print("\nFinal cleaned dataset exported successfully")