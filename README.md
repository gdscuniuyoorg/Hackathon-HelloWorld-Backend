
# Attendance System

## Overview
This project is an attendance system built with Django, which includes an API to calculate the distance of a user from a specified venue. The purpose of the API is to determine the proximity of users to the venue for attendance verification.

### Features:
- Django Rest Framework for handling API requests
- API to get the distance between a user and a venue
- API to register users
- API to add an attendance record
- API to get attendance within a time frame
- JSON responses
- More Incoming

## Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.x
- Django 3.x or later
- Django Rest Framework (DRF)

## Installation

### 1. Clone the Repository

```shell
git clone https://github.com/yourusername/attendance-system.git
cd attendance-system
```


### 2. Install the Requirements

```
pip install django
pip install djangorestframework
pip install djangorestframework-authtoken
pip install vincenty
```



### 3. Run the Server

Start the Django development server:

```python
python manage.py runserver
```

The project will be available at \`http://127.0.0.1:8000/\`.

## API Endpoints

### 1. **Get Distance of User from Venue**

- **URL**: \`/api/get_distance/\`
- **Method**: \GET\
- **Description**: This API calculates the distance of the user from a venue based on the user's current latitude and longitude, and the venue’s latitude and longitude.

| Parameter | Type   | Required | Example           |
|-----------|--------|----------|-------------------|
| name      | string | yes      | "ELF"             |
| lattitude | number | yes      | 5.043280051864717 |
| longitude | number | yes      | 7.973864477393281 |

#### Example Response:

```json
{
    "distance": 458.703231,
    "Am I Near": "You are far"
}
```

#### Example using `cURL`:

```bash
curl --location 'http://localhost:8000/api/get_distance/?name=ELF&latitude=5.043280051864717&longitude=7.973864477393281' \
--header 'Content-Type: application/json'
```

This will return the distance between the user's location and the venue in kilometers.
The coordinates given are for the hostel in perm site just to get a frame of reference


### 2. Register User
- **URL**: /api/register/
- **Method**: \POST\
- **Description**: This API allows the registration of news users based on the
                    schema description in the model

| Parameter    | Type   | Required | Example              |
|--------------|--------|----------|----------------------|
| username     | string | Yes      | "student"            |
| email        | string | No       | "email@email.com"    |
| password     | string | Yes      | "password_string"    |
| role         | string | Yes      | "student" or "admin" |
| first_name   | string | No       | "firstname"          |
| last_name    | string | No       | "lastname"           |
| phone_number | string | No       | "08012344567"        |
| reg_no       | string | No       | "19_AG_CE_1234"      |

#### Example using `cURL`:

```shell
curl --location 'http://localhost:8000/api/register/' \
--header 'Authorization: Token 52043008de8d2fcd7cdecbe8ae814eccb835cf36' \
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
```
#### Example Response:

```json
{
    "username": "student_3",
    "email": "student_3_email@em.com",
    "first_name": "First",
    "last_name": "Last",
    "phone_number": "08012345678",
    "reg_no": "19_AG_CE_1234",
    "role": "student"
}
```


### 3.Token Generator
- **URL**: /api/token/
- **Method**: \POST\
- **Description**: Generates tokens used for authenticating certain APIs

#### Example using `cURL`:
```shell
curl --location 'http://localhost:8000/api/token/' \
--header 'Content-Type: application/json' \
--data '{
    "username": "admin",
    "password": "admin"
}'
```

#### Example Response:
```json
{
    "token": "52043008de8d2fcd7cdecbe8ae814eccb835cf36"
}
```



### 4. Student Detail
- **URL**: /api/student/reg_no/
- **Method**: \POST\
- **Description**: This API allows the addition of a single attendance record

| Parameter | Type   | Required | Example       |
|-----------|--------|----------|---------------|
| reg_no    | string | yes      | 18_AG_FE_1345 |

#### Example using `cURL`:
```shell
curl --location
 'http://localhost:8000/api/student/19_EG_CO_1247/' \
--header 'Authorization:
 Token 52043008de8d2fcd7cdecbe8ae814eccb835cf36'
```

#### Example response

```json
{
    "username": "student_3",
    "email": "student_3_email@em.com",
    "first_name": "First",
    "last_name": "Last",
    "phone_number": "08012345678",
    "reg_no": "19_EG_CO_1247"
} 
```

### 4. Attendance Create
- **URL**: /api/attendanceadd/
- **Method**: \POST\
- **Description**: Create a single attendance record

| Parameter | Type   | Required | Example       |
|-----------|--------|----------|---------------|
| reg_no    | string | yes      | 19_AG_CO_1234 |
| course    | string | yes      | GRE111        |
| venue     | string | yes      | ELT           |
| date      | string | yes      | 2024-10-05    |
| time      | string | yes      | 16:45:34      |

#### Example using `cURL`:

```shell
curl --location 'http://localhost:8000/api/attendanceadd/' \
--header 'Authorization: Token c0af34fd2f8fac7cb84595a9ca18789f465cab35' \
--header 'Content-Type: application/json' \
--data '{
    "reg_no": "19_AG_CO_1234",    
    "course": "GRE112",     
    "venue": "ELF",
    "date": "2024-10-05",
    "time": "17:45:11"
}'
```

#### Example Response:
```json
{
    "reg_no": "19_AG_CO_1234",
    "time": "17:45:11",
    "course": "GRE112",
    "date": "2024-10-05T00:00:00Z",
    "venue": "ELF"
}
```

### Attendance List
- **URL**: /api/attendancelist/
- **Method**: \GET\
- **Description**: Get attendance records for a course within a time frame

| Parameter  | Type   | Required | Example    |
|------------|--------|----------|------------|
| course     | string | yes      | GRE111     |
| date       | string | yes      | 2024-10-05 |
| start_time | string | yes      | 16:45:34   |
| stop_time  | string | yes      | 16:45:34   |

#### Example using `cURL`:
```shell
curl --location 'http://localhost:8000/api/attendancelist/?course=GRE112&date=2024-10-05&start_time=15%3A45%3A11&stop_time=19%3A45%3A34' \
--header 'Authorization: Token c0af34fd2f8fac7cb84595a9ca18789f465cab35'
```

#### Example Response:
```json
[
    {
        "reg_no": "19_AG_CO_1234",
        "time": "17:45:11",
        "course": "GRE112",
        "date": "2024-10-05T00:00:00Z",
        "venue": "ELF"
    },
    {
        "reg_no": "19_EG_CO_1247",
        "time": "17:45:11",
        "course": "GRE112",
        "date": "2024-10-05T00:00:00Z",
        "venue": "ELF"
    }
]
```
