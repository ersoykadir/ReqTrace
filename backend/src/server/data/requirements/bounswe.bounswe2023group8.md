1 Functional Requirements
1.1 User Requirements
1.1.1 Registration and Login
1.1.1.1 Guests shall be able to :
1.1.1.1.1 Register giving the following information; email, password, username, birthday.
1.1.1.2 Users shall be able to:
1.1.1.2.1 Login by giving the following information: email and password or username and password.
1.1.1.2.2 Logout.
1.1.1.2.3 Update their passwords.
1.1.1.2.4 Reset their passwords using 'Forgot Password?' option.
1.1.2 Account
1.1.2.1 Guests shall verify their account via email before they can be considered as users.
1.1.2.2 Users shall be able to delete their accounts.
1.1.2.3 Users shall be able to update some of the account information.
1.1.2.3.1 Users shall be able to change passwords and other account related settings.
1.1.2.3.2 Users shall not be able to change their username, email address and birthday.
1.1.2.5 Users shall have control over privacy settings of IAs. (e.g. public, private and personal).
1.1.3 User-to-User Interactions
1.1.3.1 View other users profiles' and see their publicly viewable data such as their public posts (posts they created in public IAs), names of their public and private IAs, followers, followings, and tags that they are interested in.
1.1.3.2 Follow other users on the platform.
1.1.3.3 Vote on other users based on their profile, behaviour and activity on the platform which will affect the target's reputation scores (See "1.2.3.2 Reputation system")
1.1.4 User-to-Platform Interactions
1.1.4.1 Posts: (See "1.2.1.1 Posts")
1.1.4.1.1 Creating a post in an IA by providing a title, a main link that this post refers to, a description, tags that the post relates to defined by [Wikidata](https://www.wikidata.org/), original source of the provided link, and optionally: publication date of the original source, geolocation of the subject in accordance with [W3C Recommendation standards](https://www.w3.org/TR/geolocation/), fact-checking status, and purpose of the post.
1.1.4.1.2 Editing fields of their own post.
1.1.4.1.3 Commenting on a post.
1.1.4.1.4 Down/Upvoting a post.
1.1.4.1.5 Reporting inappropriate posts to IA moderators. (See "1.1.4.2.7" for more info in Moderators)
1.1.4.1.6 Annotating any post in order to give more detailed information about certain parts of these posts (See "1.2.1.4 Annotations")
1.1.4.1.7 Suggesting additional tags to posts created by other users.
1.1.4.2 Interest Areas: (See "1.2.1.2 Interest Areas")
1.1.4.2.1 Creating an interest area by providing a title, tags defined by [Wikidata](https://www.wikidata.org/) to describe the focus of the IA, the IA's access levels (See item "1.2.1.2.5" about access levels), and the set of IAs that the new IA will consist of in case the new IA is a collection of other IAs.
1.1.4.2.2 Editing fields of interest areas which they have owner or moderation access level except. (See item "1.2.1.2.5" about access levels)
1.1.4.2.3 Following other IAs.
1.1.4.2.4 Joining private IAs. (See item "1.2.1.2.5" about access levels)
1.1.4.2.5 Creating posts in interest areas which they have an access level higher than viewer. (See item "1.2.1.2.5" about access levels)
1.1.4.2.6 Suggesting additional tags to IAs created by other users.
1.1.4.2.7 Reporting inappropriate IAs to System Administrators.
1.1.4.2.8 Managing roles of other users in their own interest areas. Every role in the role hierarchy below shall have the permissions of all the roles below itself:
1.1.4.1 and "1.1.4.2" except creating new posts.
1.2 System Requirements
1.2.1 Content
1.2.1.1 Post
1.2.1.1.1 Shall have an IA.
1.2.1.1.2 Shall have a title
1.2.1.1.3 Shall have a main body that consists of only a main non-empty link, that is the target of the post in question, and an optional text for the creator to comment on this target link or describe it.
1.2.1.1.4 Shall contain required relevant metadata:
1.2.3.1 Tags")
1.2.1.1.5 Shall contain optional relevant metadata:
3 Recommendation standards](https://www.w3.org/TR/geolocation/).
1.2.1.1.6 Shall have comments, upvotes, and downvotes.
1.2.1.1.7 Shall specify its purpose by labels. (e.g. documentation, learning, research, news, discussion, sharing).
1.2.1.2 Interest Areas (IA):
1.2.1.2.1 Shall consist of posts created by their users or posts created within their nested IAs.
1.2.1.2.2 Shall be able to consist of a collection of other IAs.(nested)
1.2.1.2.3 Shall obtain at least one semantic label(tag) during their creation. IA tags only show the topic scope of an IA and shall utilize the main tagging system on the platform, which uses [Wikidata](https://www.wikidata.org/) knowledge base (See "1.2.3.1 Tags")
1.2.1.2.4 Shall have a "Recommended IAs" section where it lists other IAs that might interest the user based on their tags.
1.2.1.2.5 Offers various access levels: (See 1.1.4.2.8 for managing roles)
1.2.1.3 Home Page for each user:
1.2.1.3.1 Displaying recent posts from followed interest areas and users.
1.2.1.3.2 Suggesting new posts and interest areas that are relevant to its user based on the users interests. This system shall use the main tagging system to make the semantic connections between the users interests and the suggestions(See "1.2.3.1 Tags")
1.2.1.4 Annotations
1.2.1.4.1 Annotations shall have the [W3C Web Annotation Data Model](https://www.w3.org/TR/annotation-model/).
1.2.1.4.2 Annotations shall appear in form of a highlight made on the annotated text without displaying any extra content.
1.2.1.4.3 Annotations shall display a pop-up over the highlighted areas upon user interaction and only then provide its contents within this pop-up.
1.2.1.4.4 Annotations shall only be placed on Post main bodies.
1.2.2 Search and Filtering
1.2.2.1 The system shall allow users to search for posts, users, and IAs based on semantic labels, metadata, and interest areas.
1.2.2.2 The system shall enable post filtering by interest areas, date, location, and other metadata.
1.2.2.3 The system shall enable the user to sort search results by relevance, date, and popularity.
1.2.2.4 The system shall allow public and private IAs to be searchable.
1.2.3 Labeling
1.2.3.1 Tags
1.2.3.1.1 The system shall utilize [Wikidata](https://www.wikidata.org/) API, in order to implement a semantic labeling mechanism on the platform and this mechanism shall appear in form of tags under each post or IA.
1.2.3.1.2 Upon user interaction, each tag shall be able to display more tags, to which it is semantically related.
1.2.3.1.3 The system shall facilitate post and IA searching based on these tags
1.2.3.1.5 Tags shall allow users to find interest areas, users, and posts related to themselves.
1.2.3.2 Reputation system:
1.2.3.2.1 The system shall allow users to vote on other users based on their qualities and it shall keep record of these votes.
1.2.3.2.2 Votes shall represent either positive or negative side of a quality of the user.
1.2.3.2.3 The system shall assign badges to users depending on how many positive and negative votes they received on a certain quality.
1.2.4 Reporting and Moderation
1.2.4.1 Moderation Dashboard available to IA moderators shall grant abilities for:
1.2.4.1.1 Removing inappropriate posts from the IA.
1.2.4.1.2 To warn users that create such inappropriate posts or misbehave under comment sections.
1.2.4.1.3 Banning users from the IA.
1.2.4.1.4 Reporting issues to System Administrators in case these issues require actions outside the scope of the Moderation Dashboard.
1.2.4.2 Administration Dashboard available to System Administrators shall grant abilities for:
1.2.4.2.1 Removing inappropriate posts or IAs from the platform.
1.2.4.2.2 Warning users that create such inappropriate posts or misbehave under comment sections.
1.2.4.2.3 Banning users from the platform.
1.2.5 Account Management
1.2.5.1 When a user's account is deleted, all account information including the username, password, phone number and email address shall be deleted from the database.
1.2.5.2 All private IAs created by deleted account shall be deleted along with the posts created in them.
1.2.5.3 Public posts, comments, private IAs, and public IAs created by deleted account shall remain visible on the platform.
1.2.5.4 The system shall not allow creating more than one account with the same email address. The attempt to do so shall prompt a warning.
1.2.5.5 The system shall check the birthday of a user during the access to age-restricted content. This information is immutable after account creation.
2 Non-Functional Requirements
2.1 Platforms
2.1.1 Application shall be available for Web and Android platforms.
2.1.2 The web version of the application shall be compatible with commonly used web browsers, including Google Chrome, Mozilla Firefox, and Safari.
2.1.3 The Android version of the application shall be compatible with Android 5.0 and higher.
2.2 Security
2.2.1 User authorization information shall be encrypted.
2.2.2 The application shall implement strong password requirements and provide guidance to users on creating secure passwords.
2.3 Privacy and Ethical Considerations
2.3.1 The platform shall protect personal information and contact information, adherence to copyrights, and licensing considerations; according to [GDPR](https://gdpr-info.eu/)/[KVKK](https://www.mevzuat.gov.tr/mevzuat?MevzuatNo=6698&MevzuatTur=1&MevzuatTertip=5) rules.
2.3.2 The application shall have a concrete "Community Guidelines" to bring Users and System Administrators on the same page in terms of appropriate content and behavior allowed on the platform.
2.4 Restricted Content
2.4.1 Adult content should have age restrictions.
2.4.2 Application shall not contain criminal content and gore.
