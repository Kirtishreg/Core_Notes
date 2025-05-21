# Databricks notebook source

#Type 1 
# #considering the unstructured data
#Working on word count problem finding out the number of lines,occurances,words .... in  the file  the spark solution
#the entry point for an given program is Spark Context it will invokes the cluster to start
from pyspark import SparkContext,SparkConf
sc=SparkContext.getOrCreate()# starting the cluster
lines=sc.textFile("dbfs:/FileStore/usa.txt")# reading the file
lines.take(50) #take(n) it will reads the  number of lines  
#splitting with respect to space 
words=lines.flatMap(lambda x:x.split(' '))#SPLITTING
words.take(20)
wcnt=words.map(lambda x:(x.lower(),1))# mapping 
wcnt.take(20)
cnts=wcnt.reduceByKey(lambda x,y:x+y)# shuffling and using the reduce by  and give the merging info
cnts.take(20)
#stop watch mean filter not to take some words or chars how to filter
stop=[' ','the','and','is','in','an','of']
words_short=cnts.filter(lambda x:x[0] not in stop)
words_short.top(20,lambda x:x[1])
numbers_only=wcnt.groupByKey().map(lambda x:sum(x[1]))
numbers_only.take(20)
#to find the total words in the passenge or file 
total_words=numbers_only.reduce(lambda x,y:x+y)
print(total_words)




# COMMAND ----------



# COMMAND ----------

from pyspark import SparkContext,SparkConf
sc=SparkContext.getOrCreate()# starting the cluster
lines=sc.textFile("dbfs:/FileStore/apple.txt")# reading the file
lines.take(20) #take(n) it will reads the  number of lines  
#splitting the data with respect to space 
words=lines.flatMap(lambda x:x.split(' '))#flat map function takes the lambda function and prints the element word by word
words.take(20)


# COMMAND ----------

wcnt=words.map(lambda x:(x.lower(),1))
wcnt.take(20)

# COMMAND ----------

cnts=wcnt.reduceByKey(lambda x,y:x+y)
cnts.take(10)


# COMMAND ----------

#structured data  type 1 
import pyspark
from pyspark.sql.types import DoubleType,StringType,StructType,StructField
from pyspark.sql.functions import col,to_date
obj=pyspark.sql.SparkSession.builder.appName("Sqlfirsttype").getOrCreate()
df=obj.read.csv("dbfs:/FileStore/tables/emp-1.csv",inferSchema=True,header=True,sep=",").cache()
df.show()


# COMMAND ----------

#structured data  type 2 way  the data will be provided in a list manner 
import pyspark
from pyspark.sql.types import DoubleType,StringType,StructType,StructField
from pyspark.sql.functions import col,to_date
obj=pyspark.sql.SparkSession.builder.appName("Sqltype2").getOrCreate()
df=obj.read.csv("dbfs:/FileStore/tables/emp-1.csv",header=True,sep=",")
df.take(5)

# COMMAND ----------

#structured data  type 3 way  the data will be provided in a semi structured  manner  mean json,avro,xml,...
import pyspark
from pyspark.sql.types import DoubleType,StringType,StructType,StructField
from pyspark.sql.functions import col,to_date
obj=pyspark.sql.SparkSession.builder.appName("Sqltype2").getOrCreate()
df=obj.read.json("dbfs:/FileStore/Sample___Superstorejson.json")
df.take(5)

# COMMAND ----------

#structured data  type 4 way  the data will be provided in a ROW AND WE need to use DataFrame
import pyspark
from pyspark.sql import SparkSession,Row
from pyspark.sql.types import DoubleType,StringType,StructType,StructField
from pyspark.sql.functions import col,to_date
obj=pyspark.sql.SparkSession.builder.appName("Sqltype4").getOrCreate()
df=obj.createDataFrame
([ 
    Row(prodno='1',pname='computer',qty='900',price='900'),
    Row(prodno='2',pname='headphones',qty='165',price='123'),
    Row(prodno='3',pname='pendrive',qty='55',price='98'),
    Row(prodno='4',pname='HDD',qty='25',price='79'),
    Row(prodno='5',pname='mouse',qty='67',price='65'),
    Row(prodno='6',pname='washing machine',qty='39',price='35'),
    Row(prodno='7',pname='ac',qty='50',price='56'),
    Row(prodno='8',pname='fan',qty='11',price='51'),
    Row(prodno='9',pname='pen',qty='17',price='12'),
    Row(prodno='10',pname='mobile',qty='66',price='44')
])

