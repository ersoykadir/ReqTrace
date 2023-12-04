1 Functional Requirements
1.1 User Requirements
1.1.1 User Registration
1.1.1.1 User Account Creation: Users shall be able to create an account on the system. Users are, by default, assigned the "victim" role.
1.1.1.2 Registration Confirmation and Login: After successful registration, users shall receive a notification confirming the approval of their registration, indicating that the registration process is successful. Users will be automatically redirected to the login page after registration.
1.1.1.3 Convenient Sign-In: At the login page, users have the option to save their login information for a convenient sign-in process in subsequent visits, eliminating the need to re-enter their credentials.
1.1.1.4 Role Request and Emergent Functionalities: Upon logging in, users are initially assigned the "victim" role. After login, users can request new roles, each with its own verification methods. When a user's request for a new role is approved, they will gain access to emergent functionalities associated with that role. These emergent functionalities will include changes to the navbar and page view, with related buttons and options specific to the approved role.
1.1.1.5 Emergent Roles After a user's request for a new role is approved, the system shall dynamically adjust the navigation bar (navbar) and page view to reflect the functionalities and options related to the approved role. This shall include displaying role-specific buttons and options that are relevant to the newly assigned role.
1.1.2 User Roles
1.1.2.1 Victim
1.1.2.1.1 Any user should be able to assume the role of a victim after providing the necessary information to the system.
1.1.2.1.2 Victims shall be able to report their current situation and needs.
1.1.2.1.3 Victims shall be able to view assistence locations on a map and as a list. (Help centers, soup kitchens etc.)
1.1.2.1.4 Victims shall be able to filter the assistence locations by type and distance.
1.1.2.1.5 Victims shall be able to view available resources on a map and as a list.
1.1.2.1.6 Victims shall be able to filter resources by name, category and distance.
1.1.2.1.7 Victim shall be notified when a relevant assistence location is nearby.
1.1.2.1.8 Victim shall be able to get directions to nearby assistence locations.
1.1.2.2 Responder
1.1.2.2.1 Any user wishing to become a responder must upload a valid identification document as a necessity for their role transition in the system.
1.1.2.2.2 Responders shall be able to create a resource for objects or services they can offer.
1.1.2.2.3 Responders shall be able to set the following information regarding a resource: location, quantity, type, category
1.1.2.2.4 All users shall be able to view the resources a responder has added in the responder's profile.
1.1.2.2.5 Responders shall be able to accept or decline task assignments from coordinators.
1.1.2.2.6 Responders shall be able to comment on their actions using the sections on the windows provided for their actions.
1.1.2.2.7 Responders shall be able to update the status of their tasks as: to do, in progress, completed.
1.1.2.2.8 Responders shall be able to view all information provided by facilitators.
1.1.2.2.9 Responders shall be able to see their current and previous tasks.
1.1.2.2.10 Responders shall be able to view all actions in a task assigned to them as a list and on a map.
1.1.2.2.11 Responders shall be able to mark actions as completed.
1.1.2.3 Facilitator
1.1.2.3.1 Responders and victims shall be able to apply for a facilitator role through an additional verification process.
1.1.2.3.2 Facilitators shall be able to create requests.
1.1.2.3.3 Facilitators shall be able to create resources.
1.1.2.3.4 Facilitators shall be able to view requests on a map and as a list.
1.1.2.1.5 Facilitators shall be able to filter requests by name, category and distance.
1.1.2.3.6 Facilitators shall be able to group requests made by victims into a larger request.
1.1.2.3.7 Facilitators shall be able to update the status of requests as: to do, in progress, completed
1.1.2.3.8 Facilitator shall be able to provide feedback on any ongoing actions sent by the coordinators.
1.1.2.3.9 Facilitators shall be able to verify action requests from responders.
1.1.2.3.10 Facilitators shall be able to share and update information they provide.
1.1.2.4 Coordinator
1.1.2.4.1 Coordinators must be assigned by administrators.
1.1.2.4.2 Coordinators shall be able to suspend non-coordinator or non-administrator users.
1.1.2.4.3 Coordinators shall be able to create tasks consisting of a list of actions.
1.1.2.4.3 Coordinators shall be able to specify details for actions, including name, type of action, location, recommended path from the previous action, and a comment in the form of free-form text.
1.1.2.4.4 Coordinators shall be able to assign tasks to responders.
1.1.2.4.5 Coordinators shall be able to remove assignees from tasks.
1.1.2.4.6 Coordinators shall be able to view resources, requests and tasks as a list and on a map.
1.1.2.4.7 Coordinators shall be able to filter resources, requests and tasks by whichever subset of name, category, amount, distance, urgency and status is applicable.
1.1.2.4.8 Coordinators shall receive notifications for new responders signing up.
1.1.2.4.9 Coordinators shall be able to view all user profiles, actions, and information provided by facilitators.
1.1.2.4.10 Coordinators shall be able to view, delete or reply to the requests.
1.1.2.4.11 Coordinators shall be able to share and update information they provide.
1.1.2.4.12 Coordinators shall be able to delete or update information shared by facilitators.
1.1.2.4.13 Coordinators shall be able to view, delete or reply to reported problems.
1.1.2.4.14 Coordinators shall be able to send messages to admins.
1.1.2.5 Administrator
1.1.2.5.1 Administrators shall be able to assign and unassign coordinator and facilitator roles to designated users.
1.1.2.5.2 Administrators shall be able to revoke user roles in cases of abuse or misuse.
1.1.2.5.4 Administrators shall be able to provide technical assistance to coordinators.
1.1.2.5.5 Administrators shall be able to manually verify documents when needed.
1.1.2.5.7 Adminstrator role is granted by project owners.
1.1.2.5.8 Administrators shall be able to send notifications to other administrators.
1.1.2.5.9 Administrators shall have access to live system statistics.
1.1.3 Location Services
1.1.4 Information Filtering
1.1.5 Disaster Reporting
1.2 System Requirements
1.2.1 Multi-hazard support
1.2.1.1 The system shall provide multi-hazard support. The system shall support various types of disasters and emergencies, including natural disasters (e.g. earthquakes, floods, hurricanes), man-made disasters (e.g. explosions, fires, terrorist attacks), and public health emergencies (e.g. pandemics, epidemics). The system must be flexible enough to accommodate different needs and response strategies based on the disaster type.
1.2.2 Multilingual Support
1.2.2.1 The platform must support multiple languages to cater to a diverse user base.
1.2.3 Resource Management
1.2.3.1 Digital Resources
1.2.3.1.2 Resources must be digitized and quantified in the system.
1.2.3.2 Categorization of resources
1.2.3.2.1 To facilitate distribution, sent resources should be categorized in detail, including the contents of each box, quantity, shoe/clothing size, etc.
1.2.3.3 Semantic relations between resources
1.2.3.3.1 Resources should have semantic relationships for efficient categorization.
1.2.3.4 Dynamic needs
1.2.3.4.1 The platform should be flexible enough to adapt to the changing needs of disaster areas, depending on the location and stage of the disaster. This includes different needs in urban and rural areas, as well as different needs for surviving the disaster and educational needs.
1.2.4 Actions
1.2.4.1 Creating new actions
1.2.4.1.1 The system shall allow authorized users to create new actions in response to disaster events.
1.2.4.1.2 The system shall allow authorized users to provide action details such as the action type, the target group, and the due date.
1.2.4.1.3 The system shall ensure that all required fields are filled in before an action can be created.
1.2.4.1.4 The system shall provide a feature to categorize the actions based on different types of actions such as transportation, supply delivery, medical aid, etc.
1.2.4.2 Task Assignment:
1.2.4.2.1 The system shall allow authorized users to assign specific tasks to other users.
1.2.4.2.2 The system shall allow authorized users to set deadlines for task completion.
1.2.4.3 Prioritization
1.2.4.3.1 The system shall provide a feature to prioritize actions based on their urgency and impact on the affected population.
1.2.4.4 Linking Actions to Events
1.2.4.4.1 The system shall allow authorized users to link the action to the corresponding event.
1.2.4.4.2 The system shall notify users who have expressed interest in the event.
1.2.4.5 Actions Filtering
1.2.4.5.1 The system shall allow users to filter actions based on various criteria, such as action type, location, and target audience.
1.2.4.6 Tracking action progress
1.2.4.6.1 The system shall allow authorized users to track the progress of each action and its associated tasks.
1.2.4.6.2 The system shall notify users when tasks are overdue or completed.
1.2.4.6.3 The system shall allow authorized users to update the status of each action and its associated tasks.
1.2.5 Reporting
1.2.5.1 The system shall generate a live report on outstanding requests, showing the deficit in materiel by location.
1.2.5.2 The system shall generate a live report on the overall progress of the disaster response efforts, including completed and pending actions, as well as their impact on the affected population.
1.2.7 Map-based operations
1.2.7.1 The platform shall have a map interface that displays the appropriate subset of resources, requests, and tasks, along with warnings related to the current situation.
1.2.7.2 The map shall be capable of filtering items by the applciable subset of name, category, amount, distance, urgency and status.
2 Non Functional Requirements
2.1 Security and Privacy
2.1.1 Data protection regulations
2.1.1.1 Data Protection Compliance: The platform shall fully comply with relevant data protection regulations, such as GDPR in Europe and KVKK in Turkey, to ensure lawful and ethical handling of user data.
2.1.2 Personal information protection and confidentiality
2.1.2.1 The platform shall implement robust security measures to protect the personal information and contact details of individuals affected by disasters, ensuring privacy and confidentiality at all times. This includes encryption, access controls, and secure data storage practices.
