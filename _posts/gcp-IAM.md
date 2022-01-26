---
layout:     post
title:      Authentication and Authorization in Google Cloud with Cloud IAM - GCP Certification Cheat Sheet
date:       2021-12-07 10:13:00
summary:    Let's get a quick overview of Authentication and Authorization in Google Cloud with Cloud IAM in Google Cloud Platform from an GCP certification perspective. We will look at important certification questions regarding Authentication and Authorization in Google Cloud with Cloud IAM in Google Cloud Platform.
categories:  GCP_General GCP_Authentication_Authorization_Services
permalink:  /gcp-IAM
---
Let's get a quick overview of Authentication and Authorization in Google Cloud with Cloud IAM in Google Cloud Platform from an GCP certification perspective. We will look at important certification questions regarding Authentication and Authorization in Google Cloud with Cloud IAM in Google Cloud Platform.


## You will learn

- Typical identity management in the cloud
- Cloud Identity and Access Management (IAM)
- Cloud IAM Example
- IAM - Roles
- IAM - Predefined Roles - Example Permissions
- IAM - Most Important Concepts - A Review
- IAM policy
- Playing With IAM
- Service Accounts
- Use case 1 : VM <-> Cloud Storage
- Use case 2 : On Prem <-> Cloud Storage (Long Lived)
- Use case 3 : On Prem <-> Google Cloud APIs (Short Lived)
- Service Account Use case Scenarios
- ACL (Access Control Lists)
- Access Control - Overview
- Cloud Storage - Signed URL
- Cloud Storage - Static website

<BR/>


## Typical identity management in the cloud

