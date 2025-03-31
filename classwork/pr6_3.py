import pandas as pd
employees = pd.DataFrame({
    "id": range(1, 11),
    "name": ["Ivan", "Oksana", "Petro", "Olena", "Dmytro", "Nina", "Serhii", "Oleg", "Anna", "Viktoria"],
    "department": ["IT", "HR", "IT", "Finance", "HR", "Finance", "IT", "HR", "Finance", "IT"],
    "salary": [5000.0, None, 6000.0, 7000.0, None, 6500.0, 7200.0, 4800.0, None, 5500.0],
    "experience": [5, 3, None, 10, 2, 8, 6, None, 4, 7]
})
employees['salary'] = employees.groupby('department')['salary'].transform(lambda x: x.fillna(x.mean()))

employees['experience'] = employees['experience'].fillna(employees['experience'].median())# Заповнити пропущені значення в experience медіаною

average_salary_per_department = employees.groupby('department')['salary'].mean()# Визначити відділ із найвищою середньою зарплатою
highest_salary_department = average_salary_per_department.idxmax()
highest_salary_value = average_salary_per_department.max()

print("DataFrame після обробки пропущених значень:")
print(employees)
print(f"\nВідділ із найвищою середньою зарплатою: {highest_salary_department} (середня зарплата: {highest_salary_value:.2f})")
