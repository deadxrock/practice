import numpy as np
array = np.random.randint(2, 11, size=5)
print("Масив:", array)
less_than_6 = np.sum(array < 6)
print("Кількість чисел менших за 6:",less_than_6)
count_between_5_and_8 = int(np.sum((array>5)&(array<8)))
print("Кількість чисел в діапазоні від 5 до 8:", count_between_5_and_8)
