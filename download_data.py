import kagglehub 
import os
import shutil
from numba import njit

path = kagglehub.dataset_download("olistbr/brazilian-ecommerce")
print("Path to dataset files:", path)

# Path to move 
DESTINY = "data/raw/"
os.makedirs(DESTINY,exist_ok=True)

for file in os.listdir(path):
    shutil.copy()