-- CREATE DATABASE SATS;
CREATE DATABASE SATS;
-- Use the SATS database
USE SATS;

-- Table: students
CREATE TABLE students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,  -- Automatically generated unique identifier for each student
    matriculation_number VARCHAR(20) NOT NULL UNIQUE,  -- Unique matriculation number for each student
    name VARCHAR(100) NOT NULL,  -- Name of the student (up to 100 characters)
    department VARCHAR(50),  -- Department the student belongs to (optional)
    enrollment_year INT,  -- Year the student enrolled (optional)
    user_id INT,  -- Foreign key referencing the CustomUser table
    FOREIGN KEY (user_id) REFERENCES CustomUser(user_id) ON DELETE CASCADE  -- Establish the foreign key relationship; delete student record if associated user is deleted
);

-- Table: courses
CREATE TABLE courses (
    course_id INT AUTO_INCREMENT PRIMARY KEY,  -- Automatically generated unique identifier for each course
    course_name VARCHAR(100) NOT NULL,  -- Name of the course (up to 100 characters)
    department VARCHAR(50)  -- Department offering the course (optional)
);

-- Table: attendance
CREATE TABLE attendance (
    attendance_id INT AUTO_INCREMENT PRIMARY KEY,  -- Automatically generated unique identifier for each attendance record
    student_id INT,  -- Foreign key referencing the students table
    course_id INT,  -- Foreign key referencing the courses table
    is_present BOOLEAN,  -- Indicates whether the student was present (true/false)
    FOREIGN KEY (student_id) REFERENCES students(student_id),  -- Link to the students table
    FOREIGN KEY (course_id) REFERENCES courses(course_id)  -- Link to the courses table
);

-- Table: CustomUser
CREATE TABLE CustomUser (
    user_id INT AUTO_INCREMENT PRIMARY KEY,  -- Automatically generated unique identifier for each user
    first_name VARCHAR(150) NOT NULL,  -- User's first name (up to 150 characters)
    last_name VARCHAR(150) NOT NULL,  -- User's last name (up to 150 characters)
    phone_number VARCHAR(15),  -- User's phone number (optional, up to 15 characters)
    role VARCHAR(10) NOT NULL DEFAULT 'student',  -- Role of the user (default is 'student')
    username VARCHAR(150) UNIQUE NOT NULL,  -- Unique username for the user
    email VARCHAR(254) UNIQUE,  -- Unique email address for the user (optional)
    password VARCHAR(128) NOT NULL,  -- Password storage (up to 128 characters)
    is_staff BOOLEAN NOT NULL DEFAULT FALSE,  -- Indicates if the user is a staff member (true/false)
    is_active BOOLEAN NOT NULL DEFAULT TRUE,  -- Indicates if the user account is active (true/false)
    date_joined TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,  -- Timestamp for when the user joined (defaults to current time)
    last_login TIMESTAMP NULL DEFAULT NULL,  -- Timestamp for the last login (optional)
    CONSTRAINT role_enum_check CHECK (role IN ('teacher', 'student', 'admin'))  -- Constraint to restrict roles to specific values
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Table: Venue
CREATE TABLE Venue (
    id INT AUTO_INCREMENT PRIMARY KEY,  -- Automatically generated unique identifier for each venue
    short_name VARCHAR(10) NOT NULL,  -- Short name for the venue (up to 10 characters)
    full_name VARCHAR(255) NOT NULL,  -- Full name of the venue (up to 255 characters)
    latitude FLOAT NOT NULL,  -- Latitude of the venue (floating-point number)
    longitude FLOAT NOT NULL,  -- Longitude of the venue (floating-point number)
    altitude FLOAT,  -- Altitude of the venue (optional)
    CONSTRAINT check_latitude CHECK (latitude BETWEEN -90 AND 90),  -- Check constraint to ensure latitude is valid
    CONSTRAINT check_longitude CHECK (longitude BETWEEN -180 AND 180)  -- Check constraint to ensure longitude is valid
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
