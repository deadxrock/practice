import torch
tensor_a = torch.rand((5, 5))
tensor_b = torch.rand((5, 5))

mask = tensor_a > tensor_b #маска, яка буде True для елементів першого тензора, які більші за елементи другого тензора

masked_tensor = torch.where(mask, tensor_a, torch.tensor(0.0))# застосування маски до першого тензора, щоб замінити елементи, які не відповідають умові, на 0
print("Перший тензор (tensor_a):")
print(tensor_a)
print("\nДругий тензор (tensor_b):")
print(tensor_b)
print("\nМаска (True для елементів, які більші):")
print(mask)
print("\nТензор після маскування (masked_tensor):")
print(masked_tensor)
