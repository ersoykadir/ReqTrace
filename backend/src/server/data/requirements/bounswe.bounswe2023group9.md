1 Functional Requirements
1.1 User Requirements
1.1.1 User Types
5 types of users: guests, contributors, reviewers, admins and basic users.
1.1.1.1 Guests
1.1.1.1.1 Guests shall be able to view the nodes and their references.
1.1.1.1.2 Guests shall be able to view the contributors and reviewers of the nodes.
1.1.1.1.3 Guests shall be able to view the questions, answers, semantic tags, and public annotations of each node.
1.1.1.1.4 Guests shall be able to sign-up.
1.1.1.2 Basic users
1.1.1.2.1 Basic users shall be able to ask questions about a node and have the option to choose whether their identity become public or anonymous when asking a question.
1.1.1.2.2 Basic users shall be able to create private annotations for a node.
1.1.1.2.3 Basic users shall be able to be notified via email when their questions are replied.
1.1.1.2.4 Basic users shall be able to perform the same actions as guests except sign-up.
1.1.1.3 Contributors
1.1.1.3.1 Contributors shall be able to create workspaces.
1.1.1.3.2 Contributors shall be able to reference their workspaces from existing nodes.
1.1.1.3.3 Contributors shall be able to be notified via email .
1.1.1.3.3.1 Contributors shall be able to be notified via email when a node which he/she contributed is referenced by another contributor.
1.1.1.3.3.2 Contributors shall be able to be notified via email when his/her contribution is reviewed.
1.1.1.3.3.3 Contributors shall be able to be notified via email when his/her objection is reviewed.
1.1.1.3.3.4 Contributors shall be able to be notified via email when another contributor sends a collaboration request.
1.1.1.3.3.5 Contributors shall be able to be notified via email when a user asks a question about his/her node.
1.1.1.3.4 Contributors shall be able to add annotations that will be public after creating a node from the workspace to the workspaces they create before the reviewing process.
1.1.1.3.5 Contributors shall be able to issue an objection against a node.
1.1.1.3.6 Contributors shall be able to link external scientific materials to support his/her claim/node.
1.1.1.3.7 Contributors shall be able to track the progress of their workspace and edit the entries.
1.1.1.3.8 Contributors shall be able to perform the same actions as basic users.
1.1.1.3.9 Contributors shall be able to send their workspaces to review which is further to be added to the graph as a node.
1.1.1.3.10 Contributors shall be able to add semantic tags to their workspaces.
1.1.1.4 Reviewers
1.1.1.4.1 Reviewers shall be able to accept or reject the workspaces which are submitted by contributors
1.1.1.4.2 Reviewers shall be able to accept or reject the objections issued by contributors.
1.1.1.4.3 Reviewers shall be able to add comments to entries regarding to the review process.
1.1.1.4.4 Reviewers shall be able to perform the same actions as contributors.
1.1.1.5 Admins
1.1.1.5.1 Admins shall be able to remove (hide) nodes.
1.1.1.5.2 Admins shall be able to ban user accounts.
1.1.1.5.3 Admins shall be able to remove (hide) questions.
1.1.1.5.4 Admins shall be able to remove (hide) answers.
1.1.1.5.5 Admins shall be able to choose which contributors can be reviewers.
1.1.1.5.6 Admins shall be able to  perform the same actions as basic users.
1.1.2 User Interactions
1.1.2.1 Contributors shall be able to send a collaboration request to another contributor.
1.1.2.2 Contributors shall be able to accept or reject a collaboration request.
1.1.2.3 Contributors shall be able to see and contribute to the workspaces they collaborate.
1.1.2.4 Contributors shall be able to reply asked questions about his/her nodes.
1.1.3 Sign up & Login
1.1.3.1 Users shall provide their real names, e-mail addresses, and passwords to sign up.
1.1.3.2 E-mail addresses shall be unique.
1.1.3.3 User passwords shall meet safety criteria
1.1.3.4 E-mail addresses shall be confirmed.
1.1.3.5 Basic users shall provide and confirm their ORCID-ID in order to be a contributor.
1.1.4 Profile Preferences
1.1.4.1 Basic users shall be able to change their passwords.
1.1.4.2 Basic users shall have profile pages.
1.1.4.3 Basic users shall be able to let their profile pages show their activity.
1.1.4.4 Guests shall be able to view other users' profile pages.
1.1.4.5 Basic users shall be able to edit their own profile information.
1.1.4.6 Basic users shall be able to turn on or off the email notifications.
1.2 System Requirements
1.2.1 Nodes
1.2.1.1 Nodes shall contain bits of knowledge that can represent a type of knowledge at any step in the scientific knowledge development process.
1.2.1.2 Nodes shall be referenceable/linkable to other nodes.
1.2.1.3 Nodes shall have semantic tags regarding to their subjects.
1.2.1.4 Nodes shall have a questions/answers section.
1.2.1.5 Nodes shall be objectable by contributors.
1.2.1.6 Nodes shall have public annotations.
1.2.1.7 Nodes shall be created and published upon approval of a workspace.
1.2.2 Reviews
1.2.2.1 The platform shall assign some number of randomly chosen related reviewers (according to semantic tags) for a node or objection.
1.2.2.2 The platfrom shall not allow contributors and reviewers to see each others' identities when a node or an objection is being reviewed.
1.2.2.3 The platform shall provide the contributors a report prepared by reviewers when a review process is rejected.
1.2.2.4 A reviewer cannot be assigned as a reviewer for his/her own workspace.
1.2.2.5 Workspaces' chosen first and final entries are sent to the reviewers to be reviewed.
1.2.3 Questions
1.2.3.1 Questions shall be sorted either by date or by popularity.
1.2.3.2 Questions shall be repliable by the contributors of the node.
1.2.4 Annotations
1.2.4.1 Public annotations should be visible to anyone.
1.2.4.2 Private annotations should be visible only to their creator.
1.2.5 Search
1.2.5.1 Searching
1.2.5.1.1 The platform shall allow users to search for users and nodes.
1.2.5.2 Filtering
1.2.5.2.1 Nodes shall be filtered by their semantic tags.
1.2.5.2.2 Nodes shall be filtered by their contributors.
1.2.5.2.2 Nodes shall be filtered by their reviewers.
1.2.5.3 Sorting
1.2.5.3.1 Nodes shall be sorted by their publish date.
1.2.5.3.2 Nodes shall be sorted by their popularity.
1.2.5.3.2.1 Nodes shall be sorted by their visits.
1.2.5.3.2.2 Nodes shall be sorted by their number of references.
1.2.7 Graph Visualization
1.2.7.1 The platform shall visualize the graph.
1.2.8 Email Notifications
1.2.8.1 Email notifications shall include a message which contains information about the cause or reason behind it.
1.2.8.2 Email notifications shall only be delivered to users who are directly concerned.
1.2.8.3 Email notifications shall be sent immediately after the event that triggers them occurs.
1.2.8.4 Email notifications should be sent only once.
1.2.9 Workspaces
1.2.9.1 Workspaces shall let contributors add editable entries.
1.2.9.2 Workspaces shall be collaborative via sending request to desired contributors.
1.2.9.3 Workspaces shall have first and final entries chosen by the contributors before they are submitted for the review.
1.2.9.4 Workspaces shall let referenced nodes to be cited in the current work.
1.2.9.5 Workspaces shall be visible to only the contributors of the workspace.
2 Non-functional Requirements
2.1 Availability
2.1.1 The system shall be available in the English language.
2.2 Standards
2.2.1 Annotations shall be compliant with W3C annotation standards
2.3 Privacy
2.3.1 The system shall comply with the rules defined by GDPR and KVKK.
2.4 Security
2.4.1 User passwords shall be stored as hashed in the database.
