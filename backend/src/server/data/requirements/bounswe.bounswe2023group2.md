1 Functional Requirements
1.1 User Requirements
1.1.1 Account Features
1.1.1.1 Registration
1.1.1.1.1 Users shall be able to create an account using a valid and unique email address or phone number, a unique username, their name, their surname and a password.
1.1.1.2 Log In
1.1.1.2.1 Users shall be able to log into their account using their email, username or phone number; and password combination.
1.1.1.2.2 Users shall be able to reset their password via email verification or sms verification.
1.1.1.3 Log Out
1.1.1.3.1 Users shall be able to log out of their accounts.
1.1.2 User Actions
1.1.2.1 Guest User Actions:
1.1.2.1.1 Guest users shall be able to create only one emergency.
1.1.2.1.2 Guest users shall be able to view emergencies and activities about disasters, including event types, resources available, and actions taken.
1.1.2.1.3 Guest users shall be able to filter and sort activities about emergencies, events, resources, actions, and needs based on location, date, type etc.
1.1.2.2 Authenticated User Actions:
1.1.2.2.1 Authenticated users shall have all functionalities that guest users have.
1.1.2.2.2 Authenticated users shall create activities.
1.1.2.2.3 Authenticated users shall be able to update and delete their current active activities.
1.1.2.2.4 Authenticated users shall verify their accounts by verifying their phone numbers or emails unless already verified by system admins.
1.1.2.2.5 Authenticated users shall be able to delete their accounts.
1.1.2.2.6 Authenticated users shall be able to edit their profiles.
1.1.2.2.7 Authenticated users shall be able to confirm or reject other users' activities.
1.1.2.2.8 Authenticated users shall be able to report malicious users or activities to the admins.
1.1.2.2.9 Authenticated users should be able to receive notifications about certain topics based on location, date, type etc.
1.1.2.2.10 Authenticated users shall be able to search activities and emergencies.
1.1.2.2.11 Authenticated users shall be able to search profiles.
1.1.2.2.12 Users should be able to subscribe to topics using filter and search on topics.
1.1.2.2.13 Authenticated users should be able to add and delete topics for notifications.
1.1.2.2.14 Authenticated users should be able to view details or dismiss when they receive a notification
1.1.2.2.15 Authenticated users shall be able to edit their profile info.
1.1.2.2.16 If users have not added their phone number or email address to their profile, they shall be able to do so.
1.1.2.2.17 Authenticated users shall be able to choose a role after adding a valid phone number.
1.1.2.2.18 Authenticated users shall be able to select who can see their contact information.
1.1.2.2.19 Authenticated users shall be able to upvote an action or event to upgrade its reliability scale.
1.1.2.3 Role-Based User Actions:
1.1.2.3.1 Role-Based users shall have all functionalities that authenticated users have.
1.1.2.3.2 Role-Based users shall be able to search for activities that are related to their proficiency.
1.1.2.3.3 Role-Based users shall be able to contact people who state their needs are related to Role-Based user proficiency.
1.1.2.3.4 Role-Based Users shall be able to add information about their proficiency and how they can help.
1.1.2.4 Credible User Actions:
1.1.2.4.1 Credible users shall have all functionalities that role-based users have.
1.1.2.4.2 Credible user shall be able to create a special activity which is prioritized on lists and maps.
1.1.3 Admin
1.1.3.1 Admin users shall be able to create actions, such as relieving needs, sending rescue teams, etc...
1.1.3.2 Admin users shall be able to search users and see the contact information of other users.
1.1.3.3 Admin users shall be able to view the misinformation reports.
1.1.3.4 Admin users shall be able to accept or reject a misinformation report. When the misinformation report is accepted, the event will be removed.
1.1.3.5 Admin users shall be able to remove activities from the platform.
1.1.3.6 Admin users shall be able to see authenticated and verified users' activities.
1.1.3.7 Admin users shall be able to cancel verified users' verification or authenticated user's authentication. Once admin users cancel verification/authentication, they shall not be able to be verified or authenticated again.
1.1.3.8 Admin users shall be able to see and recover cancelled verification or authentication.
1.1.3.9 Admin users shall be able to select or approve users as credible users.
1.1.3.10 Admin users shall be able to cancel credible users' credibility.
1.1.3.11 Admin users shall be able to pin some activities at the top to increase their visibility.
1.2 System Requirements
1.2.1 Profile Page
1.2.1.1 A user profile shall have these attributes:
1.2.1.2 The system should show related actions, needs, resources and events to the authenticated user that has related proficiency. (i.e A doctor should see the event that medications arrive in the area.)
1.2.2 Feedback System
1.2.2.1 The system shall allow users to report malicious users and activities.
1.2.2.2 The system shall allow users to check for a number of other users' confirmations or rejections about users, activities.
1.2.2.3 The system shall carry on reports to the administration system.
1.2.2.4 The system shall not accept the restricted accounts to register again.
1.2.3 Activities
1.2.3.1 Resources
1.2.3.1.1 Resource Entry
1.2.3.1.1.1 A resource shall have these attributes:
1.2.3.1.1.2 A resource should have attributes:
1.2.3.1.2 Resource Structure
1.2.3.1.2.1 Resources should be organized in a structured manner to allow for easy access and management.
1.2.3.1.2.2 The following predefined resources shall be included: food, clothing, accommodation, and human resources.
1.2.3.1.2.1 Subtypes of food shall include:
1.2.3.1.2.2 Subtypes of human resources shall include:
1.2.3.1.2.3 Subtypes of clothes shall include:
1.2.3.1.3 An activity sorting metric which measures how many times the resource has been viewed/shared/reacted to by other users (_interaction rate_) shall be calculated.
1.2.3.2 Events
1.2.3.2.1 Events shall have these attributes:
1.2.3.2.1.1 Type (it can be predefined or other typed)
1.2.3.2.1.2 Creation time
1.2.3.2.1.3 Creator username
1.2.3.2.1.4 Location
1.2.3.2.1.5 Interaction rate
1.2.3.2.1.6 Related needs (Ex. enkaz altinda canli var, related needs: vinc, kurtarma ekibi vs)
1.2.3.2.1.7 Confirmer username
1.2.3.2.1.8 Last confirmation time
1.2.3.2.1.9 Approval and Rejection number
1.2.3.2.1.10 Reliability scale
1.2.3.2.2 The following predefined event types shall be included:
1.2.3.2.3 An activity sorting metric which measures how many times the event has been viewed/shared/reacted to by other users (_interaction rate_) shall be calculated.
1.2.3.3 Actions
1.2.3.3.1 Actions shall have these attributes:
1.2.3.3.1.1 Type (it can be predefined or other typed)
1.2.3.3.1.2 Creation time
1.2.3.3.1.3 Creator username
1.2.3.3.1.4 Interaction rate
1.2.3.3.1.5 Related resources, needs and events (Using these resources, handling these needs, related to these events etc)
1.2.3.3.1.6 Confirmer username
1.2.3.3.1.7 Last confirmation time
1.2.3.3.1.8 Approval and Rejection number
1.2.3.3.1.9 Reliability scale
1.2.3.3.1.10 Current status
1.2.3.3.2 Actions should be created with the following attributes:
1.2.3.3.2.1 Start location
1.2.3.3.2.2 End location
1.2.3.3.3 An activity sorting metric which measures how many times the action has been viewed/shared/reacted to by other users (_interaction rate_) shall be calculated.
1.2.3.4 Needs
1.2.3.4.1 Needs shall have these attributes:
1.2.3.4.1.1 Type: can be food, clothes, shelter, medical assistance, heat; should be flexible
1.2.3.4.1.2 Subtype according to type
1.2.3.4.1.3 Creation time
1.2.3.4.1.4 Creator/Demander username
1.2.3.4.1.5 Location
1.2.3.4.1.6 Quantity
1.2.3.4.1.7 Urgency
1.2.3.4.1.8 Approval and Rejection number
1.2.3.4.1.9 Reliability scale
1.2.3.4.1.10 Current status
1.2.3.4.2 Needs should be flexible enough to accommodate changing needs and priorities over time, as the disaster situation evolves.
1.2.3.4.3 Needs should allow users to assign themselves for providing the resource of it.(?)
1.2.3.4.4 Status of needs should be in a timely update and demanders shall receive status notifications for each update.
1.2.3.4.5 An activity sorting metric which measures how many times the need has been viewed/shared/reacted to by other users (_interaction rate_) shall be calculated.
1.2.3.5 Locations which were previously added should be able to be selected when creating an activity.
1.2.4 Filter, sort
1.2.4.1 The system shall sort activities based on location, reliability scale, date, emergency level etc.
1.2.4.2 The system shall sort emergencies based on location, reliability scale, date, emergency level etc.
1.2.4.3 The system shall sort users based on their roles and locations.
1.2.5 Map visualization
1.2.5.1 Maps shall contain some annotation on them. Annotations shall have different colours based on the emergency level.
1.2.5.2 The map shall be zoomed in and out and interactable. The annotations in the map should scale up and down accordingly.
1.2.5.3 The user’s location shall appear on the map so that users are able to understand what’s happening around them
1.2.5.4 The map shall show the locations that are filtered.
1.2.6 Annotation
1.2.6.1 The system shall use the W3C Geolocation API standard for implementing location-related information.
1.2.6.2 The system shall provide all kinds of search functionality (e.g., search with filters, sort by date) for models.
1.2.6.3 Users should retrieve results that are semantically similar to their queries.
1.2.6.4 Users should be able to annotate different models, and annotations should comply with W3C Web Annotation Data Model.
1.2.7 Notifications
1.2.7.1 The system shall create in-app and push notifications.
1.2.7.2 The system should create notifications, if users click the “want to be notified” button on the activity.
1.2.7.3 The system should create notifications if users' profession might be implying that they can be a resource to a certain need.
1.2.7.3.1 The system should be able to add (resource | translator | any topic) to notification settings as default when the user has a role.
1.2.7.4 The system should create notifications if an event takes place near users' addresses when they provide their addresses.
1.2.7.4.1 The system should be able to add event | any | (user's city) topic to notification settings as default.
1.2.8 Administrations
1.2.8.1 The system shall collect users' reports about other users in the admin dashboard.
1.2.8.2 The system shall collect users' reports about activities and events in the admin dashboard.
1.2.8.3 The system shall sort the reports according to the number of reports.
1.2.8.4 The system shall hold a list of restricted users and their phone numbers.
1.2.8.5 The system shall track the restricted users by their phone number in order to prevent new signs up.
1.2.8.6 The system shall hold the admins' logs.
1.2.9 Account Features
1.2.9.1 The system shall support remember me feature.
1.2.9.2 The system shall support keep me logged in feature.
2 Non-Functional Requirements
2.1 Availability
2.1.1 The application shall be available as a native website via modern web browsers. (Chrome, Edge, Firefox, Opera, Safari)
2.1.2 The application shall be available as a native mobile application on Android platforms.
2.1.3 Language
2.1.3.1 The application shall support the English and Turkish characters.
2.1.3.2 The application should be available in multiple languages to ensure that it can be used by people from diverse linguistic backgrounds
2.1.4 The application should support [UTF-8](https://en.wikipedia.org/wiki/UTF-8) character encoding.
2.1.5 High availability
2.1.5.1 The application shall be available 7/24 to ensure that it can be accessed by emergency responders, government agencies, and affected communities at any time.
2.1.6 Scalability
2.1.6.1 The application shall be designed to handle a large volume of traffic and users during peak times, such as during a disaster.
2.1.7 The application shall be easy to use, with a simple and intuitive interface that does not require extensive training or technical knowledge.
2.2 Privacy
2.2.1 The system shall follow the regulations and guidelines defined by [GDPR](https://gdpr-info.eu/) and [KVKK](https://www.kvkk.gov.tr/).
2.2.2 Users shall read and accept the Privacy Policy and User Agreement based on GDPR and KVKK before registration.
2.2.3 Users shall be notified if any change happens in the policy.
2.3 Security
2.3.1 Passwords should be at least 8 characters long and contain at least one uppercase letter, one lowercase letter and one number.
2.3.2 API endpoints should be protected by access tokens in order to prevent users to access permissions that are not in the scope of their roles.
2.3.3 Password should be encrypted with SHA-256 algorithms for account security.
2.3.4 The system shall use HTTPS protocol to prevent network-related attacks.
2.3.5 The system shall use encryption to protect all sensitive information stored or transmitted over insecure channels.
2.4 Performance and Reliability
2.4.1 Response time: The system should respond to user requests within 5 seconds.
2.4.2 Throughput: The system should be able to handle a minimum of 10000 concurrent users.
2.4.3 User Accounts: The platform shall support at least 100000 user accounts.
2.4.4 Fault Tolerance: The system should be designed to recover quickly from any failure, and data should not be lost during failures.
2.4.5 Capacity: The system should be designed to handle a large volume of data and user requests without any slowdowns.
2.4.6 Data integrity: The system should ensure that all data stored is accurate, complete, and consistent.
2.5 Backup and Recovery (Consistency)
2.5.1 The system shall have a backup mechanism to ensure that all data is regularly backed up.
2.5.1.1 The backup process should be automatic and take place at regular intervals.
2.5.1.2 The system should maintain multiple copies of backups in different locations to ensure redundancy.
2.5.2 The system shall have a recovery mechanism to restore data in case of system failure or data corruption.
2.5.2.1 The recovery process should be automatic and take place as soon as possible after the detection of failure.
2.5.3 The system should ensure data consistency during backup and recovery processes to avoid data loss or corruption.
2.5.4 The system should allow the users to create needs, resources, actions, and events even when the app is not connected to the internet.
2.5.5 The system should integrate the local actions of users with the app's data once the user is able to connect to the internet.