![iam](https://user-images.githubusercontent.com/57451228/151097473-84a3a87c-5214-44e1-a14f-a5b9a2c5306b.png)


- You have **resources** in the cloud (examples - a virtual server, a database etc)
- You have **identities (human and non-human)** that need to access those resources and perform actions
  - For example: launch (stop, start or terminate) a virtual server
- How do you **identify users** in the cloud?
  - How do you configure resources they can access?
  - How can you configure what actions to allow?
- In GCP: Identity and Access Management (Cloud IAM) provides this service


## Cloud Identity and Access Management (IAM)

- **Authentication** (is it the right user?) and
- **Authorization** (do they have the right access?)
- **Identities** can be
  - A GCP User (Google Account or Externally Authenticated User)
  - A Group of GCP Users
  - An Application running in GCP
  - An Application running in your data center
  - Unauthenticated users
- Provides very **granular** control
  - Limit a single user:
     - to perform single action
     - on a specific cloud resource
     - from a specific IP address
     - during a specific time window

## Cloud IAM Example 
  
&emsp; &emsp; ![user-card](https://user-images.githubusercontent.com/57451228/151097904-1302e9cb-080e-4a8c-a739-c09cdaf9e7e6.png)

&emsp; &emsp; &emsp; &emsp;  ![arrowtd](https://user-images.githubusercontent.com/57451228/151097914-f17b764c-e48a-45ee-a900-da1ba7c2de64.png)

&emsp; ![storage-card](https://user-images.githubusercontent.com/57451228/151097924-0e823051-473c-4341-bd03-d9204f41c384.png)

  
- I want to provide access to manage a specific cloud storage bucket to a colleague of mine:
  - Important Generic Concepts:
     - Member: My colleague
     - Resource: Specific cloud storage bucket
     - Action: Upload/Delete Objects
  - In Google Cloud IAM:
     - Roles: A set of permissions (to perform specific actions on specific resources)
        - Roles do NOT know about members. It is all about permissions!
     - How do you assign permissions to a member?
        - Policy: You assign (or bind) a role to a member
- 1: **Choose a Role** with right permissions (Ex: Storage Object Admin)
- 2: **Create Policy** binding member (your friend) with role (permissions)
- IAM in AWS is very different from GCP (Forget AWS IAM & Start FRESH!)
  - Example: Role in AWS is NOT the same as Role in GCP

## IAM - Roles

- Roles are Permissions:
  - Perform some set of actions on some set of resources
- Three Types:
  - **Basic Roles** (or Primitive roles) - Owner/Editor/Viewer
     - Viewer(roles.viewer) - Read-only actions
     - Editor(roles.editor) - Viewer + Edit actions
     - Owner(roles.owner) - Editor + Manage Roles and Permissions + Billing
     - EARLIEST VERSION: Created before IAM
     - NOT RECOMMENDED: Don't use in production
  - **Predefined Roles** - Fine grained roles predefined and managed by Google
     - Different roles for different purposes
     - Examples: Storage Admin, Storage Object Admin, Storage Object Viewer, Storage Object Creator
  - **Custom Roles** - When predefined roles are NOT sufficient, you can create your own custom roles


## IAM - Predefined Roles - Example Permissions

- Important **Cloud Storage Roles:**
  - **Storage Admin (roles/storage.admin)**
     - storage.buckets.*
     - storage.objects.*
  - **Storage Object Admin (roles/storage.objectAdmin)**
     - storage.objects.*
  - **Storage Object Creator (roles/storage.objectCreator)**
     - storage.objects.create
  - **Storage Object Viewer (roles/storage.objectViewer)**
     - storage.objects.get
     - storage.objects.list
- All four roles have these permissions:
  - resourcemanager.projects.get
  - resourcemanager.projects.list


## IAM - Most Important Concepts - A Review

![00-roles](https://user-images.githubusercontent.com/57451228/151098607-653c8eee-659d-4c35-9230-b80201836668.png)


- Member : Who?
- Roles : Permissions (What Actions? What Resources?)
- Policy : Assign Permissions to Members
  - Map Roles (What?) , Members (Who?) and Conditions (Which Resources?, When?, From Where?)
  - Remember: Permissions are NOT directly assigned to Member
     - Permissions are represented by a Role
     - Member gets permissions through Role!
- A Role can have multiple permissions
- You can assign multiple roles to a Member

## IAM policy

- Roles are assigned to users through **IAM Policy** documents
- Represented by a **policy object**
  - Policy object has list of bindings
  - A binding, binds a role to list of members
- Member type is identified by **prefix**:
  - Example: user, serviceaccount, group or domain

## IAM policy - Example

```sh
{
  "bindings": [
    {
      "role": "roles/storage.objectAdmin",
       "members": [
         "user:you@in28minutes.com",
         "serviceAccount:myAppName@appspot.gserviceaccount.com",
         "group:administrators@in28minutes.com",
         "domain:google.com"
       ]
    },
    {
      "role": "roles/storage.objectViewer",
      "members": [
        "user:you@in28minutes.com"
      ],
      "condition": {
        "title": "Limited time access",
        "description": "Only upto Feb 2022",
        "expression": "request.time < timestamp('2022-02-01T00:00:00.000Z')",
      }
    }
  ]
}

```




## Playing With IAM

- **gcloud**: Playing with IAM
  - gcloud **compute project-info** describe - Describe current project
  - gcloud **auth login** - Access the Cloud Platform with Google user credentials
  - gcloud **auth revoke** - Revoke access credentials for an account
  - gcloud **auth list** - List active accounts
  - gcloud **projects**
     - gcloud projects **add-iam-policy-binding** - Add IAM policy binding
     - gcloud projects **get-iam-policy** - Get IAM policy for a project
     - gcloud projects **remove-iam-policy-binding** - Remove IAM policy binding
     - gcloud projects **set-iam-policy** - Set the IAM policy
     - gcloud projects **delete** - Delete a project
  - gcloud **iam**
     - gcloud iam **roles describe** - Describe an IAM role
     - gcloud iam **roles create** - create an iam role(--project, --permissions, --stage)
     - gcloud iam **roles copy** - Copy IAM Roles


## Service Accounts

![compute-instance-card](https://user-images.githubusercontent.com/57451228/151099384-7b145f40-ffec-454d-bade-ff33075ed326.png)

&emsp; &emsp; &emsp; &emsp; &emsp; ![arrowtd](https://user-images.githubusercontent.com/57451228/151099390-d9f26182-482e-454b-a6cb-4dc8af31e750.png)

&emsp; &emsp; ![storage-card](https://user-images.githubusercontent.com/57451228/151099393-76939f0d-d1a7-4ad0-8d88-8bde1fa15c59.png)

  
  
- Scenario: An Application on a VM needs access to cloud storage
  - You DONT want to use personal credentials to allow access
- (RECOMMENDED) Use **Service Accounts**
  - Identified by an email address (Ex: id-compute@developer.gserviceaccount.com)
  - Does NOT have password
     - Has a private/public RSA key-pairs
     - Can't login via browsers or cookies
- Service account types:
  - **Default service account** - Automatically created when some services are used
     - (NOT RECOMMENDED) Has Editor role by default
  - **User Managed** - User created
     - (RECOMMENDED) Provides fine grained access control
  - **Google-managed service** accounts - Created and managed by Google
     - Used by GCP to perform operations on user's behalf
     - In general, we DO NOT need to worry about them


## Use case 1 : VM <-> Cloud Storage
![compute-instance-card-1](https://user-images.githubusercontent.com/57451228/151099643-4201d912-e28f-4afd-af98-65deef5646bd.png) ![arrow-card](https://user-images.githubusercontent.com/57451228/151099662-988e2a6c-828b-4961-bb71-3488a785d595.png) ![storage-card-1](https://user-images.githubusercontent.com/57451228/151099666-349056d2-3dad-4b44-a701-a13ee5466b50.png)

- 1: Create a Service Account Role with the right permissions
- 2: Assign Service Account role to VM instance
- **Uses Google Cloud-managed keys:**
  - Key generation and use are automatically handled by IAM when we assign a service account to the instance
  - Automatically rotated
  - No need to store credentials in config files
- **Do NOT delete** service accounts used by running instances:
  - Applications running on those instances will lose access!


## Use case 2 : On Prem <-> Cloud Storage (Long Lived)
 
 
&emsp; &emsp; ![user-card](https://user-images.githubusercontent.com/57451228/151100545-1564122d-c01a-41cf-acec-5c44a49d335d.png)

&emsp; &emsp; &emsp; &emsp; ![arrowtd](https://user-images.githubusercontent.com/57451228/151100580-14fd02cf-da12-42e4-955b-b3feb03bfdbf.png)

 &emsp; ![storage-card](https://user-images.githubusercontent.com/57451228/151100587-3fcba4c0-9bd5-4f5a-9e4e-cedad8c88d64.png)

 
- You **CANNOT assign Service Account directly to an On Prem App**
- 1: Create a **Service Account** with right permissions
- 2: Create a **Service Account User Managed Key**
  - **gcloud iam service-accounts keys create**
  - Download the service account key file
     - Keep it secure (It can be used to impersonate service account)!
- 3: Make the service account key file accessible to your application
  - Set environment variable GOOGLE_APPLICATION_CREDENTIALS
     - export GOOGLE_APPLICATION_CREDENTIALS="/PATH_TO_KEY_FILE"
- 4: Use **Google Cloud Client Libraries**
  - Google Cloud Client Libraries use a library - Application Default Credentials (ADC)
     - ADC uses the service account key file if env var GOOGLE_APPLICATION_CREDENTIALS exists!



## Use case 3 : On Prem <-> Google Cloud APIs (Short Lived)

- **Make calls from outside GCP to Google Cloud APIs** with short lived permissions
  - Few hours or shorter
  - Less risk compared to sharing service account keys!
- **Credential Types:**
  - OAuth 2.0 access tokens
  - OpenID Connect ID tokens
  - Self-signed JSON Web Tokens (JWTs)
- **Examples**:
  - When a member needs elevated permissions, he can assume the service account role (Create OAuth 2.0 access token for service account)
  - OpenID Connect ID tokens is recommended for service to service authentications:
     - A service in GCP needs to authenticate itself to a service in other cloud



## Service Account Use case Scenarios

|Scenario	|Solution|
|:--:|-|
|Application on a VM wants to talk to a Cloud Storage bucket	|Configure the VM to use a Service Account with right permissions|
|Application on a VM wants to put a message on a Pub Sub Topic	|Configure the VM to use a Service Account with right permissions|
|Is Service Account an identity or a resource? |	It is both. You can attach roles with Service Account (identity). You can let other members access a SA by granting them a role on the Service Account (resource).|
|VM instance with default service account in Project A needs to access Cloud Storage bucket in Project B	| In project B, add the service account from Project A and assign Storage Object Viewer Permission on the bucket|





## ACL (Access Control Lists)
- **ACL**: Define **who** has access to your buckets and objects, as well as **what level** of access they have
- **How is this different from IAM?**
  - IAM permissions apply to all objects within a bucket
  - ACLs can be used to customized specific accesses to different objects
- User gets access if he is allowed by either IAM or ACL!
- (Remember) **Use IAM for common permissions** to all objects in a bucket
- (Remember) **Use ACLs** if you need to **customize access to individual objects**



## Access Control - Overview

![iam](https://user-images.githubusercontent.com/57451228/151100030-2063b1d3-e455-4920-8991-74e767c126a3.png)


- How do you control access to objects in a Cloud Storage bucket?
- Two types of access controls:
  - **Uniform** (Recommended) - Uniform bucket level access using IAM
  - **Fine-grained** - Use IAM and ACLs to control access:
     - Both bucket level and individual object level permissions
- Use Uniform access when all users have same level of access across all objects in a bucket
- Fine grained access with ACLs can be used when you need to customize the access at an object level
  - Give a user specific access to edit specific objects in a bucket



## Cloud Storage - Signed URL

- You would want to **allow a user limited time access** to your objects:
  - Users do NOT need Google accounts
- Use **Signed URL** functionality
  - A URL that gives **permissions for limited time duration** to perform specific actions
- **To create a Signed URL:**
  - 1: Create a key (YOUR_KEY) for the Service Account/User with the desired permissions
  - 2: Create Signed URL with the key:
     - gsutil signurl -d 10m YOUR_KEY gs://BUCKET_NAME/OBJECT_PATH




## Cloud Storage - Static website
  
![user-card](https://user-images.githubusercontent.com/57451228/151099801-0321f8dc-2ff4-4205-ad89-2c5e2e234028.png). ![arrow-card](https://user-images.githubusercontent.com/57451228/151099815-e2248426-ccc8-4a5f-925b-53b7c94af0e2.png). ![storage-card](https://user-images.githubusercontent.com/57451228/151099825-4422289a-cdab-4f08-a27f-6da6d2a87d8c.png)

- 1: Create a bucket with the **same name** as website name (Name of bucket should match DNS name of the website)
  - Verify that the domain is owned by you
- 2: Copy the files to the bucket
  - Add index and error html files for better user experience
- 3: Add member **allUsers** and grant **Storage Object Viewer** option
  - Select **Allow Public Access**

<BR/>
<BR/>

<pre>
Thank You for Choosing to Learn from in28Minutes

Author
- <a href="https://www.linkedin.com/in/rangakaranam/">Ranga Rao Karanam</a>

Helping Hand
- <a href="https://www.linkedin.com/in/debrup-365/">Debrup ❤️</a>
</pre>
