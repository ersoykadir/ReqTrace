1 Functional Requirements
1.1 User Requirements
1.1.1 Guests
1.1.1.1 Guests shall be able to see polls.
1.1.1.2 Guests shall not be able to create polls.
1.1.1.3 Guests shall not be able to vote in any polls.
1.1.1.4 Guests shall be able to see other member's profile.
1.1.1.5 Guests shall be able to give feedbacks to developers.
1.1.1.6 Guests shall not be able to add friends.
1.1.1.7 Guests shall be able to sign up or log in from any page within the platform.
1.1.2 Authentication
1.1.2.1 Sign up
1.1.2.1.1 Users should be able to sign up with an unused e-mail, unused nickname and a password.
1.1.2.1.2 Passwords determined by users while signing up shall be at least 8 characters and shall contain at least three of the following:
1.1.2.1.3 Users should get a verification mail to their e-mail address when they sign up.
1.1.2.1.4 Users should be able to sign up with google.
1.1.2.1.5 Users shall accept the KVKK terms to sign up.
1.1.2.2 Sign in
1.1.2.2.1 Users should be able to sign in with their username/email and password if they have verified their e-mail via the verification mail stated in requirement 1.1.2.1.3.
1.1.2.2.2 Users should be able to sign in with google.
1.1.3 Profile
1.1.3.1 Members shall have a profile page which they can display their name, username, profile picture, bio, polls that they created, or they voted for, their domain specific badges and their domain specific ranks.
1.1.3.2 Members shall have a profile page which includes the visibility information about the member.
1.1.3.2.1 Members shall have an option to hide their information except the username.
1.1.3.2.2 Members shall have an option to decide which of their actions will be displayed in their profile.
1.1.4 Members
1.1.4.1 Members shall be able to add friends by sending friend requests and accepting friend requests.
1.1.4.2 Members shall be able to share their achievements on their social media platforms.
1.1.4.3 Members shall be able to share any poll on their social media platforms.
1.1.4.4 Members shall be able to express their views in the comment section of the poll.
1.1.4.5 Members shall be able to view other members' comments in the comment section of the poll.
1.1.4.6 If moderator applications are open, each member can send a request to the system to be a moderator.
1.1.4.7 Members shall be able to search via searchbar.
1.1.4.7.1 Members shall be able to see recommended tags according to the written text while typing.
1.1.4.7.2 Members shall be able to click the recommended tags to search by that tag.
1.1.4.7.3 Members shall be able to search according to written text.
1.1.4.7.3.1 Members shall be able to filter the search result by tags to get polls according to their tags.
1.1.4.7.3.2 Members shall be able to filter the search result by keywords to get polls according to their keywords.
1.1.4.7.3.3 Members shall be able to filter the search result by usernames to get profiles according to their usernames.
1.1.4.8 Members shall receive notifications for friend requests, poll results, and other relevant activities.
1.1.4.9 Members shall be able to block or report other members for inappropriate behavior.
1.1.4.10 Members shall be able to annotate words and expressions in their own polls.
1.1.4.11 Members shall be able to edit annotations in their own polls.
1.1.4.12 Members shall be able to view annotations in other polls.
1.1.5 Polls
1.1.5.1 Poll Opening
1.1.5.1.1 Members shall be able to post polls if they follow the following entries.
1.1.5.1.2 Each poll must have a question.
1.1.5.1.3 Poll opener shall pay 5 * daily gained points, from his/her prediction scores, to open a poll.
1.1.5.1.4 Poll opener shall be able to decide on the visibility of vote distribution of their polls to other users.
1.1.5.1.5 Poll opener shall choose a final voting date or vote change acceptance time-the time that system takes to accept a vote changing process-.
1.1.5.1.6 Poll opener shall be banned from opening polls for one day if one of his polls is reported and removed by jury.
1.1.5.1.7 Poll opener shall choose poll type as multiple-choice or continuous.
1.1.5.1.8 Poll opener shall choose the number of the options.
1.1.5.1.9 Poll opener shall fill every option.
1.1.5.1.10 Poll opener shall choose the input type such as date-time, integer, etc.
1.1.5.2 Poll Voting
1.1.5.2.1 Members shall be able to vote on active polls.
1.1.5.2.2 Members shall be able to change their vote, which changes the option where the member's general points reside.
1.1.5.2.3 Members shall be notified when a poll they participated in is closed and results are available.
1.1.5.3 Poll Closing
1.1.5.3.1 Poll owner shall be able to send a request to finish the poll to the system.
1.1.5.3.2 Members shall be able to receive points from the one and only true guess in the case of multiple-choice polls, or nearly true guesses, in the case of customized input polls. The points received is explained in the system requirements.
1.1.5.4 Annotation
1.1.5.4.1 A poll may feature annotations related to notable terms or expressions.
1.1.6 Moderator
1.1.6.1 Moderators shall be able to do whatever regular members do.
1.1.6.2 Moderators shall choose at least one at most five tags they are interested in. Tags chosen will be used by the system to determine which moderators can participate in a jury.
1.1.6.3 Moderators shall be able to accept or reject the active join-the-jury requests, explained in system requirements, they received.
1.1.6.3.1 Moderators shall participate in the jury for resolving a poll.
1.1.6.3.1.1 A moderator in a jury shall be able to set the answer whatever he/she considers to be correct in 24 hours.
1.1.6.3.1.2 If the poll the jury is responsible for is subjective, each jury member should set the suggested answer as the correct answer.
1.1.6.3.1.3 Otherwise, each jury member should do his/her own research and set his/her answer accordingly.
1.1.6.3.2 Moderators shall be able to participate in the jury investigating reports for a poll.
1.1.6.3.2.1 Each jury member shall be able to vote for either delete the poll, not to delete the poll, or set the poll as finished.
1.1.6.4 Moderators shall not be able to accept passive join-the-jury requests. (Explained in system requirements)
1.1.7 Point System
1.1.7.1 Domain Specific Point
1.1.7.1.1 Members shall be able to receive domain specific points by predicting correct answer in polls.
1.1.7.1.2 Members shall be able to see all of their domain specific points.
1.1.7.1.3 Members shall be able to receive badges from their domain specific points according to their achievements.
1.1.7.2 General Point
1.1.7.2.1 Members shall be able to receive a proportion of received domain specific points as general points.
1.1.7.2.2 Members shall be able to receive general points if they enter the platform daily/weekly.
1.1.7.2.3 Members shall be able to use their general points to open a poll in any domain with according to requirement 1.1.4.1.4 .
1.1.7.2.4 Members shall be able to use their general points to vote on polls.
1.1.7.2.5 Members shall be able to receive points with same amount to open a poll(1.1.4.1.4) when they sign up the platform.
1.1.7.2.6 Members shall be notified when they earn or lose points.
1.1.7.3 Leaderboard
1.1.7.3.1 Members shall be able to see their ranks about a specific tag in the leaderboard.
1.1.7.3.2 Members shall be able to share their ranks about a specific tag in their profile.
1.1.8 Notifications
1.1.8.1 Members shall be able to customize their notification preferences.
1.1.8.2 Members shall receive notifications for friend requests, poll results, comments on their polls, and other relevant activities.
1.2 System Requirements
1.2.1 Polls
1.2.1.1 Poll Opening
1.2.1.1.1 System shall tag the polls depending on their content.
1.2.1.2 Poll Continuity
1.2.1.2 System shall periodically notify the poll owners that created polls with no due dates to check if the poll should be ended.
1.2.1.3 Poll Vote Change
1.2.1.3.1 If the poll has a final voting date, system shall accept member's vote change immediately.
1.2.1.3.2 If the poll has a vote change acceptance time, system shall accept member's vote change after the vote change acceptance time has passed.
1.2.1.4 Poll Closing
1.2.1.4.1 System shall take %10 from the profit of the poll voters that won more points than their initial points.
1.2.2 Grading
1.2.2.1 System shall grant points to the members according to the proximity of their voting time to the poll posting time. The granted points will be determined by a linear function in which the closer the voter gets to the deadline the lower the reward points will be.
1.2.2.2 Polls with indefinite due dates shall not be subject to linear incremental grading. (TBD)
1.2.2.3 System shall award points to members based on the accuracy of their guesses in continuous polls.
1.2.2.4 In continuous polls, the closeness shall be defined as the absolute difference between the guess and the result.
1.2.2.5 System shall consider three possibilities for the distribution of members: top 50%, bottom 50%, and all members making the same guess.
1.2.2.6 If the member is at the top 50%, the system shall return their deposited points back.
1.2.2.7 The system shall divide top 50% into four parts based on performance, and each part shall share a certain percentage of the points of the losers:
1.2.2.7.1 The system shall share %5 of the points of the losers to the bottom 25% division.
1.2.2.7.2 The system shall share %15 of the points of the losers to the next better division.
1.2.2.7.3 The system shall share %25 of the points of the losers to the next better division.
1.2.2.7.4 The system shall share %45 of the points of the losers to the top %25 division.
1.2.2.8 The system shall take the points of the bottom 50% as they are losers.
1.2.2.9 If everyone makes the same guess, the system shall return the deposited points without any rewards or penalties.
1.2.2.10 If there is a tie between members in the top 50%, the system shall split rewards among the tied members starting from the best-performing division (i.e., the top 25%).
1.2.2.11 System shall share points to members proportional to their deposited points.
1.2.2.12 System shall burn the remaining 10% of the points to prevent point inflation.
1.2.2.13 System shall award the member reporting illegal content with half of the points required to open a poll, following verification of the content's illegality.
1.2.2.14 For multiple choice polls, system shall award all deposited points to members who predicted correctly proportional to their deposited points.
1.2.3 Jury
1.2.3.1 To gather a jury for a poll, the system shall send join-the-jury requests only to appropriate moderators (check glossary for definition).
1.2.3.2 The system shall send join-the-jury requests to appropriate moderators if the poll is reported by more than 250 unique members.
1.2.3.3 The system shall send join-the-jury requests to appropriate moderators if the poll has ended and a finish request is sent to the system either by the system or the poll owner.
1.2.3.4 The system shall set the initial prize for each join-the-jury request to %2 of total points placed in the poll.
1.2.3.5 If nine moderators accept the join-the-jury request, the system shall set the join-the-jury requests for the same poll as passive. (Look to Moderator section for more details about accepting join-the-jury requests)
1.2.3.6 If no nine moderators accept the join-the-jury request in six hours, the system shall send the join-the-jury request again to each appropriate moderator but this time with doubled prize. The system shall repeat this process until a jury of nine is gathered. Moreover, the system will set the previous requests to passive.
1.2.3.7 If jury does not answer the poll in time, System shall punish each jury member that did not set the correct answer or vote for the action to be taken by burning %10 of the points of the members aforementioned.
1.2.3.8 If jury does not answer the poll in time, the system shall send the join-the-jury request again to each appropriate moderator again but this time with doubled prize. Moreover, the system shall disarrange the previous jury.
1.2.3.9 The system shall open moderator applications whenever total number of polls whose answer is not yet determined divided by the number of moderators is greater than fifteen.
1.2.3.10 The system shall promote members that applied for the moderatorship if they conform to two following criteria:
1.2.3.10.1 The member used the application in the 3 days past the date the application is being considered.
1.2.3.10.2 The member has participated in more than 10 polls either by posting them or voting for them.
1.2.3.11 After each promotion of member to moderator, the system shall close the application for moderatorship and reject all the remaining applications if total number of polls whose answer is not yet determined divided by the number of moderators is less than fifteen.
1.2.3.12 If the juries' decisions aren't unanimous then the decision with highest percentage is applied.
1.2.3.13 In a case like requirement 1.2.3.12 juries in the lower percentage will not be awarded.
2 Non-Functional Requirements
2.1 Portability and Compatibility Requirements
2.1.1 The website shall be able to run on Google Chrome, Yandex, Safari, Microsoft Edge and Firefox seamlessly, any failure regarding its specified performance and scalability requirements and any change in its behavior.
2.1.2 The application shall be able to run on Android API 24 and later versions seamlessly with consistent behavior.
2.2 Performance and Scalability Requirements
2.2.1 Web Application Performance
2.2.1.1 The web application's initial load time shall not exceed 5 seconds on broadband connections.
2.2.1.2 For subsequent page loads (after caching), the load time should not exceed 2 seconds.
2.2.1.3 Asynchronous web requests should receive a response within 1 second under normal load conditions.
2.2.2 Mobile Application Performance
2.2.2.1 The mobile app should launch within 3 seconds from a stopped state on devices released within the past three years.
2.2.2.2 Screen transition within the mobile application should not exceed 1 second.
2.2.2.3 API calls initiated from the mobile application to the backend should receive a response within 1.5 seconds under normal load conditions.
2.2.3 Scalability
2.2.3.1 The system should be scalable horizontally, allowing for the addition of servers or instances without significant changes to system architecture.
2.2.4 Data Transfer
2.2.4.1 Images and media loaded in the mobile and web apps should be optimized for their respective platforms to reduce unnecessary data transfer.
2.3 Reliability, Maintainability, Availability Requirements
2.4 Security Requirements
2.4.1 An unauthorized access to admin panel shall be blocked by defining different login flows and different user roles as user actions.
2.4.2 All nicknames shall be different from each other.
2.4.3 KVKK provisions shall be applied.
2.4.4 The passwords should be stored securely.
