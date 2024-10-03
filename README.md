
# Attendance System

## Overview
This project is an attendance system built with Django, which includes an API to calculate the distance of a user from a specified venue. The purpose of the API is to determine the proximity of users to the venue for attendance verification.

### Features:
- Django Rest Framework for handling API requests
- API to get the distance between a user and a venue
- API to register users
- JSON responses
- More Incoming

## Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.x
- Django 3.x or later
- Django Rest Framework (DRF)

## Installation

### 1. Clone the Repository

\`\`\`
git clone https://github.com/yourusername/attendance-system.git
cd attendance-system
\`\`\`


### 2. Install the Requirements

\`\`\`
pip install django
pip install djangorestframework
pip install vincenty
\`\`\`



### 3. Run the Server

Start the Django development server:

\`\`\`
python manage.py runserver
\`\`\`

The project will be available at \`http://127.0.0.1:8000/\`.

## API Endpoints

### 1. **Get Distance of User from Venue**

- **URL**: \`/api/get_distance/\`
- **Method**: \GET\
- **Description**: This API calculates the distance of the user from a venue based on the user's current latitude and longitude, and the venue’s latitude and longitude.


#### Example Response:

\`\`\`
{
    "distance": 458.703231,
    "Am I Near": "You are far"
}
\`\`\`

#### Example using `cURL`:

\`\`\`
curl --location 'http://localhost:8000/api/get_distance/?name=ELF&latitude=5.043280051864717&longitude=7.973864477393281' \
--header 'Content-Type: application/json'
\`\`\`

This will return the distance between the user's location and the venue in kilometers.
The coordinates given are for the hostel in perm site just to get a frame of reference


### 2. Register User
- **URL**: \`/api/register/\`
- **Method**: \POST\
- **Description**: This API allows the registration of news users based on the
                    schema description in the model

#### Example Response:

\`\`\`
{
    "username": "student_3",
    "email": "student_3_email@em.com",
    "first_name": "First",
    "last_name": "Last",
    "phone_number": "08012345678",
    "reg_no": null,
    "role": "student"
}
\`\`\`

#### Example using `cURL`:

\`\`\`
curl --location 'http://localhost:8000/api/register/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "username" : "student_3" ,
    "email" : "student_3_email@em.com",
    "password" : "password123",
    "role": "student",
    "first_name": "First",
    "last_name" : "Last",
    "phone_number" : "08012345678"
}'
\`\`\`