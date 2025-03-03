import numpy as np
array = np.random.uniform(1, 4, (3, 5))
print("Масив:")
print(array)
column_sums = np.sum(array, axis=0)
max_column_index = np.argmax(column_sums)
print("Суми елементів по стовпчиках:")
print(column_sums)
print(f"Номер стовпчика з максимальною сумою: {max_column_index}")
