import kagglehub 
from pathlib import Path
import shutil

def run_download_data():
    path = Path(kagglehub.dataset_download("olistbr/brazilian-ecommerce"))
    destiny = Path("data/raw")
    destiny.mkdir(parents=True,exist_ok=True)
   
    for file in path.iterdir():
        if file.is_file():
            shutil.copy(file,destiny/file.name)

