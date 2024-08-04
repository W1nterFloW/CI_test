import sys
sys.path.append('../')
print("Hello, World!")
import torch
print(torch.tensor([1,2,3,4]))
print(torch.cuda.is_available())

from a import func
print(func(1, 5))