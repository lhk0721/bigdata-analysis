import pyspark

def main():
    conf = pyspark.SparkConf()
    spark = (
        pyspark.sql.SparkSession.builder
        .master('local')
        .appName('myApp')
        .config(conf=conf)
        .getOrCreate()
    )
if __name__ == "__main__":
    main()