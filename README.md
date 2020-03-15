# Courses
 This is a school Flask application assignment.\
 It consist of a SQLite3 database, 5 html files and 1 python file as a website handler.
 
 ## Purpose
 It is web application that records the courses available and number of current participants
 
 ## Database
 It is a sqlite3 database that consist of 3 tables: Course, Client, ClientCourse
 
 **Course consist of 4 columns:**
 - `ID`, the course ID, the primary key
 - `Name`
 - `MaxPax`, meaning the maximum number of participants that can join in a course
 - `CurrPax`, meaning the number of participants that have already joined
 
 **Client consist of 2 columns:**
 - `ID`, the client ID
 - `Email`
 
 **ClientCourse consist of 2 columns:**
 - `CourseID` referencing `Course.ID`
 - `ClientID` referencing `Client.ID`\
 They are both primary keys to prevent clients from joining the same course twice and creating redundancy
 
 ## HTML files
 There is a lot of redirecting going around because I *like* to make my code complicated and I *really like* to spends hours in front of my computer debugging.
 
 **`base.html`**
 This the header of all the other html files. This is just to make the code neater
 
 **`display.html`**
 If there are no courses available, the page will ask you to create a course.
 Otherwise, it is the main page which diplays information about the course in the order of:
 - ID
 - Course Name
 - Maximum Pax
 - Current Pax\
 There are 2 additional columns called 'Join Course' and 'Status'.\
 The 'Join Course' columne basically does what it says. It redirects the client to `join.html` and allow clients to insert their email to join their chosen course.\
 The 'Status' redirects clients to `status.html` where it shows the all the participants that are already in the course.\
 There is a 'Create!' button at the bottom left of the table that redirects clients to 'new_course.html', which allow clients to create more ~~silly~~ courses.
 
 **`join.html`**
 As mentioned above, it allows clients to insert their email to join their chosen course. It is just a form that ask client to input their emails. However, if client had already joined the course, the page will inform them why their email cannot be process and provide them with an option to join other course which basically redirects them back to the display page.
 
 **`status.html`**
 As mentioned above, it shows all participants that are already participating in the course. It show the information in the order of:
 - Participant ID
 - Email\
 However, if there are no participants currently participating in the course, the page will ask the client to join the particular course, redirecting back to `join.html`.
 
 **`new_course.html`**
 As mentioned above, it allow clients to create course.\
 The form ask the information in the order of:
 - Course Name
 - Maximum Participants
 The `ID` is set to autoincrement and the `CurrPax` is by default 0.
 
 **`web_handler`**
 I'm too lazy to type this now. 
