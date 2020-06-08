---
layout:     post
title:      AWS Data Lakes - Simplified Big Data Solutions - AWS Certification
date:       2020-06-06 12:31:19
summary:    Let's get a quick overview of AWS Data Lakes from an AWS certification perspective.  
categories:  AWS_CLOUD AWS_DATABASES
permalink:  /aws-certification-aws-data-lakes
---

Let's get a quick overview of AWS Data Lakes from an AWS certification perspective. 

## You will learn
- What is AWS Data Lakes?
- What are preferred Storage and Ingestion options in AWS Data Lakes?
- What is Amazon S3 Query in Place?
- Why is Data Cataloging important?
- How does AWS Glue help?

## AWS Certification - Download 25 PDF Cheat Sheets and a Free Course

Each cheat sheet contains:
- FAQs and Tutorials with 5-20 slides
- Notes to quickly review and prepare for certification exam
- Certification Exam Tips
- Certification and Interview Scenario Questions

**Download Now** - [25 AWS Cheat Sheets and Free Course - Getting Started](https://links.in28minutes.com/cloud-in28minutes-teachable-free-link){:target=""_blank""}


## AWS Data Lakes - Simplified Big Data Solutions

![](/images/aws/data-lake-architecture.png)
- Usual big data solutions are complex
- How can we make collecting, analyzing (reporting, analytics, machine learning) and visualizing huge data sets easy? 
- How to design solutions that scale? 
- How to build flexibility while saving cost?
- Data Lake 
	- Single platform with combination of solutions for data storage, data management and data analytics

## AWS Data Lakes - Storage and Ingestion
![](/images/aws/00-icons/kinesisfirehose.png)
![](/images/aws/00-icons/snowball.png)
![](/images/arrow.png)
![](/images/aws/00-icons/s3.png)
![](/images/aws/00-icons/glacier.png)

- Storage
	- Amazon S3 and S3 Glacier provide an ideal storage solution for data lakes
- Data Ingestion
	- Streaming data - Amazon Kinesis Firehose
		- Transform and store to Amazon S3
		- Transformation operations - compress, encrypt, concatenate multiple records into one (to reduce S3 transactions cost) and execute lambda functions 
	- Bulk data from on-premises - AWS Snowball
	- Integrate on-premises platforms with Amazon S3 - AWS Storage Gateway

## Amazon S3 Query in Place

![](/images/aws/00-icons/athena.png) 
![](/images/aws/00-icons/redshift.png) 
![](/images/arrow.png)
![](/images/aws/00-icons/s3.png)
![](/images/aws/00-icons/glacier.png)	

- Run your analytics directly from Amazon S3 and S3 Glacier
- S3 Select and Glacier Select
	- SQL queries to retrieve subset of data
		- Supports CSV, JSON, Apache Parquet formats
	- Build serverless apps connecting S3 Select with AWS Lambda
	- Integrate into big data workflows 
		- Enable Presto, Apache Hive and Apache Spark frameworks to scan and filter data
- Amazon Athena
	- Direct ad-hoc SQL querying on data stored in S3
	- Uses Presto and supports CSV, JSON,  Apache Parquet and Avro
- Amazon Redshift Spectrum 
	- Run queries directly against S3 without loading complete data from S3 into a data warehouse
	- Recommended if you are executing queries frequently against structured data

## Amazon S3 Query in Place - Recommendations
- You want to get quick insights from your cold data stored in S3 Glacier. You want to run queries against archives stored in S3 Glacier without restoring the archives.
	- Use S3 Glacier Select to perform filtering and basic querying using SQL queries 
	- Stores results in S3 bucket
	- No need to temporarily stage data and then run queries
- Recommendations:
	- Store data in Amazon S3 in Parquet format
		- Reduce storage (upto 85%) and improve querying (upto 99%) compared to formats like CSV, JSON, or TXT
	- Multiple compression standards are supported BUT GZIP is recommended
		- Supported by Amazon Athena, Amazon EMR and Amazon Redshift

## AWS Data Lakes -  Analytics with data in S3 Data Lake
 
| Service | Description  | 
|--|:--|
| Amazon EMR | EMR integrates well with Amazon S3 - Use big data frameworks like Apache Spark, Hadoop, Presto, or Hbase. For example: machine learning, graph analytics etc|
|Amazon Machine Learning (ML)|Create and run models for predictive analytics and machine learning (using data from Amazon S3, Amazon Redshift, or Amazon RDS)|
| Amazon QuickSight |For visualizations (using data from Amazon Redshift, Amazon RDS, Amazon Athena, and Amazon S3)|
|Amazon Rekognition | Build image recognition capabilities around images stored in Amazon S3. <BR/>Example use case : Face based verification|

## AWS Data Lakes -  Data Cataloging

![](/images/aws/data-cataloging.png) 
https://docs.aws.amazon.com/whitepapers/latest/building-data-lakes/data-cataloging.html
- 1 : What data (or assets) is stored?
- 2 : What is the format of data?
- 3 : How is the data structured?
- Question 1 - Stored in comprehensive data catalog
- Questions 2 and 3 - Stored using a Hive Meta store Catalog (HCatalog)
- AWS Glue also supports storing HCatalog

##  AWS Glue

![](/images/aws/00-icons/glue.png)

- Fully managed extract, transform, and load (ETL) service
- Simplify data preparation (capturing metadata) for analytics: 
	- Connect AWS Glue to your data on AWS (Aurora, RDS, Redshift, S3 etc)
	- AWS Glue creates a AWS Glue Data Catalog with metadata abstracted from your data
	- Your data is ready for searching and querying
- Run your ETL jobs using Apache Spark
- Metadata from AWS Glue Data Catalog can be used from:
	- Amazon Athena
	- Amazon EMR
	- Amazon Redshift Spectrum
