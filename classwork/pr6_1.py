import pandas as pd

sales = pd.DataFrame({
    "order_id": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    "date": pd.to_datetime(["2024-03-10", "2024-03-11", "2024-03-12", "2024-03-13", "2024-03-14",
                            "2024-03-15", "2024-03-16", "2024-03-17", "2024-03-18", "2024-03-19"]),
    "product": ["Laptop", "Phone", "Tablet", "Laptop", "Phone", "Laptop", "Tablet", "Phone", "Tablet", "Laptop"],
    "quantity": [2, 5, 3, 1, 2, 3, 4, 1, 5, 2],
    "price": [1200.0, 600.0, 800.0, 1500.0, 650.0, 1400.0, 850.0, 620.0, 900.0, 1300.0],
    "customer": ["Ivanov", "Petrov", "Sidorov", "Kozlov", "Smirnov", "Fedorov", "Titov", "Orlov", "Belov", "Nikolaev"],
    "region": ["East", "West", "North", "South", "East", "North", "West", "South", "East", "West"]
})
sales
sales['total_price'] = sales['quantity'] * sales['price']

# 2. Визначити, який товар приніс найбільше доходу
total_revenue_per_product = sales.groupby('product')['total_price'].sum()
highest_revenue_product = total_revenue_per_product.idxmax()
highest_revenue_value = total_revenue_per_product.max()

# 3. Порахувати, скільки було продано товарів у кожному регіоні
total_quantity_per_region = sales.groupby('region')['quantity'].sum()

# Виведення результатів
print("DataFrame з новим стовпцем total_price:")
print(sales)
print("\nТовар, який приніс найбільше доходу:")
print(f"{highest_revenue_product} з доходом {highest_revenue_value}")
print("\nКількість проданих товарів у кожному регіоні:")
print(total_quantity_per_region)