# COMMAND ----------

#type 5 form where the data will be provided seperately data and columns are different here 
# we can use parallelize 

import pyspark 
from pyspark import SparkContext,SparkConf
from pyspark.sql import SparkSession,Row
from pyspark.sql.types import DoubleType,StringType,StructType,StructField
from pyspark.sql.functions import col,to_date
sc=SparkContext.getOrCreate()
data=sc.parallelize([
(1,'computer',900,900),
(2,'headphones',165,123),
(3,'pendrive',55,98),
(4,'HDD',25,79),
(5,'mouse',67,65),
(6,'washing machine',39,35),
(7,'ac',50,56),
(8,'fan',11,51),
(9,'pen',17,12),
(10,'mobile',66,44) 
])
df=spark.createDataFrame(data,["prodno","pname","qty","price"])
df.show()

# COMMAND ----------






#type 6
import pyspark
from pyspark.sql import SparkSession,Row
from pyspark.sql.types import DoubleType,StringType,StructType,StructField,IntegerType
from pyspark.sql.functions import col,to_date
obj=pyspark.sql.SparkSession.builder.appName("Sqltype6").getOrCreate()
data=[(1,'computer',900,900),(2,'headphones',165,123),(3,'pendrive',55,98),(4,'HDD',25,79),(5,'mouse',67,65),(6,'washing machine',39,35),
(7,'ac',50,56),(8,'fan',11,51),(9,'pen',17,12),(10,'mobile',66,44)]
schema=StructType([
    StructField("prodno",IntegerType(),True),
    StructField("prodname",StringType(),True),
    StructField("qty",IntegerType(),True),
    StructField("price",IntegerType(),True),
])
df=obj.createDataFrame(data,schema)
df.show()

# COMMAND ----------

#type 6(1)
import pyspark
from pyspark.sql import SparkSession,Row
from pyspark.sql.types import DoubleType,StringType,StructType,StructField,IntegerType
from pyspark.sql.functions import col,to_date
obj=pyspark.sql.SparkSession.builder.appName("Sqltype6_1").getOrCreate()
data=[
    (("SanathReddy","Aitha"),100,"M",10000),
    (("Smika","N"),101,"F",11111),
    (("Keerthi",""),102,"F",12121),
    (("Manu","Nair"),103,"M",13131),
   (("Harsha","Reddy"),104,"M",1111133)
]
schema=StructType([
            StructField("Fullname",StructType([
                    StructField("FirstName",StringType(),True),
                    StructField("LastName",StringType(),True)
                    ])),
    StructField("empno",IntegerType(),True),
    StructField("gender",StringType(),True),
    StructField("salary",IntegerType(),True),   
])
df=obj.createDataFrame(data,schema)
df.show()

# COMMAND ----------

#lhow to read the data if it is given AVRO,PARQUEST,XML....
"""Apache Avro is a row-based data serialization format that encodes data in a compact binary format.
Avro stores both the data definition and the data together in one message or file.
Avro stores the schema in JSON format alongside the data, enabling efficient processing and schema evolution.
Avro is a row-primarily based garage format optimized for write operations and schema evolution, while Parquet is a columnar storage layout designed for read-heavy operations and analytics, offering efficient information compression and retrieval."""

import pyspark
from pyspark.sql.types import DoubleType,StringType,StructType,StructField
from pyspark.sql.functions import col,to_date
obj=pyspark.sql.SparkSession.builder.appName("Sqltype2").getOrCreate()
df=obj.read.format("avro").load("dbfs:/FileStore/userdata1.avro")

df.show()

# COMMAND ----------

df=obj.read.format("parquet").load("dbfs:/FileStore/userdata1.parquet")
df.show()

# COMMAND ----------

import pyspark
from pyspark.sql.types import DoubleType,StringType,StructType,StructField
from pyspark.sql.functions import col,to_date
obj=pyspark.sql.SparkSession.builder.appName("Sqlfirsttype").getOrCreate()
df=obj.read.csv("dbfs:/FileStore/tables/emp-1.csv",inferSchema=True,header=True,sep=",").cache()
df.show()
#print(" number of partition currently are ",str(sc.getNumPartitions()))

