---
layout:     post
title:      DevOps in AWS - CloudFormation vs CodePipeline vs CodeBuild vs CodeDeploy vs OpsWorks
date:       2020-06-06 12:31:19
summary:    Let's get a quick overview of DevOps in AWS. What are the different DevOps tools? Which one is the right option for which scenario - CloudFormation vs CodePipeline vs CodeBuild vs CodeDeploy vs OpsWorks?
categories:  AWS_CLOUD AWS_SERVICES
permalink:  /aws-certification-devops-in-aws-cloudformation-vs-codepipeline-vs-opsworks
---

Let's get a quick overview of DevOps in AWS. What are the different DevOps tools? Which one is the right option for which scenario - CloudFormation vs CodePipeline vs CodeBuild vs CodeDeploy vs OpsWorks?

## You will learn
- What is DevOps?
- What is CI/CD?
- What is IAAC?
- What is CloudFormation?
- What is OpsWorks?
- How do these compare against each other - CodePipeline vs CodeBuild vs CodeDeploy?

## AWS Certification - 25 PDF Cheat Sheets + Free Course

Each cheat sheet contains:
- FAQs and Tutorials with 5-20 slides
- Notes to quickly review and prepare for certification exam
- Certification Exam Tips
- Certification and Interview Scenario Questions

<div>
 <a href="https://links.in28minutes.com/cloud-in28minutes-teachable-free-link" target="_blank" class="button instagram">Download</a>
</div>

## DevOps
![](/images/aws/devops-06-teams.png)
- Getting Better at "**Three Elements of Great Software Teams**"
	- Communication - Get teams together
	- Feedback - Earlier you find a problem, easier it is to fix
	- Automation - Automate testing, infrastructure provisioning, deployment, and monitoring

## DevOps - CI, CD

![](/images/aws/devops-05-continuous-delivery.png) 
- Continuous Integration 
	- Continuously run your tests and packaging
- Continuous Deployment 
	- Continuously deploy to test environments
- Continuous Delivery 
	- Continuously deploy to production

## DevOps - CI, CD Tools
![](/images/aws/00-icons/codecommit.png) 
![](/images/aws/00-icons/codepipeline.png) 
![](/images/aws/00-icons/codebuild.png) 
![](/images/aws/00-icons/codedeploy.png) 
- AWS CodeCommit - Private source control (Git)
- AWS CodePipeline - Orchestrate CI/CD pipelines
- AWS CodeBuild - Build and Test Code (application packages and containers)
- AWS CodeDeploy - Automate Deployment (EC2, ECS, Elastic Beanstalk, EKS, Lambda etc)

## DevOps - IAAC
![](/images/aws/devops-06-iaac-2-overview.png) 

- Treat infrastructure the same way as application code
- Track your infrastructure changes over time (version control)
- Bring repeatability into your infrastructure
- Two Key Parts
	- Infrastructure Provisioning 
		- Provisioning compute, database, storage and networking
		- Open source cloud neutral - Terraform
		- AWS Service - CloudFormation
	- Configuration Management 
		- Install right software and tools on the provisioned resources
		- Open Source Tools - Chef, Puppet, Ansible
		- AWS Service - OpsWorks

## AWS Cloud​Formation - Introduction

![](/images/aws/00-icons/cloudformation.png) 
- Lets consider an example:
	- I would want to create a new VPC and a subnet
	- I want to provision a ELB, ASG with 5 EC2 instances and an RDS database in the subnet
	- I would want to setup the right security groups
- AND I would want to create 4 environments 
	- Dev, QA, Stage and Production!
- CloudFormation can help you do all these with a simple (actually NOT so simple) script!

## AWS CloudFormation - Advantages

![](/images/aws/00-icons/cloudformation.png) 

- Automate deployment and modification of AWS resources in a controlled, predictable way
- Avoid configuration drift
- Avoid mistakes with manual configuration
- Think of it as version control for your environments

![](/images/aws/00-icons/cloudformation.png) 

## AWS Cloud​Formation
- All configuration is defined in a simple text file - JSON or YAML
	- I want a VPC, a subnet, a database and ...
- CloudFormation understands dependencies
	- Creates VPCs first, then subnets and then the database
- (Default) Automatic rollbacks on errors (Easier to retry)
	- If creation of database fails, it would automatic delete the subnet and VPC
