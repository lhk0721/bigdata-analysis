import pyspark, os
import pandas as pd

def sparkSession():
    conf = pyspark.SparkConf()
    spark = (
        pyspark.sql.SparkSession.builder
        .master('local')
        .appName('myApp')
        .config(conf=conf)
        .getOrCreate()
    )
    
def convertCsvEncoding(filename):
    os.system(
    f"cp '/mnt/c/Users/neighbor/Downloads/{filename}.csv' ~/env3.9/bin/data"
    )
    df = pd.read_csv(
        f'data/{filename}.csv',
        encoding = 'cp949'
       )
    df.to_csv(
        f'data/{filename}_utf-8.csv', 
        encoding = 'utf-8',
        index = False
    )
    print(f'data/{filename}_utf-8.csv')

def textFile(filename):
    Rdd = (
        spark
        .sparkContext
        .textFile(
            os.path.join(
                'data',
                f'{filename}.csv'
            )
        )   
    )

def binaryFiles(filename):
    Rdd = (
        spark
        .sparkContext
        .binaryFiles(
            os.path.join(
                'data'
                f'{filename}.csv'
            )
        )
    )
    
def dataFrame(filename):
    Df = (
        spark.read
        .option('charset', 'utf-8')
        .option('header', 'true')
        .csv(
            os.path.join(
                'data',
                f'{filename}.csv'
            )
        )
    )