# COMMAND ----------

#dataframe[columnname].conditionalstatement
#df.show()
#df.tail(2)
#df.head(2)
#df.summary().show()
#df.select("*").show()
#df.select("sal").show()
#df.select(df.sal).show()
#df.select(df.sal*2.5).show()
#df.select(df.empno,df.ename,df.sal,df.comm,df.sal*2.5).show()
#df.select("empno","ename","sal","comm","sal*2.5").show()
#df.show(vertical=True)
#df.show()
#df.take(50)
#df.collect()
#how to use where clause
#df.where(df.sal>=2000).show()
#df.where(df.sal<=2000).show()
#df.where(df.job=='CLERK').show()
#df.where(df.job=='CLERK') or df.where(df.job=='ANALYST').show()
#filter
#df.filter(df.job=='CLERK').filter(df.job=='ANALYST').show()
#df.filter(df.job=='CLERK').show()
#df.filter(df.sal<=2000).show()
#df.filter(df.job=='CLERK').filter(df.deptno==20).show()
#like operator
#df.filter(df.ename.startswith("S")).show()# names which are starting with S
#df.filter(df.ename.endswith("S")).show()# names which are starting with S
#df[df.ename.like("S%")].show()
#df[(df.ename.like("S%")) | (df.ename.like("%S"))].show()
#df.where(df.sal>=1000) and df.where(df.sal<=2000).show()
#df.select(df.ename,df.sal.between(1000,2000)).show()
#df.filter((df.sal<=2000)).show()
#df.filter(~(df.sal<=2000)).show()
#df.filter(^(df.sal<=2000)).show()

# COMMAND ----------

import pyspark
from pyspark import SparkContext,SparkConf
from pyspark.sql.types import DoubleType,StringType,StructType,StructField
from pyspark.sql import Row,SparkSession
sobj=pyspark.sql.SparkSession.builder.appName("Sqlaaa2").getOrCreate()
sc=SparkContext.getOrCreate()
df1=sc.parallelize([10,20,30,40,50,"apple","mango"])
df2=sc.parallelize([10,20,130,140,50,"pineapple","mango"])
data3=data1.union(data2)
data4=data1.intersection(data2)
print(data1.collect())
print(data2.collect())
print(data3.collect())
print(data4.collect())


# COMMAND ----------

import pyspark 
from pyspark import SparkContext,SparkConf
from pyspark.sql import SparkSession,Row
from pyspark.sql.types import DoubleType,StringType,StructType,StructField
from pyspark.sql.functions import col,to_date
sc=SparkContext.getOrCreate()
data1=sc.parallelize([
(None,'computers',9010,9020),
(1,'computer',900,900),
(2,'headphones',165,123),
(None,'computers',9010,9020),
(1,'computer',900,900),
(2,'headphones',165,123),
(None,'pendrive',55,98),
(4,'HDD',25,79),
(5,'mouse',67,65),
(6,'washing machine',39,35),
(7,'ac',50,56),
(8,'fan',11,51),
(9,'pen',17,12),
(10,'mobile',66,44) 
])
data2=sc.parallelize([
(1,'computer',900,900),
(2,'headphones',165,123),
(3,'pendrive',55,98),
(4,'HDD',25,79),
(55,'mouse',67,65),
(56,'washing machine',39,35),
(57,'ac',50,56),
(58,'fan',11,51),
(59,'pen',17,12),
(510,'mobile',66,44) 
])

df1=spark.createDataFrame(data1,["prodno","pname","qty","price"])
df2=spark.createDataFrame(data2,["prodno","pname","qty","price"])
df1.join(df2,df1.prodno==df2.prodno,"inner").show(truncate=False)
df1.join(df2,df1.prodno==df2.prodno,"outer").show(truncate=False)
df1.join(df2,df1.prodno==df2.prodno,"right").show(truncate=False)
df1.join(df2,df1.prodno==df2.prodno,"left").show(truncate=False)



# COMMAND ----------

"""


coalesce
corr
distinct
dropna
fillna
replace
rollup
"""
df1.show()
#df1.na.replace(1,222).show()
#df1.na.replace("computer","computers").show()
#df1.corr("qty","price")
#df1.distinct().show()
df1.na.drop().show()