- Version control your configuration file and make changes to it over time
- Free to use - Pay only for the resources provisioned
	- Get an automated estimate for your configuration

## AWS Cloud​Formation - Example 1 - JSON
```
{
    "Resources" : {
        "MyBucket" : {
            "Type" : "AWS::S3::Bucket"
            "Properties" : {
               "AccessControl" : "PublicRead"               
            }
        }
    }
}
```

## AWS CloudFormation - Example 2 - YAML
```
Resources:
  MyBucket:
    Type: AWS::S3::Bucket
    Properties:
      AccessControl: PublicRead
```

## AWS CloudFormation - Example 3
```
Resources:
  Ec2Instance:
    Type: 'AWS::EC2::Instance'
    Properties:
      ImageId: "ami-0ff8a91507f77f867"
      InstanceType: t2.micro
      SecurityGroups:
        - !Ref InstanceSecurityGroup
  InstanceSecurityGroup:
    Type: 'AWS::EC2::SecurityGroup'
    Properties:
      GroupDescription: Enable SSH access via port 22
      SecurityGroupIngress:
        - IpProtocol: tcp
          FromPort: '22'
          ToPort: '22'
          CidrIp: 0.0.0.0/0
```

## AWS Cloud​Formation - Terminology
- Template 
	- A Cloud​Formation JSON or YAML defining multiple resources
- Stack 
	- A group of resources that are created from a CloudFormation template
	- In the earlier example, the stack contains an EC2 instance and a security group
- Change Sets 
	- To make changes to stack, update the template
	- Change set shows what would change if you execute
	- Allows you to verify the changes and then execute

## AWS Cloud​Formation - Important template elements

```
{
  "AWSTemplateFormatVersion" : "version date",
  "Description" : "JSON string",
  "Metadata" : {},
  "Parameters" : {},
  "Mappings" : {},
  "Resources" : {},
  "Outputs" : {}
}
```

- Resources - What do you want to create?
	- One and only mandatory element
- Parameters - Values to pass to your template at runtime 
	- Which EC2 instance to create? - ("t2.micro", "m1.small", "m1.large")
- Mappings - Key value pairs 
	- Example: Configure different values for different regions
- Outputs - Return values from execution 
	- See them on console and use in automation

## AWS CloudFormation - Mappings Example

```
"Mappings" : {
  "RegionMap" : {
    "us-east-1"      : { "AMI" : "AMI-A"},
    "us-west-1"      : { "AMI" : "ami-B"},
    "eu-west-1"      : { "AMI" : "ami-C"},
    "ap-southeast-1" : { "AMI" : "ami-D"},
    "ap-northeast-1" : { "AMI" : "ami-E"}
  }
}
```

## AWS Cloud​Formation - Remember

![](/images/aws/00-icons/cloudformation.png)  
- Deleting a stack deletes all the associated resources
	- EXCEPT for resources with DeletionPolicy attribute set to "Retain"
	- You can enable termination protection for the entire stack
- Templates are stored in S3
- Use CloudFormation Designer to visually design templates
- AWS CloudFormation StackSets 
	- Create, update, or delete stacks across multiple accounts and regions with a single operation

## Cloud​Formation vs AWS Elastic Beanstalk
![](/images/aws/00-icons/elastic-beanstalk.png) 
![](/images/arrow.png)
![](/images/aws/00-icons/cloudformation.png)  

- (Do you know?) You can create an Elastic Beanstalk environment using CloudFormation!
- Think of Elastic Beanstalk as a pre-packaged CloudFormation template with a User Interface
	- You choose what you want
	- (Background) A Cloud Formation template is created and executed
	- The environment is ready!

## AWS OpsWorks - Configuration Management

![](/images/aws/00-icons/opsworks.png) 
- OpsWorks is used for Configuration Management 
	- How do you ensure that 100 servers have the same configuration?
	- How can I make a change across 100 servers?
- Managed service based on Chef & Puppet
- One service for deployment and operations in cloud and on-premise environments
- Configuration - Chef recipes or cookbooks, Puppet manifests
- All metrics are sent to Amazon CloudWatch
- (IMPORTANT) All configuration management tools can also do infrastructure provisioning
	- However, I would recommend NOT doing that as they are not good at infrastructure provisioning
