# EMS: Event Management System

This is a portal system which helps to manage multi-team events such as Annual Sports Meet or Inter college tournaments or Cultural Fest etc. This is built in frappe bench with some updations in server side and client side.

So let's see the overview of the protal.

Various doctypes and child tables (as per the need) are implemented which will be discussed below.

### Features of EMS

- Main Event
- Sub Event
- Teams Participating
- Sub Events Format (fixtures and results)
- Medals per sub events
- Medal Tally

We have implemented these features using various doctypes. 

![1](https://user-images.githubusercontent.com/45628486/198974589-d447e311-d68a-445e-b297-d899f1f70cdb.jpeg)

Now let us see these features in details. Here an event named Intercollege Table Tennis Tournament has been created and managed through this app so you will be able to get an idea about the work flow of this system

<b>Note:</b> In the following doctypes, there are various instances where sub events and teams are filtered as per the main event selected by the user, this has been done in js (client side scripting) and is available in the repository at .js file in ems/ems/doctype/doctype_name folder. Simiplarly python scripting has been done in .py files present in the same location

- <b>Main Event:</b><br>
Doctype: MainEvent
![2](https://user-images.githubusercontent.com/45628486/198984496-8690bc7a-5dc1-429c-8e4d-091a568b982d.jpeg)
![3](https://user-images.githubusercontent.com/45628486/198988885-8af0cd22-6c7b-49f2-a379-4ba4880293e3.jpeg)

- <b>Sub Event:</b><br>
Doctype: SubEvent
List of Sub events created for Inter college table tennis tournament
Now in this following image see the details to be entered while creating a subevent:
![4](https://user-images.githubusercontent.com/45628486/198992434-6ea39005-f333-4f1c-bf42-131294fbcc94.jpeg)
<b>Note:</b> The name of subevent is stored as a unique code concatenated with the main event name to avoid duplicacy as men's singles can be an event in Table Tennis or Badmintor or Squash etc. Its scripting has been done in python (server side scripting) using autoname function. 

- <b>Teams Participating:</b><br>
Doctype: TeamRegistration 
![10](https://user-images.githubusercontent.com/45628486/198999777-5e82f77c-10da-4bae-b11f-d7cfb1a15a60.jpeg)
Now see the fields to be entered with registering a team
![11](https://user-images.githubusercontent.com/45628486/199001091-bc91951a-d7fd-435b-b8ca-96c5567daf8c.jpeg)
![12](https://user-images.githubusercontent.com/45628486/199001104-402c9a17-0bfc-4b70-83a8-0673f36e8689.jpeg)

- <b>Sub Events Format (fixtures and results):</b><br>
Doctype: SubEventFormat
![5](https://user-images.githubusercontent.com/45628486/199002220-5d7b8b8e-5bfd-4069-94f9-4a7734f902c4.jpeg)
![6](https://user-images.githubusercontent.com/45628486/199002253-58b58d8e-6cef-41dd-8ec5-3e6a6a8e4438.jpeg)


- <b>Medals per sub events:</b><br>
Doctype: SubEventWiseMedals

- <b>Medal Tally:</b><br>
Doctype: Medal Table
