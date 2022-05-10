---
Question: You have a application that should process the messages comes from the Pub/Sub and update the CloudSQL DB. You would like to run this as Cloud Run application. To integrate with Pub/Sub what is the best possible solution from the given options?
1. Integrate Cloud Run directly with Pub/Sub. Run the command **gcloud pubsub subscriptions create myRunSubscription --topic myRunTopic --push-endpoint=SERVICE-URL**. This creates a subscription and whenever message is received, it automatically published to the SERICE-URL your application is exposing.
2. Create a Cloud Function which gets triggered whenever message received in the Pub/Sub. Write a logic in the Cloud Function which invokes the SERVICE-URL with the contents of the message
3. Create a Service Account. Assign the role roles/run.invoker to this Service Account for this Cloud Run application. Also allow Pub/Sub to create authentication tokens on the project of the Cloud Run application. Create the Pub/Sub subscription with the Service Account.
4. Create a Service Account. Also allow Pub/Sub to create authentication tokens on the project of the Cloud Run application. Create the Pub/Sub subscription with the Service Account.

Ans Option 3: Create a service account. Assign the role roles/run.invoker to this service account for this Cloud Run application. Also allow Pub/Sub to create authentication tokens on the project of the Cloud Run application. Create the Pub/Sub subscription with the service account. is the correct answer. For the integration to work, the best way to do this is through a service account and assigning the run.invoker role for the service sccount. More details are here https://cloud.google.com/run/docs/tutorials/pubsub#integrating-pubsub.
Option 4 Create a Service Account. Also allow Pub/Sub to create authentication tokens on the project of the Cloud Run application. Create the Pub/Sub subscription with the service account. is not correct as this solution missing the assignment of roles/run.invoker to the service account.
Option 1 Integrate Cloud Run directly with Pub/Sub. Run the command **gcloud pubsub subscriptions create myRunSubscription --topic myRunTopic --push-endpoint=SERVICE-URL**. This creates a subscription and whenever message is received, it automatically published to the SERICE-URL your application is exposing. is not correct. This gcloud command has an option to specific service account which needs to be created as explained in the option 3. 
---
Question: You are creating an application as Cloud Function which creates a Thumbnail for the images uploaded in the Cloud Storage. You notice that, for some of the bigger images were not processed correctly. What could be the cause of the problems?
1. The timeout settings for the Cloud Function is too low to process larget images
2. Copying larger images takes more time so the trigger function is not correctly working
3. To process larger images, the role roles/function.processLargeImage should be assigned to the function
4. The Cloud Function has a defect when processing larger images which cause the processing to fail.

Ans: **Option 1: The timeout settings for the Cloud Function is too low to process large images** is the correct answer. 
Option 2: Copying larger images takes more time so the trigger function is not correctly working is not correct as triggering will happen irrespective of size of the file. 
Option 3: To process larger images, the role roles/function.processLargeImage should be assigned to the function is not correct as there is no role called roles/function.processLargeImage
Option 4: The Cloud Function has a defect when processing larger images which cause the processing to fail. is not correct
---
Question: What is the default timeout settings for the Cloud Funtion?
1. 1 minute
2. 10 minute
3. 5 minute
4. 9 minute

Ans Option 1: 1 minute is the default timeout settings for the Cloud Function. 9 minute is the maximum
All other options are invalid.
---
Question: What is the maximum timeout settings for the Cloud Funtion?
1. 1 minute
2. 10 minute
3. 5 minute
4. 9 minute

Ans Option 4: 9 minute is the maximum timeout settings for the Cloud Function. 1 minute is the default timeout settings.
All other options are invalid.
---
Question: Which one of the following GCP resources can NOT generate events that can trigger a Cloud Function?
1. Cloud Pub/Sub
2. Cloud Logging
3. Cloud Storage
4. Cloud SQL

