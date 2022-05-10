---
layout:     post
title:      GCP App Engine - GCP Certification Cheat Sheet
date:       2022-05-06 00:00:00
summary:    Let's get a quick overview of Google Cloud App Engine
categories:  GCP_COMPUTE
permalink:  /gcp-certification-google-cloud-app-engine
---

Let's get a quick overview of Google Cloud App Engine from an GCP certification perspective. We will look at important certification questions related to App Engine, how this is different compared to other compute services, features of App Engine and how to use AppEngine to run your compute load.

## You will learn
- What is a App Engine
- Features of AppEngine
- Various concepts of AppEngine and how to use it to run the applications
- Commands Cheatsheet

## GCP Certification Study Material and Notes - 25 PDF Cheat Sheets

Each cheat sheet contains:
- FAQs and Tutorials with 5-20 slides
- Study Material and Notes to quickly review and prepare for certification exam
- Certification Exam Tips
- Certification and Interview Scenario Questions

<div>
 <a href="https://links.in28minutes.com/cloud-in28minutes-teachable-free-link" target="_blank" class="button instagram">Download</a>
</div>

# App Engine

## App Engine
![](./gcpimages/00-icons/gcp/app-engine.png)
- **Simplest way** to deploy and scale your applications in GCP
	- Provides end-to-end application management
- Supports:
	- Go, Java, .NET, Node.js, PHP, Python, Ruby using pre-configured runtimes
	- Use custom run-time and write code in any language
	- Connect to variety of Google Cloud storage products (Cloud SQL etc)
- **No usage charges** - Pay for resources provisioned
- **Features**:
	- Automatic load balancing & Auto scaling
	- Managed platform updates & Application health monitoring
	- Application versioning
	- Traffic splitting

## Compute Engine vs App Engine
![](./gcpimages/00-icons/gcp/app-engine.png)
![](./gcpimages/00-icons/gcp/compute-engine.png)
- **Compute Engine**
	- IAAS
	- MORE Flexibility
	- MORE Responsibility
		- Choosing Image
		- Installing Software
		- Choosing Hardware
		- Fine grained Access/Permissions (Certificates/Firewalls)
		- Availability etc
- **App Engine**
	- PaaS
	- Serverless
	- LESSER Responsibility
	- LOWER Flexibility

## App Engine environments
![](./gcpimages/00-icons/gcp/app-engine.png)

- **Standard**: Applications run in language specific sandboxes
	- Complete isolation from OS/Disk/Other Apps
	- **V1**: Java, Python, PHP, Go (OLD Versions)
		- ONLY for Python and PHP runtimes:
			- Restricted network Access
			- Only white-listed extensions and libraries are allowed
		- No Restrictions for Java and Go runtimes
	- **V2**: Java, Python, PHP, Node.js, Ruby, Go (NEWER Versions)
		- Full Network Access and No restrictions on Language Extensions
- **Flexible** - Application instances run within Docker containers 
	- Makes use of Compute Engine virtual machines
	- Support ANY runtime (with built-in support for Python, Java, Node.js, Go, Ruby, PHP, or .NET)
	- Provides access to background processes and local disks

## App Engine - Application Component Hierarchy
![](./gcpimages/02-architecture/appengine-architecture-components.png)
- **Application**: One App per Project
- **Service(s)**: Multiple Microservices or App components
	- You can have multiple services in a single application
	- Each **Service** can have different settings
	- Earlier called Modules
- **Version(s)**: Each version associated with code and configuration
	- Each **Version** can run in one or more instances
	- Multiple versions can co-exist
	- Options to rollback and split traffic

## App Engine - Comparison

| Feature | Standard | Flexible |
|:--|:--|:--|
|Pricing Factors|Instance hours|vCPU, Memory & Persistent Disks|
|Scaling|Manual, Basic, Automatic|Manual, Automatic|
|Scaling to zero|Yes|No. Minimum one instance|
|Instance startup time|Seconds|Minutes|
|Rapid Scaling|Yes|No|
|Max. request timeout|1 to 10 minutes|60 minutes|
|Local disk|Mostly(except for Python, PHP). Can write to /tmp.  |Yes. Ephemeral. New Disk on startup.|
|SSH for debugging|No|Yes|

## App Engine - Scaling Instances
![](./gcpimages/00-icons/gcp/app-engine.png)

