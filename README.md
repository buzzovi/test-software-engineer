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

Requirement | User Story | Importance | Acceptance Criteria | Notes
------------ | ------------- | ------------- | ------------- | -------------
Technical documentation | A developer/administrator wants to be able to understand how the web application is built | CRITICAL | Sufficient technical documentation available |
Add basic update | A user wants to be able to post a basic update | CRITICAL | XXX |
Add update with image | A user wants to be able to post an update with an image | MEDIUM | XXX |
View updates | A user wants to be able to view all updates | CRITICAL | XXX | Sorted with the newest update first, and so that it displays the author, the date and the text
Filter updates | A user wants to be able to filter updates that contain a specific keyword | LOW | XXX |
Add comment | A user wants to be able to add a comment to an update | CRITICAL | XXX |
Update comment | A user wants to be able to update an existing comment | LOW | XXX |
View comments | A user wants to be able to view all comments on each update | CRITICAL | XXX | Sorted with the oldest comment first, and so that it displays the author, the date and the text
Delete comment | A user wants to be able to delete an existing comment | HIGH | XXX |
Comment deletion notification | An administrator wants to get notified when a user deletes a comment | HIGH | XXX |
Logging | An administrator wants to be able to access logs of all actions performed by users | MEDIUM | XXX |
Security | An administrator wants to be able to trust that the webapp has been coded securely | HIGH | AWS services permissionned following the principle of least privilege |
Authentication | A user wants to be able to authenticate to the webapp | LOW | XXX |

## Constraints

## Technical architecture

Please replace the text in this section with a short paragraph detailing how you will be architecting the solution. Which services you are going to use, why you think that they're the most appropriate and how they interact with each other. We're not looking for a fully detailed technical documentation here, but at least something that quickly enables us (and other developers) to understand what you've done and how.