Ans Option 4: is the correct answer. The Cloud Functions supports events from the following providers
HTTP
Cloud Storage
Cloud Pub/Sub
Cloud Firestore
Firebase (Realtime Database, Storage, Analytics, Auth)
Cloud Logging—forward log entries to a Pub/Sub topic by creating a sink. You can then trigger the function.
So Cloud SQL is the only resource that is not supported.
---
Question: You are a GCP architect working for a major retail customer. Many of your applications use Cloud Spanner as the backend DB. However Cloud Spanner does not automatically adjust the size of the instance when the workload changes. You are tasked with designing the solution for this problem. What would be the best solution?
1. Use a Cloud Scheduler to monitor the metrics of the Cloud Spanner instances. Use the same scheduler to adjust the instance size accordingly.
2. Use Cloud Monitor to monitor the metrics of the various Cloud Spanner instances. Send email to the operations team when threshold exceeds to let them handle the sizing accordingly.
3. Using Cloud Function query the Cloud Monitoring metrics of the Cloud Spanner instances. Use this Cloud Function to send request to Cloud Spanner to scale up or down.
4. Use Cloud Run to query the Cloud Monitoring metrics of the Cloud Spanner instances. Use this Cloud Run to send request to Cloud Spanner to scale up or down.
Ans Option 4: Using Cloud Function query the Cloud Monitoring metrics of the Cloud Spanner instances. Use this Cloud Function to send request to Cloud Spanner to scale up or down. is correct and little bit better compared to other options. An architecture note on the Google Architecture Center explains this architecture https://cloud.google.com/architecture/autoscaling-cloud-spanner
Option 1: Use a Cloud Scheduler to monitor the metrics of the Cloud Spanner instances. Use the same scheduler to adjust the instance size accordingly. is not correct. 
Option 2: Use Cloud Monitor to monitor the metrics of the various Cloud Spanner instances. Send email to the operations team when threshold exceeds to let them handle the sizing accordingly. is not correct as sending e-mails to the operations team is not efficient as this is manual.
Option 4: Use Cloud Run to query the Cloud Monitoring metrics of the Cloud Spanner instances. Use this Cloud Run to send request to Cloud Spanner to scale up or down. is not correct because in this architecture, Cloud Run has to continuously run all the time. In case of Cloud Functions, it can run on a predetermined interval to check the metrics and act accordingly. 
---
Question: You would like to create Cloud Function which reads the file contents as soon as it gets uploaded in the Cloud Storage. You would like to start the process only after the file gets completely uploaded becasue some files could be big. Which Cloud Storage trigger you should use to start the process?
1. google.storage.object.finalize
2. google.storage.object.complete
3. google.storage.object.upload
4. google.storage.object.finalized
Ans Option 1: google.storage.object.finalize is the correct option. This event is sent when a new object is created. 
There are only 4 valid events for the Cloud Storage. 
google.storage.object.finalize (default)
google.storage.object.delete - This event is sent when an object is permanently deleted
google.storage.object.archive - This event is sent when a live version of an object is archived or deleted.
google.storage.object.metadataUpdate - This event is sent when the metadata of an existing object changes.
All other options are invalid.
---
Question: You are using Cloud Storage to store employees identification documents. You would like to create a Cloud Function based on the event that the document gets deleted or updated for some reason. The versioning on the bucket is not enabled. Which Cloud Storage trigger you should use to start the process?
1. google.storage.object.finalize
2. google.storage.object.delete
3. google.storage.object.archive
4. google.storage.object.metadataUpdate
Ans Option 2: google.storage.object.delete is the correct option. This event is sent when an object is permanently deleted. 
There are only 4 valid events for the Cloud Storage. 
google.storage.object.finalize (default)
google.storage.object.delete - This event is sent when an object is permanently deleted. However this depends on the versioning setting for the bucket.
Depending on the object versioning setting for a bucket this means:
For versioning buckets, this is only sent when a version is permanently deleted (but not when an object is archived).
For non-versioning buckets, this is sent when an object is deleted or overwritten.
Option 3 google.storage.object.archive is not correct- This event is sent when a live version of an object is archived or deleted. This event is only sent for versioning buckets.
Option 4 google.storage.object.metadataUpdate is not correct - This event is sent when the metadata of an existing object changes. This event is sent when the metadata of an existing object changes.
---
Question: You are using Cloud Storage to store employees identification documents. You would like to create a Cloud Function based on the event that the live version of the document gets archived or deleted for some reason. The versioning on the bucket is enabled. Which Cloud Storage trigger you should use to start the process?
1. google.storage.object.finalize
2. google.storage.object.delete
3. google.storage.object.archive
4. google.storage.object.metadataUpdate
Ans Option 3: google.storage.object.archive is the correct option. This event is sent when an object is permanently deleted. 
There are only 4 valid events for the Cloud Storage. 
google.storage.object.finalize (default)
google.storage.object.delete - This event is sent when an object is permanently deleted. However this depends on the versioning setting for the bucket.
Depending on the object versioning setting for a bucket this means:
For versioning buckets, this is only sent when a version is permanently deleted (but not when an object is archived).
For non-versioning buckets, this is sent when an object is deleted or overwritten.
Option 3 google.storage.object.archive is not correct- This event is sent when a live version of an object is archived or deleted. This event is only sent for versioning buckets.
Option 4 google.storage.object.metadataUpdate is not correct - This event is sent when the metadata of an existing object changes. This event is sent when the metadata of an existing object changes.
----
---
Question:Compute-1->. You are running 100s of Linux VM machines in production. You need to manage access to the users to these VM machines. Which one of the below is NOT an correct option to manage access to the VM's?
1. OS Login
2. Managing SSH keys in metadata
3. Temporarily grant a user access to an instance
4. Managing SSH keys in Persistent Disks

