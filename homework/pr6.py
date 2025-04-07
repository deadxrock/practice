import pandas as pd
data = {
    'Ім\'я': [' Марія', ' Максим', 'Ліза', 'Костянтин', 'Поліна'],
    'Зріст': [175, 180, 165, 170, 178],
    'Вага': [63, 88, 61, 76, 80]
}
df = pd.DataFrame(data, index=['A', 'B', 'C', 'D', 'E'])

print("Початковий датафрейм:")
print(df)

df_sorted_by_height = df.sort_values(by='Зріст')# Сортування за зростанням зросту

print("\nДатафрейм, відсортований за зростанням зросту:")
print(df_sorted_by_height)

df_sorted_by_weight = df.sort_values(by='Вага', ascending=False)# Сортування за спаданням ваги

print("\nДатафрейм, відсортований за спаданням ваги:")
print(df_sorted_by_weight)
