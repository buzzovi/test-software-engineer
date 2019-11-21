# The Kaizen blog

Hi there! And welcome to the technical test stage of our interview process for becoming a Kaizen Software Engineer!

Normally at that point, you should already be aware of what will be expected from you over the next few hours.

So let's jump straight into it!

## Overview

We want you to create a web application that will be used as an "internal blog". The objective here is to let Kaizen staff members share updates and comment on those updates through a single-page web UI, as shown below:

![Example](https://github.com/KaizenReporting/test-software-engineer/blob/master/The%20Kaizen%20Blog.jpg?raw=true)

Users don't have to be authenticated. Anyone within the organisation can access this webapp and post updates and comments. They just have to enter their name and the message they want to post. (And optionally an image for updates if they want to)

Users can also delete comments. Again, it doesn't matter whether they posted the comment they want to delete or not, here any user is able to delete any comment, there is no concept of authentication. However, what we'll want in a situation where a comment is deleted, is to send an email to alert administrators about it.

Below is the full list of requirements. We recommend you to start by documenting the technical architecture you plan on implementing before doing any actual work. (Last section of this document)

## Requirements

Requirement | User Story | Importance | Acceptance Criteria
------------ | ------------- | ------------- | -------------
Technical documentation | A developer/administrator wants to be able to understand how the web application is built | CRITICAL | Sufficient technical documentation available
Add basic update | A user wants to be able to post a basic update | CRITICAL | Given I'm on the Kaizen Blog, When I enter my username and the update I want to share, and click on the "Post!" button, Then my update is published and displayed at the top of the list
Add update with image | A user wants to be able to post an update with an image | MEDIUM | Given I'm on the Kaizen Blog, When I am in the process of posting an update, Then I can add a picture to it that will be displayed below the text of the update
View updates | A user wants to be able to view all updates | CRITICAL | Given I'm on the Kaizen Blog, When I browse through the page, Then I can view all updates sorted with the newest update first. When I am looking at a particular update, Then I can see the author, date, text and optional picture of the update
Filter updates | A user wants to be able to filter updates that contain a specific keyword | LOW | Given I'm on the Kaizen Blog, When I enter a keyword in the search field, Then the list of updates is refreshed to only display those updates that contain my keyword in the text of the update
Add comment | A user wants to be able to add a comment to an update | CRITICAL | Given I'm on the Kaizen Blog, When I enter my username, comment and click on "Comment!", right below an update, Then my comment is published and displayed below all other comments for this update
Edit comment | A user wants to be able to edit a comment | LOW | Given I'm on the Kaizen Blog, When I click on the "Edit" button next to a comment, Then I can directly edit the comment using an inline form. When I have submitted the form to edit a comment, Then the new comment is displayed in place of the old comment, and the "(edited)" text is displayed next to the comment
View comments | A user wants to be able to view all comments on each update | CRITICAL | Given I'm on the Kaizen Blog, When I browse through the page, Then I can view all comments for all updates sorted with the oldest comment first. When I am looking at a particular comment, Then I can see the author, date, text, an "Edit" button and a "Delete" button
Delete comment | A user wants to be able to delete a comment | HIGH | Given I'm on the Kaizen Blog, When I click on the "Delete" button next to a comment, Then I get prompted to confirm my action. When I confirm that I want to delete the comment, Then the comment is deleted and not displayed on the page anymore
Comment deletion notification | An administrator wants to get notified when a user deletes a comment | HIGH | Given I'm an administrator, When a user deletes a comment, Then I receive an email notification telling me which comment just got deleted
Logging | An administrator wants to be able to access logs of all actions performed by users | MEDIUM | Given I'm on the Kaizen Blog, When I perform any action, Then logs of that action are generated and saved in the backend
Backend security | An administrator wants to be able to trust that the webapp has been coded securely | HIGH | AWS services permissionned following the principle of least privilege
IP whitelisting | An administrator wants to be able to launch the stack with IP whitelisting configured | MEDIUM | Given I'm an administrator, When I launch the stack, Then I can specify an IP address that will be the only location from where users are able to access the Kaizen Blog
Like | A user want to be able to "like" updates | LOW | Given I'm on the Kaizen Blog, When I am looking at a particular update, Then I can "like" that update. When I "like" an update, then the count of likes for that update is increased by 1 and displayed next to the update

## Constraints

## Technical architecture

Please replace the text in this section with a short paragraph detailing how you will be architecting the solution. Which services you are going to use, why you think that they're the most appropriate and how they are going to interact with each other. We're not looking for a fully detailed technical documentation here, but at least something that quickly enables us (and other developers) to understand what you've done and how.