Ans 4. Managing SSH keys in Persistent Disks is not one of the recommended options. Google provides multiple ways to manage user access to Linux machines.
Option 1: OS Login is the recommended option from Google. From the documentation "In most scenarios, we recommend using OS Login. The OS Login feature lets you use Compute Engine IAM roles to manage SSH access to Linux instances. You can add an extra layer of security by setting up OS Login with two-factor authentication, and manage access at the organization level by setting up organization policies.". More details can be found here. https://cloud.google.com/compute/docs/instances/access-overview
Option 2: Managing SSH keys in metadata is also a correct option to manage access. However this is not a recommended one compared to OS Login as this involves manually managing SSH keys. 
Option 3: Temporarily grant a user access to an instance is also an option to grant access to users. To grant a role to a member on a resource, use the resource's add-iam-policy-binding subcommand with the --member and --role flags.
gcloud compute resource-type add-iam-policy-binding resource-name \
    --member='member' \
    --role='role'
resource-type here could be disks, images, instances, instance-templates, regionDisks, sole-tenancy node-groups, sole-tenancy node-templates, snapshots. member is someone to whom you want to grant access and role is the role you want to assign to the identity.
---
Question:Compute-1a->You are running 100s of Linux VM machines in production. You need to manage access to the users to these VM machines. Which one of the below is the recommended option to manage access to the VM's?
1. OS Login
2. Managing SSH keys in metadata
3. Temporarily grant a user access to an instance
4. Managing SSH keys in Persistent Disks

Google provides multiple ways to manage user access to Linux machines.
Option 1: OS Login is the recommended option from Google. From the documentation "In most scenarios, we recommend using OS Login. The OS Login feature lets you use Compute Engine IAM roles to manage SSH access to Linux instances. You can add an extra layer of security by setting up OS Login with two-factor authentication, and manage access at the organization level by setting up organization policies.". More details can be found here. https://cloud.google.com/compute/docs/instances/access-overview
Option 2: Managing SSH keys in metadata is also a correct option to manage access. However this is not a recommended one compared to OS Login as this involves manually managing SSH keys. 
Option 3: Temporarily grant a user access to an instance is also an option to grant access to users. To grant a role to a member on a resource, use the resource's add-iam-policy-binding subcommand with the --member and --role flags.
gcloud compute resource-type add-iam-policy-binding resource-name \
    --member='member' \
    --role='role'
resource-type here could be disks, images, instances, instance-templates, regionDisks, sole-tenancy node-groups, sole-tenancy node-templates, snapshots. member is someone to whom you want to grant access and role is the role you want to assign to the identity.
Ans 4. Managing SSH keys in Persistent Disks is not one of the recommended options.
---
Question:Compute-2-> You are running multiple Linux VM's on production in a project named Production. You have built a custom app which connect to all VM's using SSH and execute a specific command which gathers specific information about the VM's. When new VM's added to the project that VM's also should be included. The custom app will be running on one of VM's in the same network as other VM's. What is the Google recommended way of doing this?
1. Create a service account. Provide the role roles/compute.osAdminLogin to the Service Account on the project level (production project). For the VM, where the custom app is running provide the scope cloud-platform scope. Also assign the Service Account to this VM. This should enable the custom app to connect to the other VM's in the project
2. Create a service account. Provide the role roles/compute.osOwnerLogin to the Service Account on the project level (production project). For the VM, where the custom app is running provide the scope cloud-platform scope. Also assign the Service Account to this VM. This should enable the custom app to connect to the other VM's in the project
3. Create a service account. Provide the role roles/compute.osAdminLogin to the Service Account on the project level (production project). Assign the Service Account to this VM. This should enable the custom app to connect to the other VM's in the project
4. Create a service account. Provide the role Owner to the Service Account on the project level (production project). Also assign the Service Account to this VM. This should enable the custom app to connect to the other VM's in the project

