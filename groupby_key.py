def groupby_key(_list):
    Rdd = (
        spark.sparkContext.parallelize(
            _list
        )
    )
    Rdd2 = (
        Rdd.groupBy(
            lambda x:x[0]
        )
        .mapValues(
            lambda x:list(x)
        )
        .collect()
    )

if __name__ == '__main__':
    groupby_list()
