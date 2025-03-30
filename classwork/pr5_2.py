import pandas as pd

data = {
    'ПІБ': ['Анна', 'Богдан', 'Віктор', 'Дарина', 'Євген'],
    'Зріст': [165, 180, 175, 160, 170], 
    'Вага': [55, 85, 75, 60, 90] 
}
df = pd.DataFrame(data, index=['A', 'B', 'C', 'D', 'E'])

print("Початковий DataFrame:")
print(df)

threshold_weight = 55 # Задане значення ваги
count_above_threshold = (df['Вага'] > threshold_weight).sum()# Обчислюємо кількість рядків, в яких вага більше заданої

print(f"\nКількість рядків, в яких вага більше {threshold_weight}: {count_above_threshold}")
