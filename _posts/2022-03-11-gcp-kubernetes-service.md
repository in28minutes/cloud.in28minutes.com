---
layout:     post
title:      Google Kubernetes Service 
date:       2022-03-11 11:13:00
summary:    Let's get a quick overview of Google Kubernetes Service from an GCP certification perspective. We will look at important certification questions regarding Google Kubernetes Service.
categories:  GCP_General GCP_Computing_Services Google_Kubernetes_Engine Google_Cloud_Platform 
permalink:  /gcp-kubernetes-service
---
Let's get a quick overview of Google Kubernetes Service from an GCP certification perspective. We will look at important certification questions regarding Google Kubernetes Service.

## You will learn

- What is Kubernetes Service?
- Why to use Kubernetes Service?
- Case Study : Quick Reminder of Kubernetes Service.
- Types of Kubernetes Service?

<BR/>



## Kubernetes Service

`The main concept of a Service is to group a set of Pod endpoints in a single resource.`

Service use a selector to identify it's member Pods. To be a member of the Service, Pods must have all of the `labels (an arbitrary key/value pair that is attached to an object)` mentioned in the selector.

You can check the below example Service manifest which has a selector that specifies two labels. 
So, Now according to the `selector` field, any Pod that has both the `app : metrics` label and the `department : cloudengineering` label is a member of this Service.

```sh
apiVersion: v2
kind: Service
metadata:
  name: in28Minutes-service
spec:
  selector:
    app: metrics
    department: cloudengineering
  ports:
  ...
  ```

## Why to use Kubernetes Service?

Think about a scenario, In Kubernetes Cluster your each Pod has an internal IP address. But, In a deployment it come and go, and the ip address also change. So, You cann't use Pod IP address directly.
So, here Service comes into the picture, with the help of Service, `you get a static IP address which lasts for the life of the service, it does not care if the IP address of the member Pods change.`

It's also helps in `load balancing`. Here client can call a single and static IP address, and the requests are balanced accross the Pods, which are member of the Service.

## Case Study : For quick remember
  
- Each Pod has its **own IP address:**
  - How do you ensure that external users are not impacted when:
     - A pod fails and is replaced by replica set
     - A new release happens and all existing pods of old release are replaced by ones of new release
- Create **Service**
  - kubectl expose deployment name --type=LoadBalancer --port=80
     - Expose PODs to outside world using a stable IP Address
     - Ensures that the external world does not get impacted as pods go down and come up

## Types of Kubernetes Services :

- **ClusterIP (default) :** Exposes Service on a cluster-internal IP
  - Use case: You want your microservice only to be available inside the cluster (Intra cluster communication)
- **LoadBalancer:** Exposes Service externally using a cloud provider's load balancer
   - Use case: You want to create individual Load Balancer's for each microservice
- **NodePort:** Exposes Service on each Node's IP at a static port (the NodePort)
   - Use case: You DO not want to create an external Load Balancer for each microservice (You can create one Ingress component to load balance multiple microservices)
- ExternalName: Internal clients use the DNS name of a Service as an alias for an external DNS name.
- Headless: You can use a headless service when you want a Pod grouping, but don't need a stable IP address.


<BR/>
<BR/>

<pre>
Thank You for Choosing to Learn from in28Minutes

Author
<a href="https://www.linkedin.com/in/debrup-365/">Debrup Mondal ❤️</a>

