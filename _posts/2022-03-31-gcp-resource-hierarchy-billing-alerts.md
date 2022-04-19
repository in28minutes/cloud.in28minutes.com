---
layout:     post
title:      GCP Resource Hierarchy, Roles and Identities - GCP Certification Cheat Sheet
date:       2022-03-31 00:00:00
summary:    Let's get a quick overview of resource hierarchy and billing in google cloud and what roles, identities helps you setup the right hierachy for your google cloud workloads 
categories:  GCP_CLOUD General
permalink:  /gcp-certification-resource-hierarchy
---

Let's get a quick overview of resources hierachy from an GCP certification perspective. We will look at important certification questions regarding resource hierarchy, billing, roles and identities.

## You will learn
- What is a Resource Hierarchy?
- Why it is important and how to set it up?
- What are the important roles necessary?

## GCP Certification Study Material and Notes - 25 PDF Cheat Sheets

Each cheat sheet contains:
- FAQs and Tutorials with 5-20 slides
- Study Material and Notes to quickly review and prepare for certification exam
- Certification Exam Tips
- Certification and Interview Scenario Questions

<div>
 <a href="https://links.in28minutes.com/cloud-in28minutes-teachable-free-link" target="_blank" class="button instagram">Download</a>
</div>

## Resource Hierarchy in GCP

![](./gcpimages/02-architecture/resource-hierarchy-overview.png)
source: (https://cloud.google.com)

- **Well defined hierarchy**:
	- Organization > Folder > Project > Resources
- **Resources** are created in projects
- A **Folder** can contain multiple projects
- **Organization** can contain multiple Folders

- **Organization** 
    - **G-Suite domain** or **Cloud Identity** maps to Organization
    - One Cloud Identity assigns to atmost one Organization
    - Cloud Identity
        - Have Super admins
        - They assign the IAM role of Organization administrator to users
    - Users with Organization administrator role is responsible for
        - Defining the structure of the resource hierarchy
        - Defining IAM policies over the resource hierarchy
        - Delegation of other management roles to other users
    - GCP automatically assigns the **Project Creator** and **Billing Account Creator** IAM roles to all users in domain
    - This allows any user to create projects and enable billing for the cost of resources
- **Folder**
    - building blocks of multi-layer organizational hierarchies
    - folders can contain other folders and projects
    - Folders Organization - Normally based on the services provided by the resources in the contained projects & policies governing the folders and projects
- **Project**
    - Important part of the hierachy
    - Contains resources, GCE services, permissions and manage billing options
    - Anyone with **resourcemanager.projects.create** IAM permission can create project
    - By default when Organization get created, everyone in the domain is granted that permission
    - Organization has quota of number of projects that can be created

## Resource Hierarchy - Recommendations for Enterprises

- Create **separate projects for different environments**:
	- Complete isolation between test and production environments
- Create **separate folders for each department**:
	- Isolate production applications of one department from another
	- We can create a shared folder for shared resources
- **One project per application per environment**: 
	- Let's consider two apps: "A1" and "A2"
	- Let's assume we need two environments: "DEV" and "PROD"
	- In the ideal world you will create four projects: A1-DEV, A1-PROD, A2-DEV, A2-PROD:
		- Isolates environments from each other
		- DEV changes will NOT break PROD
		- Grant all developers complete access (create, delete, deploy) to DEV Projects
		- Provide production access to operations teams only!

## Billing Accounts

- **Billing Account** is mandatory for creating resources in a project:
	- Billing Account contains the payment details
	- Every Project with active resources should be associated with a Billing Account
- Billing Account can be associated with one or more projects
- You can have multiple billing accounts in an Organization
- (RECOMMENDATION) Create Billing Accounts representing your organization structure:
	- A startup can have just one Billing account
	- A large enterprise can have a separate billing account for each department
- Two Types:
	- **Self Serve** : Billed directly to Credit Card or Bank Account
	- **Invoiced** : Generate invoices (Used by large enterprises)

## Managing Billing - Budget, Alerts and Exports

- Setup a **Cloud Billing Budget** to avoid surprises:
	- (RECOMMENDED) Configure **Alerts** 
	- Default alert thresholds set at 50%, 90% & 100%
		- Send alerts to Pub Sub (Optional)
		- Billing admins and Billing Account users are alerted by e-mail
- Billing data can be **exported (on a schedule)** to:
	- **Big Query** (if you want to query information or visualize it)
	- **Cloud Storage** (for history/archiving)

## Organization Policy Service

![](./gcpimages/00-icons/gcp/iam.png)

- How to enable **centralized constraints** on all resources created in an Organization?
	- Configure **Organization Policy**
	- Example: Disable creation of Service Accounts
	- Example: Allow/Deny creation of resources in specific regions
- Needs a Role - Organization Policy Administrator
- (Remember) **IAM** focuses on **Who** 
	- Who can take specific actions on resources?
- (Remember) Organization Policy focuses on **What** 
	- What can be done on specific resources?

## Resource Hierarchy & IAM Policy

![](./gcpimages/02-architecture/00-policy-role-resource.png)

- IAM Policy can be set at any level of the hierarchy
- Resources inherit the policies of **All parents**
- The effective policy for a resource is the union of the policy on that resource and its parents
- Policy inheritance is transitive:
	- For example: Organization policies are applied at resource level
- You can't restrict policy at lower level if permission is given at an higher level

## Organization, Billing and Project Roles

- **Organization Administrator**
	- Define Resource Hierarchy
	- Define Access Management Policies
	- Manage other users and roles
- **Billing Account Creator** - Create Billing Accounts
- **Billing Account Administrator** - Manage Billing Accounts (payment instruments, billing exports, link and unlink projects, manage roles on billing account)
	- CANNOT create a Billing Account
- **Billing Account User** - Associate Projects with Billing Accounts
	- Typically used in combination with **Project Creator**
	- These two roles allow user to create new project and link it with billing account
- **Billing Account Viewer** - See all Billing Account details

## Billing Roles - Quick Review

| Roles| Description | Use Case|
|:--|:--|
| Billing Account Creator | Permissions to create new billing accounts |Finance Team|
| Billing Account Administrator | Manages billing account but can't create them |Finance Team|
| Billing Account User | Assigns projects to billing accounts |Project Owner|
| Billing Account Viewer | View only access to billing account |Auditor|
| Billing Account Costs Manager | Manage budgets, view & export cost information of billing accounts | budget Team|
| Project Billing Manager | Link/UnLink the project to/from billing account | Project Owners |

## Organization, Billing and Project Roles - Scenarios

- **Scenario 1**: I'm creating a project and I want to associate an existing billing account with the project 
	- Roles needed : Project Creator and Billing Account User (link project to billing account)
- **Scenario 2**: I'm a billing auditor 
	- Roles needed : Billing Account Viewer role




