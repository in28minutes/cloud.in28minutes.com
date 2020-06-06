## Graphviz Examples
- First of all - Look at the files in the images folder (01ab.dot, 01ab.png, 01abc.dot, 01abc.png, 01abcd.dot, 01abcd.png, 02a.dot, 02a.png ..... 03c.dot, 03c.png)
- https://sketchviz.com/graphviz-examples
- https://graphs.grevian.org/example
- https://www.tonyballantyne.com/graphs.html
- https://renenyffenegger.ch/notes/tools/Graphviz/examples/index

## Create your own images

- You can install this - `brew install graphviz`
- clone github repo
- cd into the images folder 
- run `dot -Tpng dummy.dot > square.png` 

## Architecture
- Serverless flow - step functions, api gateway, lambda, dynamo db etc (xx-serverless-gateway-lamda-cognito-s3.png)
- Image : Cognito - API Gateway - Lambda -  DynamoDB (xx-serverless-gateway-lamda-cognito-s3.png)
- Image : S3 Notification - Lambda - SNS Notication - Email, SMS (xx-s3-event-notification.png)
- Debugging with X-Ray
- HPC workflow
- Data stream workflow
- Big data workflow

## Others

S3
- S3 Lifecycle Rules - Example (xx-s3-event-notification.png)
- S3 static website - Steps in exposing
- S3 durability - replication multi az (xx-s3-srr-crr.png)
- S3 replication if multi region is enabled (xx-s3-srr-crr.png)
- S3 notifications to SNS, SQS and lamdbas and logs to Cloud Watch (xx-s3-event-notification.png)
- S3 Pre signed urls creation - Steps involved (xx-cloudfront-signed-url.png)
- S3 Encryption - SSE-S3, SSE-KMS, SSE-C

EBS
- EBS durability - replication multi az (xx-ebs-snapshot-creation.png)
- EBS copy to different region 
- Raid 0
- Raid 1
- network communication options between EC2 instances and EBS (EBS-optimized Instances, Enhanced networking, Elastic Network Adapter, Elastic Fabric Adapter)

Check AWS Documentation for the next 4 diagrams 
- AWS Storage File Gateway (xx-file-tape-gateway.png)
- AWS Storage Tape Gateway
- AWS Storage Volume Gateway Cached (xx-storage-gateway-cached.png)
- AWS Storage Volume Gateway Stored

~Storage (xx-aws-storage-types.png)~
- Object Storage (Showing the protocols used)
- File Storage(Showing the protocols used)
- Block Storage(Showing the protocols used)

Databases
- RDS - multi az replication, active standby (master standby with sync in different azs) (xx-rds-multiaz-failover.png)
- RDS - cross region replication
- Database - Read Replicas (OLTP -> Master --async sync--> Read Replica -> (Analytics, Reports, etc) )
- EXCITING : RDS - encryption (db, communication, snapshots, backups etc)
- Redshift cluster
- Redshift integration with other services (xx-rds-multiaz-failover.png)
- Redshift Workload Management - Slow Queue and Fast Queue
- EXCITING Dynamodb - partitioning
- EXCITING Diagram - Eventually consistent
- EXCITING Diagram - Strongly consistent
- Dynamodb integration with other services including DAX (cache) (xx-dynamodb-dax.png)
- DynamoDB Streams (xx-dynamodb-streams-todo.png)

Caching
- ElastiCache usecases - ex session storage, cache (xx-simple-elasticache-rds.png)
- Redis Usecases (xx-aws-apigateway-redis-rds.png)

Cloud Front
- Cloud Front integrations overview - S3, EC2, ELB, External Website (xx-cloudfront-origins.png)
- Cloud Front stop access to S3 content
- Cloud Front - Premium content in S3
- Cloud Front signed URL (xx-cloudfront-signed-url.png)

Queuing
- SQS usecases (xx-sqs-simple-usecase-drawio.png)
- SWF - simple use case (xx-swf-simple-todo.png)
- SWF - decider, activity worker etc (xx-swf-decider-worker-drawio.png)

VPC, Subnet etc
- user -> web server -> ec2 -> database 
	- VPC - Public Subnet (web server) and Private Subnet (ec2, database)
- How is public subnet implemented? Internet Gateway and routetable configuration.
- Full flow - NACL - Security Groups
	- VPC (check against route table) -> Subnet (check against route table, NACL) -> Instance (Security groups)

Connecting to other networks/vpcs
- VPC Peering
- Elastic Network Interface
- Endpoints
- Network Address Translation(NAT) Instance and Gateways
	- CG (Customer Gateway), VPG (Virtual Private Gateway), VPN (Virtual Private Network)
- AWS Managed VPN
- AWS Direct Connect (xx-directconnect.png)
- AWS Direct Connect plus VPN

Amazon Kinesis Flows
- Kinesis Firehose
- Kinesis Stream

Others
- Elastic Beanstalk interaction with S3, SNS, CloudWatch, X-Ray
- AWS Import/Export Flow
- ELB - ASG - Target Groups - Listener - Cloud Watch Alarm etc etc.. How does ELB work?
- Cloud Watch Integrations - Alarms, Logs, SNS etc
- SNS Usecase - publisher -> sns topic -> (lambda, sqs, https, sms, email)
- Route53 
- AWS Directory Service 
- Cloud HSM
- KMS
- Amazon EMR Cluster
~- Amazon EMR Flow and integration with other services (xx-emr-ml-redshift.png)~
- AWS Data Pipeline usecase
- OpsWorks
- CloudFormation
- EC2 Placement groups - Cluster, Spread and Partitions
- Security flows - STS
