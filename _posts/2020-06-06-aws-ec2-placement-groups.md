---
layout:     post
title:      EC2 Placement Groups - AWS Certification Cheat Sheet
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



## EC2 Placement Groups

Certain usecases need control over placement of a group of EC2 instances. Examples are use cases needing:
- Low latency network communication
- High availability

You can control placement of EC2 instances using EC2 placement groups:
- Cluster (low network latency )
- Spread (avoid simultaneous failures)
- Partition (multiple partitions with low network latency)

### EC2 Cluster Placement Group

![](/images/aws/ec2/ec2-placement-groups-cluster.png) 

Instances in EC2 Cluster Placement Group are optimized for low latency network communication between EC2 instances. EC2 instances are placed near to each other in single AZ. This provides **High Network Throughput**: EC2 instances can use 10 Gbps or 25Gbps network.

Use Case Example: Big Data or High Performance Computing needing extreme low latency

However, the disadvantage is Low Availability (Rack crashes => All EC2 instances fail)

 
### EC2 Spread Placement Group

![](/images/aws/ec2/ec2-placement-groups-spread.png) 

In EC2 Spread Placement Group, we spread EC2 instances across distinct racks having its  own network and power source.

This **Avoid simultaneous failures**  of EC2 instances.

Features:
- Can be spread across different AZs in same region
- Maximum of seven running instances per AZ in a spread placement group

#### EC2 Partition Placement Group - Use Case

![](/images/aws/ec2/ec2-placement-groups-partition.png) 

In large distributed and replicated workloads (HDFS, HBase, and Cassandra), EC2 instances need to be **divided into multiple groups** with:
- Low latency communication between instances in a group
- Each group is placed on a different rack


### EC2 Partition Placement Group

![](/images/aws/ec2/ec2-placement-groups-partition.png) 

A partition is a group of EC2 instances. In a EC2 Partition Placement Group, each partition will be **placed on a different rack**.

Features:
- You can choose the partition where EC2 instance is launched into
- Can be spread across **different AZs** in same region
- Maximum of seven partitions per Availability Zone per group

## EC2 Placement Groups - Certification Tips
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
