import pandas as pd
import numpy as np
data = pd.Series(np.random.randint(51, 100, size=10))
mean_value = data.mean() # Обчислюємо середнє арифметичне
greater_than_mean = data[data > mean_value]
greater_than_mean_series = pd.Series(greater_than_mean) # Переписуємо їх в інший масив Series

print("Оригінальний масив:")
print(data)
print("\nСереднє арифметичне:", mean_value)
print("\nЧисла, що більше за середнє арифметичне:")
print(greater_than_mean_series)
