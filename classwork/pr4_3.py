import pandas as pd
names = ['Анна', 'Богдан', 'Віктор', 'Дарина', 'Євген']
grades = [88, 75, 90, 85, 78]
names_series = pd.Series(names)# Створюємо Series з іменами та оцінками
grades_series = pd.Series(grades)

print("Перші три студенти:")
print(names_series.head(3))

max_grade_index = grades_series.idxmax()  # Знаходимо індекс студента з найвищою оцінкою
max_grade_name = names_series[max_grade_index]
max_grade_value = grades_series[max_grade_index]
print(f"\nСтудент з найвищою оцінкою: {max_grade_name}: {max_grade_value}")

average_grade = grades_series.mean()
print(f"\nСередня оцінка групи: {average_grade:.2f}")
