import pandas as pd

names = ['Анна', 'Богдан', 'Віктор', 'Дарина', 'Євген']
grades = [88, 75, 90, 85, 78]
df = pd.DataFrame({
    'Імена': names,
    'Оцінки': grades
})

print("Перші три студенти:")
print(df.head(3))

max_grade_index = df['Оцінки'].idxmax()  # Знаходимо індекс студента з найвищою оцінкою
max_grade_name = df.loc[max_grade_index, 'Імена']
max_grade_value = df.loc[max_grade_index, 'Оцінки']
print(f"\nСтудент з найвищою оцінкою: {max_grade_name}: {max_grade_value}")
average_grade = df['Оцінки'].mean()

print(f"\nСередня оцінка групи: {average_grade:.2f}")
