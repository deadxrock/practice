import pandas as pd
data = {
    'ПІБ': ['Анна', 'Богдан', 'Віктор', 'Дарина', 'Євген'],
    'Зріст': [165, 180, 175, 160, 170],  # Зріст у сантиметрах
    'Вага': [55, 85, 75, 60, 90]         # Вага у кілограмах
}
df = pd.DataFrame(data, index=['A', 'B', 'C', 'D', 'E'])# Створюємо DataFrame з індексами - символами абетки

print("Початковий DataFrame:")
print(df)

max_weight_index = df['Вага'].idxmax()
df_dropped = df.drop(max_weight_index) # Вилучаємо цей рядок

print("\nОновлений DataFrame (після вилучення):")
print(df_dropped)
