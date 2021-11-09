# HR-Right Employee Management System
### Video Demo: https://youtu.be/ZBhr_KBlbFg
## How the project works?
### This employee manager app allows Admin to login and add employees or view a list of employees. At first login, the admin sees employees.html. Admin has the option to click on a link that takes them to register.html. Register.html has a form to enter all employee information. Admin gives new employees a default password that prompts them to reset their password.
### When a new employee logs in with their default password, they are sent to update.html to reset their password. After password is reset, they are sent back to login.html. After logging in the employee is directed to index.html where they have a link to view their profile. The link takes the employee to profile.html where they’re employee information can be seen (first name, last name, address, and pay rate).
### Both admin and employees can login and logout. If an error occurs with the password or username, they are directed to error.html which gives a description of the error. Errors for passwords not matching are seen on error.html. Username not found sends the user to error.html. 
###  *Login:
###     * Email
### 	* Password
### 	* Check Admin/Emp
## Technologies Used:
###	 *sqlite3
###	 *Python
###	 *Flask
## Routing
### Each route checks if the user is authenticated or password and email are correct. Admin and or EMP option must be chosen at login. /login does not require authentication. Other routes like /register is only for admin and require auth. All Employee routes require auth (/index, /profile, /update)
## Sessions
### The webpage uses sessions to confirm that the user is registered via “user_id”. No cookies are stored, and the filesystem is used. 
## Database
## The database stores all users as admin or employees. The primary key is id for the “employees” table.

## How can this project be improved?
### This app is a prototype and can be improved upon. Mainly CSS needs improvement. The project is not responsively designed. My design choice is simple, and I debated whether employee manager apps should be straight to the point. As an employee, I want to login and get the information that I need was my thought process. Each page has the same design, and I debated whether I should change the design based on what the purpose of the page. As CSS can be tricky, I wanted to focus on delivering a project that works. My focus was on the backend and not the design. I figure design can always be improved upon as long as the backend works. 
