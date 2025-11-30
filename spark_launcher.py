import pyspark

spark = None

def start():
    global spark
    
    print('Opening SparkSession... please wait.\n')
    
    try:
        conf = pyspark.SparkConf()
        spark = (
            pyspark.sql.SparkSession.builder
            .master('local')
            .appName('myApp')
            .config(conf=conf)
            .getOrCreate()
        )
    
        print('Spark Version:\t\t', spark.version)
        print('SparkSession available:\t', spark.sparkContext._jsc is not None, '\n')
    
    except Exception as e:
        print('SparkSession failed to start.')
        print('Error:', e)


def stop():
    global spark
    
    if spark is None:
        print('Error: SparkSession not started.')
        return

    # sparkSession이 살아 있지만 이미 내부 context가 죽은 경우 처리
    try:
        _jsc_alive = spark.sparkContext._jsc is not None
    except:
        _jsc_alive = False

    if not _jsc_alive:
        print('Error: SparkSession already stopped.')
        return

    spark.stop()
    print('SparkSession stopped.')


def main():
    start()


if __name__ == '__main__':
    main()
