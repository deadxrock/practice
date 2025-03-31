import pandas as pd
customers = pd.DataFrame({
    "customer_id": range(1, 11),
    "name": ["Anna", "Oleg", "Maria", "Ivan", "Olena", "Petro", "Dmytro", "Nina", "Serhii", "Viktoria"],
    "age": [25, 40, 35, 50, 28, 33, 38, 45, 30, 42],
    "city": ["Kyiv", "Lviv", "Odesa", "Dnipro", "Kharkiv", "Lviv", "Kyiv", "Odesa", "Kharkiv", "Dnipro"],
    "purchases": [5, 2, 7, 3, 4, 6, 1, 8, 5, 3]
})
customers
average_age = customers['age'].mean()

city_counts = customers['city'].value_counts()#Визначити, в якому місті найбільше клієнтів
most_common_city = city_counts.idxmax()
most_common_city_count = city_counts.max()

frequent_customers = customers[customers['purchases'] > 3]#Відфільтрувати клієнтів, які зробили більше 3 покупок

print(f"Середній вік клієнтів: {average_age:.2f}")
print(f"Місто з найбільшою кількістю клієнтів: {most_common_city} (кількість: {most_common_city_count})")
print("\nКлієнти, які зробили більше 3 покупок:")
print(frequent_customers)