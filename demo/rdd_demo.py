# -*- coding: UTF-8 -*-
from pyspark.sql import SparkSession
from operator import *
import os
os.environ['HADOOP_USER_NAME'] = 'hdfs'

spark = SparkSession \
    .builder \
    .appName("A") \
    .master("local[*]") \
    .enableHiveSupport()\
    .config("hive.exec.dynamic.partition.mode", "nonstrict")\
    .getOrCreate()

"""----------------------------从hdfs读取csv文件进行处理生成对应df，使用sql语句进行分区插入表--------------------------"""
# df = spark.sparkContext.textFile("devnode1:///data/AML/web/file/upload/16_TB_CUST.csv")\
#         .map(lambda x: x.split("|")).map(lambda x: list(x)).toDF(["id", "status", "keyword"])
# # df.createOrReplaceTempView("tab")
# df.show()
# spark.sql("insert overwrite table pay.t_user partition (status,keyword) select id,status,keyword from tab distribute by (status,keyword)")


"""-----------------------------------------------词频统计操作-------------------------------------------------------"""
rdd = spark.sparkContext.parallelize(["Hello hello", "Hello New York", "York says hello"])
# print(rdd.collect())

resultRDD = (rdd.flatMap(lambda sentence: sentence.split(" "))
             .map(lambda word: word.lower())
             .map(lambda word: (word, 1))  # 将word映射成(word,1)
             .reduceByKey(add))  # reduceByKey对所有有着相同key的items执行reduce操作
# resultRDD = (rdd.flatMap(lambda sentence: sentence.split(" "))
#              .map(lambda word: word.lower())
#              .map(lambda word: (word, 1))  # 将word映射成(word,1)
#              .reduceByKey(lambda x, y: x + y))
print(resultRDD.collect())

"测试map与flatMap"
# rdd0 = rdd.flatMap(lambda sentence: sentence.split(" "))\
#              .map(lambda word: word.lower())
# print(rdd0.collect())
# rdd00 = rdd.map(lambda sentence: sentence.split(" "))
# print(rdd00.collect())

result = resultRDD.collectAsMap()
print(result)

print(resultRDD.sortByKey(ascending=True).collect())

spark.stop()