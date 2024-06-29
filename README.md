# To-Do-List

### Create databse
``` create database todo_list; ```

### Createa tables in database
```
# to create user table in todo list database
create table if not exists user_table(
    user_name varchar(50),
    user_email varchar(100),
    user_contact varchar(20),
    sec_ques varchar(120),
    sec_ans varchar(120),
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
### How to run
Execute the Root.py file.
