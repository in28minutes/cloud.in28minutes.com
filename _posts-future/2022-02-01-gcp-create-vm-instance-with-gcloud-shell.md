---
layout:     post
title:      Create a Virtual Machine instance from the Cloud Shell - GCP Certification Cheat Sheet
date:       2022-02-01 10:13:00
summary:    Let's get a quick overview of Create a Virtual Machine instance from the Cloud Shell in Google Cloud Platform from an GCP certification perspective. We will look at important certification questions regarding Create a Virtual Machine instance from the Cloud Shell in Google Cloud Platform.
categories:  GCP_General GCP_Compute_Engine Google_Cloud_Platform
permalink:  /gcp-create-vm-instance-with-gcloud-shell
---
Let's get a quick overview of Create a Virtual Machine instance from the Cloud Shell in Google Cloud Platform from an GCP certification perspective. We will look at important certification questions regarding Create a Virtual Machine instance from the Cloud Shell in Google Cloud Platform.


## You will learn
- How to Create a Virtual Machine instance from the Cloud Shell? 

<BR/>

If you are a command line fan, Instead of using the Cloud Console to create the VM instance, you can use the pre-installed command line tool gcloud (Debian-based virtual machine loaded with all the development tools you'll need likegcloud, git, and others and offers a persistent 5-GB home directory) in Google Cloud Shell. 


## Prerequisites

- Billing enabled GCP Account ( If you don't have one, create a billing account with your international transaction enabled credit card and you will get $300 credit for free and you can spend it over the next 90 days)

## Let's get started

**1.** Click the icon on the top right of the screen to open **Cloud Shell**.

<BR/>


![Screenshot 2022-02-01 at 5 04 28 PM](https://user-images.githubusercontent.com/57451228/151963019-73888945-a332-425f-b266-fae6149dc9ee.png)

<BR/>

If **Compute Engine API** is not enable in your GCP, You will get a option like this. And Click on **Enable**.

<BR/>


![Screenshot 2j022-02-01 at 4 52 41 PM copy](https://user-images.githubusercontent.com/57451228/151964725-94e52459-1add-4b25-90eb-9787808f9d9c.png)


<BR/>


Once it opened, you will able to view the **Cloud Shell Terminal**.

<BR/>

![Screenshot 2022-02-01 at 5 18 34 PM](https://user-images.githubusercontent.com/57451228/151963601-aa283d9e-79e4-4b73-992a-6342e68eda9f.png)

<BR/>


**2.** Now **create** the **Virtual Machine instance** using the command.

<BR/>

```sh

gcloud compute instances create gcelab2 --machine-type n1-standard-2 --zone us-central1-f

```
<BR/>

**Note: While creating the VM instance you have to specify the zone in which you want to create your instance. And instance name must be unique under the the project.**

And, The new instance has some deafult values. To know more about all the defaults. Run 

<BR/>

```sh

gcloud compute instances create --help

```
<BR/>

**3.** Now to **check the VM Instance**.
In the **Google Cloud Console**, Click on the left top **Navigation Menu**, Click on **Compute Engine**, Click on **VM instances**.

<BR/>

![Screenshot 2022-02-01 at 4 20 53 PM](https://user-images.githubusercontent.com/57451228/151964950-891aba34-3035-4481-8e25-b0bf08edead9.png)

<BR/>

<BR/>

![hhh](https://user-images.githubusercontent.com/57451228/151965228-ae08e984-15c7-42cd-9ea1-47bd41b29345.png)

<BR/>

<BR/>

**Congratulations you have succesfully created a new Virtual Machine from the Cloud Shell.**



<BR/>


<BR/>
<BR/>

<pre>
Thank You for Choosing to Learn from in28Minutes

Author
<a href="https://www.linkedin.com/in/debrup-365/">Debrup Mondal ❤️</a>