# COMMAND ----------

#Aggregate functions min(),max(),avg(),sum().....
#u need to have compulsoryly group function 
from pyspark.sql.functions import row_number,dense_rank,lag,lead,avg,sum,min,max,col,count,lit,rank
from pyspark.sql.window import Window

w=Window.orderBy("job")
df.withColumn("Avgsal",avg(col("sal")).over(w)).show()
df.withColumn("minsal",min(col("sal")).over(w)).show()
df.withColumn("maxsal",max(col("sal")).over(w)).show()
df.withColumn("sumsal",sum(col("sal")).over(w)).show()


# COMMAND ----------

df.createOrReplaceTempView("emptable")#converting the dataframe into a temptable

# COMMAND ----------

# MAGIC %sql
# MAGIC --select * from emptable
# MAGIC select * from emptable where deptno=10
# MAGIC --select sum(sal),deptno from emptable group by deptno
# MAGIC --select min(sal),max(sal),sum(sal),avg(sal) from emptable group by deptno
# MAGIC
# MAGIC

# COMMAND ----------


#spark.sql("select * from emptable").show()
#spark.sql("select * from emptable where deptno=10").show()
#spark.sql("select sum(sal),deptno from emptable group by deptno").show()
spark.sql("select min(sal),max(sal),sum(sal),avg(sal) from emptable group by deptno").show()



# COMMAND ----------

#window functions 

w=Window.orderBy("sal")
#df.withColumn("leadsal",lead("sal",1).over(w)).show()
#df.withColumn("leadsal",lag("sal",1).over(w)).show()
#df.withColumn("denserank",dense_rank().over(w)).show()
#df.withColumn("rank",rank().over(w)).show()
df.withColumn("rownumber",row_number().over(w)).show()

# COMMAND ----------

#Math functions
from pyspark.sql.functions import pow,floor,ceil,sqrt,lit,abs
#df.select(df.sal,sqrt(lit(df.sal))).show()
#df.select(sqrt(lit(df.sal)),floor(sqrt(lit(df.sal))),ceil(sqrt(lit(df.sal)))).show()
#df.select (df.comm-df.sal).show()
#df.select(abs(df.comm-df.sal)).show()
df.select(pow(lit(3),lit(2))).show()


# COMMAND ----------

def myfunc():
    print(" welcome to functions ")

myfunc()


# COMMAND ----------

#when ever u want to use functions we need to call the udf
from pyspark.sql.types import StringType,DoubleType,IntegerType
from pyspark.sql.functions import udf
def sampleempdef(p_sal):
    if(p_sal>0 and p_sal<1500):
        return p_sal-(p_sal*0.02)
    elif (p_sal>=1501 and p_sal<=2500):
        return p_sal-(p_sal*0.05)
    else:
        return p_sal-(p_sal*.25)
    
#udf(functiona,returndatatype)
result=udf(sampleempdef,DoubleType())
# to see the output 
df.withColumn("Result output  after deduction of tax is ",result(df.sal)).show()
#using udf  Manager ----> BOSS,ANALYST I GRADE,CLERK-->3RD GRADE,SALESMAN--->2ND GRADE,OTHERS -->STRINGTYPE 
    



# COMMAND ----------

from pyspark.sql.types import StringType,DoubleType,IntegerType
from pyspark.sql.functions import udf
def sampleempdef(p_deptno):
    if(p_deptno==10):
        return "sales department "
    elif (p_deptno==20):
        return "Purchases Department "
    else:
        return " Other Department"
    
#udf(functioname,returndatatype)
result=udf(sampleempdef,StringType())
# to see the output 
df.withColumn("Dept name is  ",result(df.deptno)).show()
"""
--->names  a-g ist group
h-m iind group
n-z iiird group """



# COMMAND ----------

#ML-->MACHINE LEARNING CONCEPTS train,and test VALIDATION MODELS  


