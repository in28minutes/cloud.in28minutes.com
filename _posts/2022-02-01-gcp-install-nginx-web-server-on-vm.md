---
layout:     post
title:      Install NGINX Web Server on Virtual Machine - GCP Certification Cheat Sheet
date:       2022-02-01 10:13:00
summary:    Let's get a quick overview of Install NGINX Web Server on Virtual Machine in Google Cloud Platform from an GCP certification perspective. We will look at important certification questions regarding Install NGINX Web Server on Virtual Machine in Google Cloud Platform.
categories:  GCP_General GCP_Compute_Engine
permalink:  /gcp-install-nginx-web-server-on-vm
---
Let's get a quick overview of Install NGINX Web Server on Virtual Machine in Google Cloud Platform from an GCP certification perspective. We will look at important certification questions regarding Install NGINX Web Server on Virtual Machine in Google Cloud Platform.


## You will learn

- How to Install NGINX Web Server on Virtual Machine?



## Prerequisites

- Billing enabled GCP Account ( If you don't have one, create a billing account with your international transaction enabled credit card and you will get $300 credit for free and you can spend it over the next 90 days)




## Let's get started

 In this article we I will show you how to install one of the most popular web server NGINX on Virtual machine, to connect it with something.

1. Go to https://console.cloud.google.com/ or open **Google cloud console**. 
   - Login with your billing enabled Google account.
   - Create a **new project**, if you have not any. 
   - Create a **Virtual Machine**, if you have not any. If you don't know how to create VM Instance, you can watch this article [Link]

<BR/>

2. Click on the **SSH link** on your **VM Instance**.
 
 ![Screenshot 2022-02-01 at 5 02 41 PM](https://user-images.githubusercontent.com/57451228/151987392-dea74c5e-4da2-49ed-be10-7048d4cea431.png)

Now, You will able to see a command line interface which is the console of your Virtual Instance.

<BR/>

3. To get the **root acces** in the SSH Terminal. Run the following command:

```sh

sudo su -

```

Awesome! Now you are the root user.

<BR/>

4. Now time to **update** your OS:

```sh

apt-get update

```

Awesome! Your OS is updated and you are good to go.

<BR/>

5. Now it's time to **install NGINX** with the following command:

```sh

apt-get install nginx -y

```
**Yeppie! NGINX is successfully installed.**

<BR/>

6. Now it's time to confirm that NGINX is running with the following command:

```sh

ps auwx | grep nginx

```

I know now you are too curious to visit the official default NGINX page.

<BR/>

7. To visit the web page, just retun to the **Google Cloud Console** in the **VM Instance page**. Click the **external link** in the row of the Virtual Machine or just copy the value and paste in a new window.

![Screenshot k2022-02-01 at 5 02 41 PM copy](https://user-images.githubusercontent.com/57451228/151988939-ad2cb4da-a6ae-4598-8732-aca2f6afbf52.png)

Now you will be able to see the default web page of NGINX.

![Screenshot 2022-02-01 at 5 03 22 PM](https://user-images.githubusercontent.com/57451228/151989161-f8208c8f-4373-41b2-b909-3218e2d094d6.png)


**Congratulations! You have successfully installed NGINX on you Virtual Machine.**




<BR/>
<BR/>

<pre>
Thank You for Choosing to Learn from in28Minutes

Author
<a href="https://www.linkedin.com/in/debrup-365/">Debrup Mondal ❤️</a>
