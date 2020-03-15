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
 - `ClientID` referencing `Client.ID`
 They are both primary keys to prevent clients from joining the same course twice and creating a lot of redundancy
 
 TBC