"""Vector Assembler:-  list of columns 2 or more into one single column is termed as Vector Assmebler and the result column is called as Vector.
 The VectorAssembler takes a list of columns as an input and combines them into a single vector column. It is useful for combining various raw as well as generated/transformed features into a single feature vector which then can be used for modeling.

#type 1 form of vectorAssembler if they give only numerical data.
#column vector that we got here is called as 'features '
m1,m2,m3,v(features)
10,20,30,[10,20,30]
#type 2 form of vector Assembler if it consists of bothe numerical and categorical data .
m1,m2,m3,a #INDEXER/ONEHOTENCODER --> TYPE 2 CATOGORICAL MANNER IS GIVEN 
10,20,30,"apple"
20,30,56,"banana"
45,66,77,"grapes"
66,77,88,"gova"
99,88,77,"pineapple"
5,66,77,"apple"
88,87,45,"banana"
10,20,40,"gova"
m1,m2,m3,a,v(features)
10,20,30,"apple",[10,20,30,0]
20,30,56,"banana",[20,30,46,1]
45,66,77,"grapes"[45,66,77,2]
99,88,77,"pineapple",[99,88,77,3]
66,77,88,"gova",[66,77,88,4]
5,66,77,"apple"[5,66,77,0]
88,87,45,"banana"[88,87,45,1]
10,20,40,"gova"[10,20,40,4]


# COMMAND ----------

"""m1,m2,m3,features
12,54,76,[12,54,76]
45,65,78,[45,65,78]
67,88,99,[67,88,99]
45,43,78,[45,43,78]
34,66,77,[34,66,77]
66,77,88,[66,77,88]
45,66,78,[45,66,78]
67,78,89,[67,78,89]
60,60,60,[60,60,60]"""


# COMMAND ----------

"""
#1) part 1 --->vector column/features
2) Modeling
3) apply the formulas 
"""

import pyspark
from pyspark import SparkContext,SparkConf
from pyspark.sql.types import DoubleType,StringType,StructType,StructField
from pyspark.sql import Row,SparkSession
sobj=pyspark.sql.SparkSession.builder.appName("Sqlaaa2").getOrCreate()
#data ingestion

df=obj.createDataFrame([(12,54,76),
                          (45,65,78),
                          (67,88,99),
                          (45,43,78),
                          (34,66,77),
                          (66,77,88),
                          (45,66,78),
                          (67,78,89),
                          (60,60,60)],("sub1","sub2","sub3"))
df.show()

#explanatory data analysis
from pyspark.ml.feature import VectorAssembler
assembler=VectorAssembler(inputCols=["sub1","sub2","sub3"],outputCol="features")
df=assembler.transform(df)
df.show()



# COMMAND ----------

#data ingestion 
import pyspark
from pyspark import SparkContext,SparkConf
from pyspark.sql.types import DoubleType,StringType,StructType,StructField
from pyspark.sql import Row,SparkSession
import numpy as np
from sklearn import metrics
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

obj=pyspark.sql.SparkSession.builder.appName("Sqlaaa2").getOrCreate()
df=obj.read.csv("dbfs:/FileStore/Student_Pass_Fail_Data.csv",inferSchema=True,header=True,sep=",")
df.show()
#step 1 Creating the model dataframe
X=df.drop('Pass_Or_Fail')
y=df['Pass_Or_Fail']
X,y=make_classification()
# 2)split the records  into x train and y train x test and y test models 
X_train,X_test,y_train,y_test=train_test_split(X,y)
#3) now fit the model into the logistic regression()
lr=LogisticRegression()
lr.fit(X_train,y_train)#lr1.fit(X_test,y_test)
#4)Getting the prediction on Test dataset with actual values 
y_pred=lr.predict(X_test)
#5 finding how much accurracy the model is and the values that we got 
accuracy=metrics.accuracy_score(y_test,y_pred)
accuracy_percentage=100*accuracy
accuracy_percentage



# COMMAND ----------

#Decission Tree Classifier :- it present under ML.classification import DecissionTreeClassifier predefined formulas like Gini,Entropy,informationGain were existing. 
#now creating Trainmodel-- the data that u have taken for sampling purpose should be upto 80% of data only
#remaining 20% data will be allocated to the test model.
#TestModel gives how much the accurate the data is 

#The entire DataFrame we will split into two models
#Trainmodeldf,testmodeldf and after spliting  and storing the records into the models 
# taking features column  on x axis and y axis any other column and deriving the results 
"""#fit() method in machine learning 
#fit(x,y): x refers feature matrix where each row represents  a sample and each column represents a feature
# y denotes a target vector containing labels or target values with sample.
rawPrediction is the raw output of the logistic regression classifier (array with length equal to the number of classes)
probability is the result of applying the logistic function to rawPrediction (array of length equal to that of rawPrediction)
prediction is the argument where the array probability takes its maximum value, and it gives the most probable label (single number)
#rawPrediction is equal (w*x + bias) variable coefficients values
#probability is 1/(1+e^(w*x + bias))
#prediction is 0 or 1."""

