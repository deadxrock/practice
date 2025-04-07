import torch
random_tensor = torch.rand((10, 5))
mean_value = random_tensor.mean() #обчислення середнього значення тензора
filtered_tensor = random_tensor[random_tensor > mean_value]#усі елементи > середнє значення

print("Випадковий тензор:")
print(random_tensor)
print("\nСереднє значення тензора:")
print(mean_value.item()) 
print("\nНовий тензор, що містить лише елементи, які перевищують середнє значення:")
print(filtered_tensor)
