from utils.spark import get_spark
import os 
from numba import jit
import time

RAW = "data/raw/"
BRONZE = "data/bronze/"

@jit(nopython=True) # Just in time (compiler that makes python functions run at C like speed.)
def ingest():
    
    spark = get_spark()
    os.makedirs(BRONZE,exist_ok=True)
    
    files = [
        "olist_orders_dataset.csv",
        "olist_order_items_dataset.csv",
        "olist_customers_dataset.csv",
        "olist_products_dataset.csv",
        "olist_order_payments_dataset.csv"
    ]
    
    for file in files: 
        df = spark.read.csv(RAW + file,header=True,inferSchema=True)
        
        name = file.replace("csv","")
        
        df.write.mode("overwrite").parquet(BRONZE + name)
        
        print(f" Ingested {file}")
    