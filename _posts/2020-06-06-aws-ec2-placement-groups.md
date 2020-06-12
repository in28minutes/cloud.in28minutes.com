---
layout:     post
title:      EC2 Placement Groups - AWS Certification
date:       2020-06-06 12:31:19
summary:    Let's get a quick overview of EC2 Placement Groups from an AWS certification perspective. We will look at important certification questions regarding EC2 Placement Groups.  We will look at the three types of EC2 Placement Groups - Cluster, Spread and Partition.
categories:  AWS_CLOUD EC2
permalink:  /aws-certification-ec2-placement-groups
---

Let's get a quick overview of EC2 Placement Groups from an AWS certification perspective. We will look at important certification questions regarding EC2 Placement Groups.

Let's understand the three types of EC2 Placement Groups
- Cluster (low network latency )
- Spread (avoid simultaneous failures)
- Partition (multiple partitions with low network latency)


## You will learn
- What are the three types of EC2 Placement Groups?
- Why do you need EC2 Placement Groups?
- When do you use Cluster, Spread and Partition EC2 Placement Groups?

## AWS Certification - 25 PDF Cheat Sheets + Free Course

Each cheat sheet contains:
- FAQs and Tutorials with 5-20 slides
- Notes to quickly review and prepare for certification exam
- Certification Exam Tips
- Certification and Interview Scenario Questions

<div>
 <a href="https://links.in28minutes.com/cloud-in28minutes-teachable-free-link" target="_blank" class="button instagram">Download</a>
</div>


## EC2 Placement Groups
![](/images/aws/ec2-host.png)
![](/images/aws/ec2-host.png)
![](/images/aws/ec2-host.png)

Certain usecases need control over placement of a group of EC2 instances. Examples are use cases needing:
- Low latency network communication
- High availability

You can control placement of EC2 instances using EC2 placement groups:
- Cluster (low network latency )
- Spread (avoid simultaneous failures)
- Partition (multiple partitions with low network latency)

## EC2 Cluster Placement Group
![](/images/aws/ec2/ec2-placement-groups-cluster.png) 
- When low latency network communication between EC2 instances is critical
- Example: Big Data or High Performance Computing needing extreme low latency
- EC2 instances placed near to each other in single AZ
- **High Network Throughput**: EC2 instances can use 10 Gbps or 25Gbps network
- (Disadvantage) Low Availability (Rack crashes => All EC2 instances fail)

 
## EC2 Spread Placement Group
![](/images/aws/ec2/ec2-placement-groups-spread.png) 
- Spread EC2 instances across distinct racks
- Each rack has its own network and power source
- **Avoid simultaneous failures**  of EC2 instances
- Can be spread across different AZs in same region
- Maximum of seven running instances per AZ in a spread placement group

## EC2 Partition Placement Group - Use Case
![](/images/aws/ec2/ec2-placement-groups-partition.png) 
- In large distributed and replicated workloads (HDFS, HBase, and Cassandra), EC2 instances need to be **divided into multiple groups**:
	- Low latency communication between instances in a group
	- Each group is placed on a different rack


## EC2 Partition Placement Group
![](/images/aws/ec2/ec2-placement-groups-partition.png) 
- A partition is a group of EC2 instances
- Each partition will be **placed on a different rack**
- You can choose the partition where EC2 instance is launched into
- Can be spread across **different AZs** in same region
- Maximum of seven partitions per Availability Zone per group

## EC2 Placement Groups - Best Practices
- **Insufficient capacity error** can happen when:
	- New instances are added in (OR)
	- More than one instance type is used (OR)
	- An instance in placement group is stopped and started
- If you receive a capacity error: 
	- Stop and start all instances in the placement group (OR)
	- Try to launch the placement group again 
	- Result: Instances may be migrated to a rack that has capacity for all the requested instances
- **Recommendation**:
	- Have only one instance type in a launch request AND 
	- Launch all instances in a single launch request together   

## EC2 Placement Groups - AWS Certification Exam Practice Questions

Coming Soon...

