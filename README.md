# Todo List Application

This application is a simple Todo List manager implemented using Python with a GUI built using Tkinter. It utilizes MySql as the backend database to store and manage the tasks.

## Features

Add tasks: Easily add new tasks with a title and optional description.
View tasks: See all tasks currently in the list.
Mark tasks as completed: Check off tasks that have been finished.
Delete tasks: Remove tasks from the list when they are no longer needed.
Requirements
Python 3.x
Tkinter (usually comes with Python installation)
MySql

## Installation

Clone the repository:

```git clone https://github.com/Newbieprogram22/To-Do-List```

Navigate to the project directory:

```cd todo-list```

## Usage

Run the application:

```python Root.py```

The GUI window will open. You can start adding tasks after registration (if you are a new user) and login.

## Database

The application uses MySql as the database backend.


### Create databse
``` create database todo_list; ```

### Createa tables in database
```
# to create user table in todo list database
create table if not exists user_table(
    user_name varchar(50),
    user_email varchar(100),
    user_contact varchar(20),
    user_pwd varchar(25),
    user_conf_pwd varchar(25)
);
```
```
# to create table in todo list database
create table if not exists tasks (
  	task_id INT AUTO_INCREMENT PRIMARY KEY,
    task_name varchar(120),
    task_description TEXT,
    task_status VARCHAR(50),
    created_by varchar(100)
);
```
