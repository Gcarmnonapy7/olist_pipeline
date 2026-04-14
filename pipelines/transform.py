from utils.spark import get_spark
from pyspark.sql.functions import col,to_timestamp,datediff
import os

BRONZE = "data/bronze"
SILVER = "data/silver"

def transform():
    spark = get_spark()
    os.makedirs(SILVER,exist_ok=True)
    
    
    