Option 1: Create a service account. Provide the role roles/compute.osAdminLogin to the Service Account on the project level (production project). For the VM, where the custom app is running provide the scope cloud-platform scope. Also assign the Service Account to this VM. This should enable the custom app to connect to the other VM's in the project is the correct answer. 
The recommended way is to create a Service Account and assign the role OS Login. This way the app's running on the VM can connect to the VM's through SSH. More details are here. https://cloud.google.com/compute/docs/tutorials/service-account-ssh
Option 2  Create a service account. Provide the role roles/compute.osOwnerLogin to the Service Account on the project level (production project). For the VM, where the custom app is running provide the scope cloud-platform scope. Also assign the Service Account to this VM. This should enable the custom app to connect to the other VM's in the project is incorrect because there is no role called roles/compute.osOwnerLogin. 
Option 3 Create a service account. Provide the role roles/compute.osAdminLogin to the Service Account on the project level (production project). Assign the Service Account to this VM. This should enable the custom app to connect to the other VM's in the project is incorrect because there is no scope is given which is required for the Service Account to execute API requests on this instance
Option 4 Create a service account. Provide the role Owner to the Service Account on the project level (production project). Also assign the Service Account to this VM. This should enable the custom app to connect to the other VM's in the project is not correct because assigning Owner role is not a Google recommended practice.
---
Question:Compute-2a-> You are running multiple Linux VM's on production in a project named Production. You have built a custom app which connect to all VM's using SSH and execute a specific command which gathers specific information about the VM's. When new VM's added to the project that VM's also should be included. The custom app will be running on one of VM's in the same network as other VM's. What is the Google recommended way of doing this?
1. Create a service account. Provide the role roles/compute.osAdminLogin to the Service Account on the project level (production project). For the VM, where the custom app is running provide the scope cloud-platform scope. Also assign the Service Account to this VM. This should enable the custom app to connect to the other VM's in the project
2. Create a service account. Provide the role roles/compute.osOwnerLogin to the Service Account on the project level (production project). For the VM, where the custom app is running provide the scope cloud-platform scope. Also assign the Service Account to this VM. This should enable the custom app to connect to the other VM's in the project
3. Create a service account. Provide the role roles/compute.osLogin to the Service Account on the project level (production project). For the VM, where the custom app is running provide the scope cloud-platform scope. Also assign the Service Account to this VM. This should enable the custom app to connect to the other VM's in the project
4. Create a service account. Provide the role Owner to the Service Account on the project level (production project). Also assign the Service Account to this VM. This should enable the custom app to connect to the other VM's in the project

Option 3: Create a service account. Provide the role roles/compute.osLogin to the Service Account on the project level (production project). For the VM, where the custom app is running provide the scope cloud-platform scope. Also assign the Service Account to this VM. This should enable the custom app to connect to the other VM's in the project is the correct answer. 
The recommended way is to create a Service Account and assign the role OS Login. This way the app's running on the VM can connect to the VM's through SSH. More details are here. https://cloud.google.com/compute/docs/tutorials/service-account-ssh
Option 1: Create a service account. Provide the role roles/compute.osAdminLogin to the Service Account on the project level (production project). For the VM, where the custom app is running provide the scope cloud-platform scope. Also assign the Service Account to this VM. This should enable the custom app to connect to the other VM's in the project is not correct answer though it will do the job but you don't necessarily have to provide osAdminLogin role unless you want admin privilages to those VM's.
Option 2  Create a service account. Provide the role roles/compute.osOwnerLogin to the Service Account on the project level (production project). For the VM, where the custom app is running provide the scope cloud-platform scope. Also assign the Service Account to this VM. This should enable the custom app to connect to the other VM's in the project is incorrect because there is no role called roles/compute.osOwnerLogin. 
Option 4 Create a service account. Provide the role Owner to the Service Account on the project level (production project). Also assign the Service Account to this VM. This should enable the custom app to connect to the other VM's in the project is not correct because assigning Owner role is not a Google recommended practice.
---
Question:Compute-3-> You would like to setup OS Login to a VM as that is the recommended way of allowing the users to connect to a VM. Which of the below commands is the correct command to enable this?
1. gcloud compute project-info add-metadata --metadata enable-oslogin=TRUE
2. gcloud compute instances add-metadata VM_NAME --metadata enable-oslogin=TRUE
3. gcloud compute instances add-metadata VM_NAME --metadataflag enable-oslogin=TRUE
4. gcloud compute instances add-metadata VM_NAME --enable-oslogin=TRUE

