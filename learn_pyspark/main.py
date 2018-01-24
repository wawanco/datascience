import os
from pyspark import SparkContext, SparkConf


def main():
    # Spark Configurations
    conf = SparkConf()
    conf.set("spark.master", "local[*]")
    conf = conf.setAppName('Learning PySpark')
    sc = SparkContext(conf=conf)
    df = sc\
        .textFile('IXQ_20170622080001.csv')\
        .map(lambda line: line.split(','))
    print(df.take(5))


if __name__ == "__main__":
    main()