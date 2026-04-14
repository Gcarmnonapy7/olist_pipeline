from utils.spark import get_spark
from pyspark.sql.functions import col,to_timestamp,datediff
import os

BRONZE = "data/bronze"
SILVER = "data/silver"

def transform():
    spark = get_spark()
    os.makedirs(SILVER,exist_ok=True)
    
    orders = spark.read.parquet(BRONZE + "olist_orders_dataset")
    items = spark.read.parquet(BRONZE + "")
    customers = spark.read.parquet()
    products = spark.read.parquet()
    payments = spark.read.parquet()
    
    df = (
        orders
        .join(items,"order_id")
        .join(customers,"")
    )
    
    