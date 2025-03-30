import pandas as pd
data = pd.Series(range(50))  #Створюємо масив Series з цілих чисел
even_numbers = data[data % 2 == 0]
even_numbers_list = even_numbers.tolist()

print(even_numbers_list)