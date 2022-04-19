---
layout:     post
title:      GCP Resource Hierarchy, Roles and Identities - GCP Certification Cheat Sheet
date:       2022-03-31 00:00:00
summary:    Let's get a quick overview of resource hierarchy and billing in google cloud and what roles, identities helps you setup the right hierachy for your google cloud workloads 
categories:  GCP_CLOUD General
permalink:  /gcp-certification-region-availability-zones-az
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
![](./images/02-architecture/resource-hierarchy-overview.png)
source: (https://cloud.google.com)
- **Well defined hierarchy**:
	- Organization > Folder > Project > Resources
- **Resources** are created in projects
- A **Folder** can contain multiple projects
- **Organization** can contain multiple Folders

- Organization 
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
- Folder
    - building blocks of multi-layer organizational hierarchies
    - folders can contain other folders and projects
    - Folders Organization - Normally based on the services provided by the resources in the contained projects & policies governing the folders and projects
- Project
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
![](./images/00-icons/gcp/iam.png)
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
![](./images/02-architecture/00-policy-role-resource.png)

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

## Typical identity management in the cloud
![](./images/00-icons/gcp/iam.png)
- You have **resources** in the cloud (examples - a virtual server, a database etc)
- You have **identities (human and non-human)** that need to access those resources and perform actions 
	- For example: launch (stop, start or terminate) a virtual server
- How do you **identify users** in the cloud?
	- How do you configure resources they can access? 
	- How can you configure what actions to allow?
- In GCP: *Identity and Access Management (Cloud IAM)* provides this service

## Cloud Identity and Access Management (IAM)
![](./images/00-icons/gcp/iam.png)
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
![](./images/00-icons/gcp/user-card.png)
![](./images/arrowtd.png)
![](./images/00-icons/gcp/storage-card.png)
- I want to provide access to manage a specific cloud storage bucket to a colleague of mine:
	- Important Generic Concepts:
		- **Member**: My colleague
		- **Resource**: Specific cloud storage bucket
		- **Action**: Upload/Delete Objects
	- In Google Cloud IAM:
		- **Roles**: A set of permissions (to perform specific actions on specific resources)
			- **Roles do NOT know about members**. It is all about permissions!
		- How do you assign permissions to a member?
			- **Policy**: You assign (or **bind**) a role to a member
- 1: **Choose a Role** with right permissions (Ex: Storage Object Admin)
- 2: **Create Policy** binding member (your friend) with role (permissions)
- IAM in AWS is very different from GCP (Forget AWS IAM & Start FRESH!)
	- Example: Role in AWS is NOT the same as Role in GCP

## IAM - Roles
![](./images/00-icons/gcp/iam.png)
- **Roles are Permissions**:
	- Perform some set of actions on some set of resources
- Three Types:
	- **Basic Roles (or Primitive roles)** - Owner/Editor/Viewer
		- **Viewer(roles.viewer)** - Read-only actions
		- **Editor(roles.editor)** - Viewer + Edit actions 
		- **Owner(roles.owner)** - Editor + Manage Roles and Permissions + Billing
		- EARLIEST VERSION: Created before IAM
		- NOT RECOMMENDED: **Don't use in production**
	- **Predefined Roles** - Fine grained roles predefined and managed by Google
		- Different roles for different purposes
		- **Examples**: Storage Admin, Storage Object Admin, Storage Object Viewer, Storage Object Creator
	- **Custom Roles** - When predefined roles are NOT sufficient, you can create your own custom roles

## IAM - Predefined Roles - Example Permissions
![](./images/00-icons/gcp/iam.png)
- Important **Cloud Storage Roles**:
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
![](./images/02-architecture/00-roles.png)

- **Member** : Who?
- **Roles**  : Permissions (What Actions? What Resources?)
- **Policy** : Assign Permissions to Members
	- Map Roles (What?) , Members (Who?) and Conditions (Which Resources?, When?, From Where?)
	- Remember: Permissions are NOT directly assigned to Member
		- Permissions are represented by a Role
		- Member gets permissions through Role!
- A Role can have multiple permissions
- You can assign multiple roles to a Member

## Service Accounts
![](./images/00-icons/gcp/compute-instance-card.png)
![](./images/arrowtd.png)
![](./images/00-icons/gcp/storage-card.png)

- Scenario: An Application on a VM needs access to cloud storage
	- You DONT want to use personal credentials to allow access
- (RECOMMENDED) Use **Service Accounts**
	- Identified by an email address (Ex: id-compute@developer.gserviceaccount.com)
	- Does NOT have password
		- Has a **private/public RSA key-pairs**
		- Can't login via browsers or cookies
- Service account types:
    - **Default service account** - Automatically created when some services are used
    	- (NOT RECOMMENDED) Has **Editor role** by default
    - **User Managed** - User created
    	- (RECOMMENDED) Provides fine grained access control
    - **Google-managed service** accounts - Created and managed by Google
    	- Used by GCP to perform operations on user's behalf
    	- In general, we DO NOT need to worry about them


Question: You are designing cloud applications for a insurance company. The customer information system is for managing the customers details. This system can be accessed by customer service department and sales team. The patient information system is responsible for receiving, storing, analysing the patient information
submitted for claiming medical insurance. This information is sensitive and only small set of employees should access this. Another application which manages the regulatory reporting has the requirement to run isolated from other software systems. How to design the resource hierarchy to meet these requirements?

1. One organization resource, which has 3 different folders for customer information system, patient information system and regulatory reporting system. Common constraints would be declared in org-level policies. Specific policies would be defined at individual folder level.
2. One organization resource, with two sub-folders one for customer information system and another for regulatory reporting system. The customer information folder also contains another folder for patient information system. No common constraints at organization level. Specific policies would be defined at individual folder level.
3. One organization resource, which has 3 different folders for customer information system, patient information system and regulatory reporting system. All constraints would be declared in org-level policies. Same policies would be defined at individual folder level.
4. No Organization resource, 3 different folders for customer information system, patient information system and regulatory reporting system. Specific policies would be defined at individual folder level.

Ans 1: Option 1 is the most flexible solution for this scenario because common constraints can be declared at Organization level and specific constraints can be declared at individual folder level. 
Option 2 is less flexible compared to option 1 because patient information system is part of customer information system folder. So defining restrictive policies are difficult at the customer information system folder. This is not a wrong solution per se but Option 1 is better suited
Option 3 is not correct because you can't declare all the policies at Organization level and achieve optimal results. Different systems have different requirements so declaring them at folder levels gives more flexibility
Option 4 At enterprise level not defining Organization is not an option
---
Question: You are a Cloud administrator in an banking corporation. It comes to your notice that, teams are using the serial port of the VM to do debugging that also causes a security violation. Your security team instructs the operations team to disable the serial port access to all VM's across all the projects in the Organization. How can you achieve this?

1. Implement security control at each individual VM to disable serial port access. Also instruct team members to use the golden image which has this security control implemented
2. Implement constraints at the individual project level so that any current and future VM's will have this constraints inherited. 
3. Implement constraints at the Organization level so that any current and future VM's will have this constraints inherited. 
4. Create a folder under Organization level and bring all the projects under the folder. Then define constraints at the folder level.

Ans 4: Implement constraints at the Organization level so that any current and future VM's will have this constraints inherited is the correct answer. This gives the coverage at the broader level and also can be managed at single place. 
Option 2 is not valid because it involves more work and also when a new project gets created, there is a chance this gets missed. 
Option 4 is not valid because it involves more work and also when a new project gets created, there is a chance this gets missed.
Option 1 is the least preferred option as this has to be enabled at each individual VM level and that is not a good solution.
---

Question: You are joining a small company as GCP architect and you notice some developers creating projects in GCP and paying for the resources using their personal credit cards. The company's account department has to reimburse and this is creating too much work. The CEO wants all the projects under a single billing account for better finance control. What is the best way to achieve this?
1. Contact google support team via email for a corporate billing account for the company
2. In the GCP console, create a new billing account and update the payment method for the company. Move the projects under the Organization using Resource manager API.
3. Contact google support team through phone for a corporate billing account for the company
4. Ask the developers to use corporate credit cards instead of personal credit cards. 

Ans 2: In the GCP console, create a new billing account and update the payment method for the company. Move the projects under the Organization using Resource manager API. is the correct answer as GCP allows the creation of new billing account through the console itself. 
Option 1 & 3 is not needed as this can be achieved using self-service
Option 4 is not a optimal solution to solve this problem.
---
Question: You are a GCP cloud architect working with a health care provider to setup their GCP infrastructure and migrate the applications to the cloud. Due to cost pressure, the CFO wants to have the detailed analysis of all the costs incurred with the use of Cloud resources to be analyzed so cost can be controlled and optimized. The accounting department has little bit of experience with running SQL queries. What solution you would propose to get the cost details by resource type for various time periods?
1. The billing screen provides detailed reporting option as well which can be used 
2. The billing details can be exported to cloud storage and SQL like queries can be run directly on the cloud storage
3. The billing details can be exported to Bigtable for analysis and SQL like queries can be executed to generate various insights
4. The billing details can be exported to Bigquery for analysis and SQL like queries can be executed to generate various insights

Ans Option 4: The billing details can be exported to Bigquery for analysis and SQL like queries can be executed to generate various insights is the recommended solution for this. https://cloud.google.com/billing/docs/how-to/export-data-bigquery 
Option 1 is not correct because though you can see the details in the Billing details screen, for historic data and analysis you need the data in BigQuery
Option 2 is mainly used for archiving purpose and not for the usecase where analysis is needed
Option 3 is not correct because Bigtable is not suitable for this usecase and BigQuery is more suitable.
---
Question: You are a GCP operations architect working for a retail giant. Your accounts team is requesting you to split the current billing account for better cost control and create two more new billing accounts. Also some of the existing projects should be linked to these newly created billing accounts. How this can be achieved?
1. You should have Billing Account Creator role to create a new billing accounts. Then should have Project Billing Manager in combination with Billing Account User role to link/unlink the existing projects to this new Billing Account.
2. You should have Billing Account Creator role to create a new billing accounts. Then should have Project Billing Manager role to link/unlink the existing projects to this new Billing Account.
3. You should have Billing Account Administrator role to create a new billing accounts. Then should have Project Billing Manager role to link/unlink the existing projects to this new Billing Account.
4. You should have Billing Account Administrator role to create a new billing accounts. Then should have Project Billing Manager role to link/unlink the existing projects to this new Billing Account.

Ans 1: You should have Billing Account Creator role to create a new billing accounts. Then should have Project Billing Manager in combination with Billing Account User role to link/unlink the existing projects to this new Billing Account is the right answer. Billing account creator role allows the creation of billing accounts. Though the Project Billing Manager roles allows you to link/unlink billing account to a project, You need Billing Account User role as well. From the documentation

"This role has very restricted permissions, so you can grant it broadly. When granted in combination with Project Creator, the two roles allow a user to create new projects linked to the billing account on which the Billing Account User role is granted. Or, when granted in combination with the Project Billing Manager role, the two roles allow a user to link and unlink projects on the billing account on which the Billing Account User role is granted."

https://cloud.google.com/billing/docs/how-to/billing-access#overview-of-cloud-billing-roles-in-cloud-iam

Option 2 You should have Billing Account Creator role to create a new billing accounts. Then should have Project Billing Manager role to link/unlink the existing projects to this new Billing Account is not correct because only the Project Billing Manager role is not sufficient to link/unlink the project to the billing account. From the documentation (Project Owner or Project Billing Manager on the project, AND Billing Account Administrator or Billing Account User for the target Cloud Billing account.) https://cloud.google.com/billing/docs/how-to/modify-project#change_the_billing_account_for_a_project

Option 3 You should have Billing Account Administrator role to create a new billing accounts. Then should have Project Billing Manager role to link/unlink the existing projects to this new Billing Account. is not correct because Billing Account Administrator can't create new billing account

Option 4 You should have Billing Account Administrator role to create a new billing accounts. Then should have Project Billing Manager role to link/unlink the existing projects to this new Billing Account is not correct because Billing Account Administrator can't create new billing account
---
Question: You are a GCP operations architect working for a banking client. You are setting up the cloud environment and you need to set up billing and create projects to link with the billing account. What permissions you should possess to achieve this?

1. You should have Billing Account Creator role to create a new billing accounts. Then should have Project Creator in combination with Billing Account User role to link/unlink the newly created projects to this new Billing Account.
2. You should have Billing Account Creator role to create a new billing accounts. Then should have Project Billing Manager role to link/unlink the new projects to this new Billing Account.
3. You should have Billing Account Administrator role to create a new billing accounts. Then should have Project Billing Manager role to link/unlink the new projects to this new Billing Account.
4. You should have Billing Account Administrator role to create a new billing accounts. Then should have Project Billing Manager role to link/unlink the new projects to this new Billing Account.

Ans 1: You should have Billing Account Creator role to create a new billing accounts. Then should have Project Creator in combination with Billing Account User role to link/unlink the newly created projects to this new Billing Account. is the correct answer. Billing account creator role allows the creation of billing accounts and Project creator role allows the creation of projects. This in combination with Billing Account User role allow a user to create new projects linked to the billing account on which the Billing Account User role is granted. From the documentation

"This role has very restricted permissions, so you can grant it broadly. When granted in combination with Project Creator, the two roles allow a user to create new projects linked to the billing account on which the Billing Account User role is granted. Or, when granted in combination with the Project Billing Manager role, the two roles allow a user to link and unlink projects on the billing account on which the Billing Account User role is granted."

https://cloud.google.com/billing/docs/how-to/billing-access#overview-of-cloud-billing-roles-in-cloud-iam

Option 2 You should have Billing Account Creator role to create a new billing accounts. Then should have Project Billing Manager role to link/unlink the new projects to this new Billing Account is not correct because only the Project Billing Manager role is not sufficient. You also need the Project Creator role to create new projects. From the documentation (Project Owner or Project Billing Manager on the project, AND Billing Account Administrator or Billing Account User for the target Cloud Billing account.) https://cloud.google.com/billing/docs/how-to/modify-project#change_the_billing_account_for_a_project

Option 3 You should have Billing Account Administrator role to create a new billing accounts. Then should have Project Billing Manager role to link/unlink the new projects to this new Billing Account. is not correct because Billing Account Administrator can't create new billing account and also You also need the Project Creator role to create new projects

Option 4 You should have Billing Account Administrator role to create a new billing accounts. Then should have Project Billing Manager role to link/unlink the new projects to this new Billing Account is not correct because Billing Account Administrator can't create new billing account. You also need the Project Creator role to create new projects
---
Question: You are a GCP operations architect working for a fintech client. You have IT team and accounts team among other teams. You would like the accounts team to link the projects to the correct Billing Accounts but other than that, they should not have any access to the resources in the project itself. What is the best way to set this up?

1. The accounts team should be granted Project Billing Manager & Billing Account User for the projects they want to work with. This allows them to link and unlink the projects as per their need.
2. The accounts team should be granted Billing Account User role for the projects they want to work with. This allows them to link and unlink the projects as per their need.
3. The accounts team should be granted Billing Account Administrator role. This allows them to link and unlink the projects as per their need.
4. The accounts team should be granted Billing Account Creator role. This allows them to link and unlink the projects as per their need.

Ans Option 1: The accounts team should be granted Project Billing Manager & Billing Account User for the projects they want to work with. This allows them to link and unlink the projects as per their need. is the correct answer. These two roles in combination with each other, provides the right level of permissions to link and unlink the projects to the right billing account. 
Option 2: The accounts team should be granted Billing Account User role for the projects they want to work with. This allows them to link and unlink the projects as per their need. is partially correct but this role alone is very restrictive. This role has to be assigned in combination with Project Billing Manager
Option 3: The accounts team should be granted Billing Account Administrator role . This allows them to link and unlink the projects as per their need. is technically correct but this gives them additional permissions which is not required
Option 4: The accounts team should be granted Billing Account Creator role. This allows them to link and unlink the projects as per their need. is incorrect. This roles provides access to create Billing Accounts which is not the requirement.
---
Open Discussion: Question: You are working for a company Monster Inc which uses GCP for running it's IT systems. Your company acquires another company which also uses GCP. Your CTO would like to use a single Organization strategy to consolidate the cloud costs and generate a single consolidated cost statement. What is the best approach?

1. Move the projects to the Monster Inc. Organization. Update the billing accounts for each project to the Monster Inc.'s billing account.
2. Move the projects to the Monster Inc. Organization. This is sufficient to generate a consolidated billing statement
3. There is no need to move the projects under a single Organization. Just update the billing account to same billing account in both Organizations
4. There is no need to move the projects under a single Organization. Just inform GCP to generate a consolidated billing statement for both Organizations

---
Question: Your company has received higher invoice than expected from the GCP usage. Looking at the higher cost, the accounts department would like to setup budget across projects in the Organization and would like to receive alerts whenever the costs crosses the 75% of the budget. How to set this up? Select all the options required.
1. Ensure you have Billing Account Administrator role or Billing Account Cost Manager role. 
2. Ensure you have Billing Accoung Administrator role and Billing Account User role
3. Select the Billing Account and setup budget and alerts for all the projects linked with the Billing Account
4. Select the Billing Account and setup budget and alerts for one of the projects linked with the Billing Account
5. Ensure you have a Project Administrator role and setup budget and alerts for all the projects linked with the Billing Account

Option 1 (Ensure you have Billing Account Administrator role or Billing Account Cost Manager role.) & 3 (Select the Billing Account and setup budget and alerts for all the projects linked with the Billing Account) are the right options. To create budget and alerts you need one of the above permissions. GCP allows very flexible budget and alert options using which this can be easily setup. 
https://cloud.google.com/billing/docs/how-to/budgets#overview
Option 2 is not correct because you don't need the Billing Account User role to create the budgets and alerts. 
Option 4 **Select the Billing Account and setup budget and alerts for one of the projects linked with the Billing Account** is incorrect because this option talks about setting up budgets and alerts for one of the projects and not all the projects
Option 5 **Ensure you have a Project Administrator role and setup budget and alerts for all the projects linked with the Billing Account** is not correct because Project Administrator role is not sufficient to setup the billing budget and alerts.
---
Question: The cost budgetting team in your company would like to manage the budgets and manage the export of billing cost data to BigQuery. No additional permissions are required for this team in line with restricted privilage principle. This is to help them plan the budget for the period. How this can be achieved?
1. Provide the budget team with the role of Billing Account Costs Manager (roles/billing.costsManager)
2. Provide the budget team with the role of Billing Account Administrator (roles/billing.admin)
3. Provide the budget team with the role of Billing Account Viewer (roles/billing.viewer)
4. Provide the budget team with the role of Billing Account User (roles/billing.user)

Ans: Provide the budget team with the role of Billing Account Costs Manager (roles/billing.costsManager) is the correct answer. From the documentation "Create, edit, and delete budgets, view billing account cost information and transactions, and manage the export of billing cost data to BigQuery. Does not confer the right to export pricing data or view custom pricing in the Pricing page. Also, does not allow the linking or unlinking of projects or otherwise managing the properties of the billing account."
Option 2 Provide the budget team with the role of Billing Account Administrator (roles/billing.admin) is not the correct answer. This role is an owner role for a billing account. Use it to manage payment instruments, configure billing exports, view cost information, link and unlink projects and manage other user roles on the billing account.
Option 3 Provide the budget team with the role of Billing Account Viewer (roles/billing.viewer) is also not correct. Billing Account Viewer access would usually be granted to finance teams, it provides access to spend information, but does not confer the right to link or unlink projects or otherwise manage the properties of the billing account.
Option 4 Provide the budget team with the role of Billing Account User (roles/billing.user) is also not correct. This role has very restricted permissions, so you can grant it broadly. When granted in combination with Project Creator, the two roles allow a user to create new projects linked to the billing account on which the Billing Account User role is granted. Or, when granted in combination with the Project Billing Manager role, the two roles allow a user to link and unlink projects on the billing account on which the Billing Account User role is granted.
---
Question: The finance team in your company would like to have view only rights to the billing details. No additional permissions are required for this team in line with restricted privilage principle. This is to help them plan the budget for the period. How this can be achieved?
1. Provide the finance team with the role of Billing Account Costs Manager (roles/billing.costsManager)
2. Provide the finance team with the role of Billing Account Administrator (roles/billing.admin)
3. Provide the finance team with the role of Billing Account Viewer (roles/billing.viewer)
4. Provide the finance team with the role of Billing Account User (roles/billing.user)

Ans: Provide the budget team with the role of Billing Account Costs Manager (roles/billing.costsManager) is not the correct answer. From the documentation "Create, edit, and delete budgets, view billing account cost information and transactions, and manage the export of billing cost data to BigQuery. Does not confer the right to export pricing data or view custom pricing in the Pricing page. Also, does not allow the linking or unlinking of projects or otherwise managing the properties of the billing account."
Option 2 Provide the budget team with the role of Billing Account Administrator (roles/billing.admin) is not the correct answer. This role is an owner role for a billing account. Use it to manage payment instruments, configure billing exports, view cost information, link and unlink projects and manage other user roles on the billing account.
Option 3 Provide the budget team with the role of Billing Account Viewer (roles/billing.viewer) is the correct answer. Billing Account Viewer access would usually be granted to finance teams, it provides access to spend information, but does not confer the right to link or unlink projects or otherwise manage the properties of the billing account.
Option 4 Provide the budget team with the role of Billing Account User (roles/billing.user) is also not correct. This role has very restricted permissions, so you can grant it broadly. When granted in combination with Project Creator, the two roles allow a user to create new projects linked to the billing account on which the Billing Account User role is granted. Or, when granted in combination with the Project Billing Manager role, the two roles allow a user to link and unlink projects on the billing account on which the Billing Account User role is granted.
---