- **Automatic** - Automatically scale instances based on the load:
	- Recommended for Continuously Running Workloads
		- Auto scale based on:
			- **Target CPU Utilization** - Configure a CPU usage threshold.
			- **Target Throughput Utilization** - Configure a throughput threshold
			- **Max Concurrent Requests** - Configure max concurrent requests an instance can receive
		- Configure **Max Instances** and **Min Instances**
- **Basic** - Instances are created as and when requests are received:
	- Recommended for Adhoc Workloads
		- Instances are shutdown if ZERO requests
			- Tries to keep costs low
			- High latency is possible
		- NOT supported by App Engine Flexible Environment
		- Configure **Max Instances** and **Idle Timeout**
- **Manual** - Configure specific number of instances to run: 
	- Adjust number of instances manually over time

## app.yaml Reference
```
runtime: python28 #The name of the runtime environment that is used by your app
api_version: 1  #RECOMMENDED - Specify here - gcloud app deploy -v [YOUR_VERSION_ID]
instance_class: F1
service: service-name 
#env: flex

inbound_services:
- warmup

env_variables:
  ENV_VARIABLE: "value"

handlers:
- url: /
  script: home.app

automatic_scaling:
  target_cpu_utilization: 0.65
  min_instances: 5
  max_instances: 100
  max_concurrent_requests: 50
#basic_scaling:
  #max_instances: 11
  #idle_timeout: 10m
#manual_scaling:
  #instances: 5
```

## AppEngine - Request Routing
![](./gcpimages/00-icons/gcp/app-engine.png)

- You can use a **combination** of three approaches:
	- Routing with **URLs**:
		- https://PROJECT_ID.REGION_ID.r.appspot.com (default service called)
		- https://SERVICE-dot-PROJECT_ID.REGION_ID.r.appspot.com (specific service)
		- https://VERSION-dot-SERVICE-dot-PROJECT_ID.REGION_ID.r.appspot.com (specific version of service)
		- Replace -dot- with . if using custom domain
	- Routing with a **dispatch file**:
		- Configure `dispatch.yaml` with routes 
		- `gcloud app deploy dispatch.yaml`
	- Routing with **Cloud Load Balancing**:
		- Configure routes on Load Balancing instance

## AppEngine - Deploying new versions without downtime
![](./gcpimages/00-icons/gcp/app-engine.png)
- How do I go from V1 to V2 without downtime?
- **Option 1**: I'm very confident - Deploy & shift all traffic at once:
	- Deploy and shift all traffic at once from v1 to v2: ***gcloud app deploy***
- **Option 2**: I want to manage the migration from v1 to v2
	- **STEP 1**: Deploy v2 without shifting traffic (`--no-promote`)
		- ***gcloud app deploy --no-promote***
	- **STEP 2**: Shift traffic to V2:
		- **Option 1** (All at once Migration): Migrate all at once to v2 
			- ***gcloud app services set-traffic s1 --splits V2=1***
		- **Option 2 (Gradual Migration)**: Gradually shift traffic to v2. Add `--migrate` option.
			- Gradual migration is not supported by App Engine Flexible Environment
		- **Option 3 (Splitting)**: Control the pace of migration 
			- ***gcloud app services set-traffic s1 --splits=v2=.5,v1=.5***
			- Useful to perform A/B testing
		- Ensure that new instances are warmed up before they receive traffic (app.yaml - `inbound_services > warmup`)

## How do you split traffic between multiple versions?
![](./gcpimages/00-icons/gcp/app-engine.png)

- How do you decide which version receives which traffic?
	- **IP Splitting** - Based on request IP address
		- IP addresses can change causing accuracy issues! (I go from my house to a coffee shop)
		- If all requests originate from a corporate vpn with single IP, this can cause all requests to go to the same version
	- **Cookie Splitting** - Based on a cookie (**GOOGAPPUID**)
		- Cookies can be controlled from your application
		- Cookie splitting accurately assign users to versions
	- **Random** - Do it randomly
- How to do it?
	- Include `--split-by` option in `gcloud app services set-traffic` command
		- Value must be one of: cookie, ip, random
		- `gcloud app services set-traffic s1 --splits=v2=.5,v1=.5 --split-by=cookie` 

## Playing with App Engine

![](./gcpimages/00-icons/gcp/app-engine.png)

