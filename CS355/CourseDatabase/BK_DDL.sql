--- Creation file for database used in cs355 to answer homework questions.

IF EXISTS BK_Prereq;
IF EXISTS BK_Time_slot;
IF EXISTS BK_Advisor;
IF EXISTS BK_Takes;
IF EXISTS BK_Student;
IF EXISTS BK_Teaches;
IF EXISTS BK_Section;
IF EXISTS BK_Instructor;
IF EXISTS BK_Course;
IF EXISTS BK_Department;
IF EXISTS BK_Classroom;

CREATE TABLE BK_Classroom (
  building                varchar(15),
  room_number             varchar(7),
  capacity                numeric(4,0),
  PRIMARY KEY(building, room_number)
);

CREATE TABLE BK_Department (
  dept_name               varchar(20),
  building                varchar(15),
  budget                  numeric(12,2) check (budget > 0),
  PRIMARY KEY (dept_name)
);

CREATE TABLE BK_Course (
  course_id               varchar(8),
  title                   varchar(50),
  dept_name               varchar(20),
  credits                 numeric(2,0) check (credits > 0),
  PRIMARY KEY (course_id),
  FOREIGN KEY (dept_name) references BK_Department (dept_name) 
    on DELETE set NULL
);

CREATE TABLE BK_Intructor (
  ID                      varchar(5),
  name                    varchar(20) NOT NULL,
  dept_name               varchar(20),
  salary                  numeric(8,2) check (salary > 29000),
  PRIMARY KEY (ID),
  FOREIGN KEY (dept_name) references BK_Department (dept_name) 
    on DELETE set NULL
);

CREATE TABLE BK_Section (
  course_id               varchar(8),
  sec_id                  var_char(8),
  semester                var_char(6) check (semester IN ('Fall', 'Winter', 'Spring', 'Summer')),
  year                    numeric(4,0) check (year > 1701 and year < 2100),
  building                varchar(15),
  room_number             varchar(7),
  time_slot_id            varchar(4),
  PRIMARY KEY (course_id, sec_id, semester, year),
  FOREIGN KEY (course_id) references BK_Course (course_id) 
    on DELETE CASCADE,
  FOREIGN KEY (building, room_number) references BK_Classrooom (building, room_number) 
    on DELETE set NULL
);

CREATE TABLE BK_Teaches (
  ID                      varchar(5),
  course_id               varchar(8),
  sec_id                  varchar(8),
  semester                varchar(6),
  year                    numeric(4,0),
  PRIMARY KEY (ID, course_id, sec_id, semester, year),
  FOREIGN KEY (course_id, sec_id, semester, year) references BK_Section (course_id, sec_id, semester, year) 
    on DELETE CASCADE,
  FOREIGN KEY (ID) references BK_Instructor (ID)
    on DELETE CASCADE
);

CREATE TABLE BK_Student (
  ID                      varchar(5),
  name                    varchar(20) NOT NULL,
  dept_name               varchar(20),
  tot_cred                numeric(3,0) check (tot_cred >= 0),
  PRIMARY KEY (ID),
  FOREIGN KEY (dept_name) references BK_Department (dept_name)
     on DELETE set NULL
);

CREATE TABLE BK_Takes (
  ID                      varchar(5),
  course_id               varchar(8),
  sec_id                  varchar(8),
  semester                varchar(6),
  year                    numeric(4,0),
  grade                   varchar(2),
  PRIMARY KEY (ID, course_id, sec_id, semester, year),
  FOREIGN KEY (course_id, sec_id, semester, year) references BK_Section (course_id, sec_id, semester, year)
    on DELETE CASCADE,
  FOREIGN KEY (ID) reference BK_Student (ID)
    on DELETE CASCADE
);

CREATE TABLE BK_Advisor (
  s_ID                    varchar(5),
  i_ID                    varchar(5),
  PRIMARY KEY (s_ID),
  FOREIGN KEY (i_ID) references BK_Instructor (ID)
    on DELETE set NULL,    
  FOREIGN KEY (s_ID) references BK_Student (ID)
    on DELETE set NULL
);

CREATE TABLE BK_Time_slot (
   time_slot_id           varchar(4),
   day                    varchar(1),
   start_hr               numeric(2) check (start_hr >= 0 and start_hr < 24),
   start_min              numeric(2) check (start_min >= 0 and start_min < 60),
   end_hr                 numeric(2) check (end_hr >= 0 and end_hr < 24),
   end_min                numeric(2) check (end_min >= 0 and end_min < 60),
   PRIMARY KEY (time_slot_id, day, start_hr, start_min)
);

CREATE TABLE BK_Prereq (
   course_id               varchar(8),
   prereq_id               varchar(8),
   PRIMARY KEY (course_id, prereq_id),
   FOREIGN KEY (course_id) references BK_Course (course_id),
     on DELETE CASCADE,
   FOREIGN KEY (prereq_id) references BK_Course (course_id)
     on DELETE CASCADE
);