# COMMAND ----------

#data ingestion 
import pyspark
from pyspark import SparkContext,SparkConf
from pyspark.sql.types import DoubleType,StringType,StructType,StructField
from pyspark.sql import Row,SparkSession
import numpy as np
from sklearn import metrics
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression


obj=pyspark.sql.SparkSession.builder.appName("Sqlaaa2").getOrCreate()
df=obj.read.csv("dbfs:/FileStore/affairs.csv",inferSchema=True,header=True,sep=",")
# explanatory data analysis
#vector assembler we will be using and collecting the entire numerical data into one single column
from pyspark.ml.feature import VectorAssembler
assembler=VectorAssembler(inputCols=["rate_marriage","age","yrs_married","children","religious","affairs"],outputCol="features")
df=assembler.transform(df)
df.show()
# based on affairs  column we are doing the analysis to check the data is accurate or not % how much percent
from pyspark.ml.classification import DecisionTreeClassifier
model_df=df.select(['features','affairs'])# we have stored the data into a model dataframe 
#Now split the data into  train and test models
train_mdf,test_mdf=model_df.randomSplit([.75,.25])
print(" The total number of records in model frame  is ",model_df.count())
print(" The total number of records in model frame  is ",train_mdf.count())
print(" The total number of records in model frame  is ",test_mdf.count())
from pyspark.ml.regression import LinearRegression
lin_reg=LinearRegression(labelCol='affairs')
#using fit with trainging dataset for deriving linear regression analysis
lrmodel=lin_reg.fit(train_mdf)
#Istformula
lrmodel.intercept
print(lrmodel.coefficients)
#calculating the rms,r2,mse values
trainpredictions=lrmodel.evaluate(train_mdf)
testpredictions=lrmodel.evaluate(test_mdf)
print("for Train model below predictions ")
print("MSE",trainpredictions.meanSquaredError,"R2",trainpredictions.r2," RMS ",trainpredictions.rootMeanSquaredError)
print("for Test model below predictions ")
print("MSE",testpredictions.meanSquaredError,"R2",testpredictions.r2," RMS ",testpredictions.rootMeanSquaredError)



# COMMAND ----------

#data ingestion 
import pyspark
from pyspark import SparkContext,SparkConf
from pyspark.sql.types import DoubleType,StringType,StructType,StructField
from pyspark.sql import Row,SparkSession
import numpy as np
from sklearn import metrics
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression


obj=pyspark.sql.SparkSession.builder.appName("Sqlaaa2").getOrCreate()
df=obj.read.csv("dbfs:/FileStore/affairs.csv",inferSchema=True,header=True,sep=",")
# explanatory data analysis
#vector assembler we will be using and collecting the entire numerical data into one single column
from pyspark.ml.feature import VectorAssembler
assembler=VectorAssembler(inputCols=["rate_marriage","age","yrs_married","children","religious","affairs"],outputCol="features")
df=assembler.transform(df)
df.show()
# based on affairs  column we are doing the analysis to check the data is accurate or not % how much percent
from pyspark.ml.classification import DecisionTreeClassifier
model_df=df.select(['features','affairs'])# we have stored the data into a model dataframe 
#Now split the data into  train and test models
train_mdf,test_mdf=model_df.randomSplit([.75,.25])
print(" The total number of records in model frame  is ",model_df.count())
print(" The total number of records in model frame  is ",train_mdf.count())
print(" The total number of records in model frame  is ",test_mdf.count())
from pyspark.ml.classification import LogisticRegression
log_reg=LogisticRegression(labelCol='affairs')
#using fit with trainging dataset for deriving linear regression analysis
logmodel=log_reg.fit(train_mdf)
train_results=logmodel.evaluate(train_mdf).predictions
test_results=logmodel.evaluate(test_mdf).predictions
print("Train results are ",train_results)
print("Test results are ",test_results)

train_results.select(['prediction','probability']).show(10)
test_results.select(['prediction','probability']).show(10)

