from pyspark.sql import SparkSession

def get_spark():
    return (
        SparkSession.builder
        .appName("OlistPipeline")
        .config("spark.sql.shuffle.partitions","4")
        .getOrCreate()
    )