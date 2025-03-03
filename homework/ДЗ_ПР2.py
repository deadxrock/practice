import numpy as np
array = np.random.randint(1, 101, size=10)
print("Масив:", array)
odd_elements = array[array % 2 != 0]
if odd_elements.size > 0:
    max_odd = np.max(odd_elements)
    min_odd = np.min(odd_elements)
    count_max_odd = np.sum(odd_elements == max_odd)
    count_min_odd = np.sum(odd_elements == min_odd)

    print("Найбільший непарний елемент:", max_odd)
    print("Найменший непарний елемент:", min_odd)
    print("Кількість найбільших непарних елементів:", count_max_odd)
    print("Кількість найменших непарних елементів:", count_min_odd)
else:
    print("Немає непарних елементів у масиві.")