- ***gcloud app browse/create/deploy/describe/open-console***
	- *gcloud app **create** --region=us-central*
	- *gcloud app **deploy** app.yaml*
		- --image-url: Only for flexible environments. Deploy docker image.
			- *gcloud app deploy --image-url gcr.io/PROJECT-ID/hello-world-rest-api:0.0.1.RELEASE*
		- --promote --no-promote (Should new version receive traffic?)
		- --stop-previous-version --no-stop-previous-version (Should old version be stopped after new version receives all traffic?)
		- --version (Assign a version. Otherwise, a version number is generated.)
	- *gcloud app **browse** --service="myService" --version="v1"* (open in a web browser)
	- *gcloud app **open-console** --service="myService" --version="v1"*
	- *gcloud app **open-console --logs***
- Other Commands
	- *gcloud app **logs tail***
	- *gcloud app **regions list***

![](./gcpimages/00-icons/gcp/app-engine.png)

## Playing with App Engine Instances
- ***gcloud app instances delete/describe/list/scp/ssh***
	- *gcloud app instances **delete** i1 --service=s1 --version=v1*
	- *gcloud app instances **describe** --service=s1 --version=v1 i1*
	- *gcloud app instances **list***
	- *gcloud app instances **scp** --service=s1 --version=v1  --recurse local_dir i1:remote_dir* (Copy files to/from App Engine Flexible instances)
	- *gcloud app instances **ssh** --service=s1 --version=v1 i1* (SSH into the VM of an App Engine Flexible instance)

## Playing with App Engine Services and Versions

- **gcloud app services browse/delete/describe/list/set-traffic**
	- *gcloud app services **list***
	- *gcloud app services **browse** myService --version="v1"*
	- *gcloud app services **delete** service1 service2*
	- *gcloud app services **describe** service1*
	- *gcloud app services **set-traffic** APP1 --splits v1=0.9,v2=0.1*
		- --split_by (ip, cookie, random)
- **gcloud app versions browse/delete/describe/list/migrate/start/stop**
	- *gcloud app versions **list***
		- --hide-no-traffic (Only show versions that are receiving traffic)
	- *gcloud app versions **browse**/**delete**/**describe** v1 --service="myService"*
	- *gcloud app versions **migrate** v2 --service="myService"* (migrate all traffic to new version)
	- *gcloud app versions **start/stop** v1*
		- --service=my-service Only start v1 of service my-service

## App Engine - Cron Job

```
cron:
- description: "daily summary job"
  url: /tasks/summary
  schedule: every 24 hours
```

- Allows to run **scheduled jobs** at pre-defined intervals
- **Use cases**:
	- Send a report by email every day
	- Refresh cache data every 30 minutes
- Configured using **cron.yaml** 
- Run this command -  ***gcloud app deploy cron.yaml***
	- Performs a **HTTP GET** request to the configured URL on schedule


## Others Important App Engine yaml files

- **dispatch.yaml** - override routing rules	

```
dispatch:
  - url: "*/mobile/*"
    service: mobile-frontend
  - url: "*/work/*"
	service: static-backend
```
- **queue.yaml** - manage task queues

```
queue:
- name: fooqueue
  rate: 1/s
  retry_parameters:
    task_retry_limit: 7
    task_age_limit: 2d
```

## App Engine - Remember
![](./gcpimages/00-icons/gcp/app-engine.png)
- AppEngine is **Regional** (services deployed across zones)
	- You **CANNOT** change an Application's region
- Good option for simple **microservices** (multiple services)
	- Use **Standard v2** when you are using supported languages
	- Use **Flexible** if you are building containerized apps 
- Be aware - **ATLEAST one container** is always running when using **Flexible**:
	- **Go for Standard** if you want to be able to scale down the number of instances to **zero** when there is NO load
- Use a **combination of resident and dynamic** instances
	- Resident Instances: Run continuously
	- Dynamic Instances: Added based on load
		- Use all dynamic instances if you are cost sensitive
		- If you are not very cost sensitive, keep a set of resident instances running always

## App Engine - Scenarios

| Scenario |Solution  |
|:--|:--|
|I want to create two Google App Engine Apps in the same project|Not possible. You can only have one App Engine App per project. However you can have multiple services and multiple version for each service.|
|I want to create two Google App Engine Services inside the same App|Yup. You can create multiple services under the same app. Each service can have multiple versions as well.|
|I want to move my Google App Engine App to a different region|App Engine App is region specific. You CANNOT move it to different region. Create a new project and create new app engine app in the new region.|
|Perform Canary deployments|Deploy v2 without shifting traffic (`gcloud app deploy --no-promote`)<BR/> Shift some traffic to V2 (`gcloud app services set-traffic s1 --splits v1=0.9,v2=0.1`)|