Option 2: gcloud compute instances add-metadata VM_NAME --metadata enable-oslogin=TRUE is correct. This command enables the os-login on the VM.
Option 1: gcloud compute project-info add-metadata --metadata enable-oslogin=TRUE is incorrect because it does this at project level. The question is how to enable this at the VM level.
Option 3: gcloud compute instances add-metadata VM_NAME --metadataflag enable-oslogin=TRUE is not correct because there is no flag called --metadataflag
Option 4: gcloud compute instances add-metadata VM_NAME --enable-oslogin=TRUE is incorrect because there is no flag called --enable-oslogin

For more information https://cloud.google.com/compute/docs/oslogin/set-up-oslogin
---
Question:Compute-3a-> You would like to setup OS Login to all the VMs in a project as that is the recommended way of allowing the users to connect to a VMs. Which of the below commands is the correct command to enable this?
1. gcloud compute project-info add-metadata --metadata enable-oslogin=TRUE
2. gcloud compute instances add-metadata VM_NAME --metadata enable-oslogin=TRUE
3. gcloud compute project-info add-metadata --metadataflag enable-oslogin=TRUE
4. gcloud compute instances add-metadata ALL_VM --metadata enable-oslogin=TRUE

Option 1: gcloud compute project-info add-metadata --metadata enable-oslogin=TRUE is correct and it does this at project level. 
Option 2: gcloud compute instances add-metadata VM_NAME --metadata enable-oslogin=TRUE is not correct. This command enables the os-login on the VM. The question is how to enable this at the VM level.
Option 3: gcloud compute project-info add-metadata --metadataflag enable-oslogin=TRUE is not correct because there is no flag called --metadataflag
Option 4: gcloud compute instances add-metadata ALL_VM --metadata enable-oslogin=TRUE  is incorrect because there is no way to mention all the VM's in the project by using the term ALL_VM.

For more information https://cloud.google.com/compute/docs/oslogin/set-up-oslogin
---
---
Question: Your company stores lot of information in the cloud storage buckets. This information is frequently accessed by the users (more than once a month) from across multiple geographies. Which storage class is best suited to address this requirement?
1. Standard - Regional
2. Standard - Multi-Regional
3. Nearline
4. Coldline

Ans: Standard - Multi-Regional is the correct answer as this is accessable from across multiple geographies.
Option 1 Standard - Regional is not correct as Regional storage keeps the data in a single region and users from other regions may experience latency issues.
Option 3 Nearline is not correct as this is used for infrequently accessed data. In the above scenario it is accessed more than once a month. 
Option 4 Coldline is not correct as this is used for infrequently accessed data.
---
Question: Your company stores lot of information in the cloud storage buckets. This information is in-frequently accessed by the users (once a month or less) from across multiple geographies. Which storage class is best suited to address this requirement?
1. Standard - Regional
2. Standard - Multi-Regional
3. Nearline - Regional
4. Nearline - Multi-Regional

Ans: 
Option 1 Standard - Multi-Regional is the not correct answer though this is accessable from across multiple geographies, it is accessed infrequently.
Option 1 Standard - Regional is not correct as Regional storage keeps the data in a single region and also this data is not hot data
Option 3 Nearline - Regional is not correct though this is used for infrequently accessed data, multi regional is better suited in this scenario. 
Option 4 Nearline - Multi-Regional is correct as this is used for infrequently accessed data. 
---