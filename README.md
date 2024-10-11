
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

### 5. Attendance List
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

### PDF Generation
- **URL**: /api/pdfgen/
- **Method**: \GET\
- **Description**: Generate pdf from attendance records

| Parameter  | Type   | Required | Example    |
|------------|--------|----------|------------|
| course     | string | yes      | GRE111     |
| date       | string | yes      | 2024-10-05 |
| start_time | string | yes      | 16:45:34   |
| stop_time  | string | yes      | 16:45:34   |

#### Example:
`http://localhost:8000/api/pdfgen/GRE112/2024-10-05/15:45:11/19:00:00/`
Note : use your browser to get the pdf

#### Example Response: 
A pdf should be downloaded 


### Venue Add

- **URL**: /api/venueadd/
- **Method**: \POST\
- **Description**: API to create venue

| Parameter  | Type   | Required | Example                                        |
|------------|--------|----------|------------------------------------------------|
| short_name | string | yes      | PTDF                                           |
| full_name  | string | yes      | Petroleum Technology<br/> Development Facility |
| latitude   | number | yes      | 7.97588646295044                               |
| longitude  | number | yes      | 5.041485459813603                              |

#### Example using `cURL`:
```shell
curl --location 'http://localhost:8000/api/venueadd/' \
--header 'Authorization: Token c0af34fd2f8fac7cb84595a9ca18789f465cab35' \
--header 'Content-Type: application/json' \
--data '{
        "short_name": "PTDF",
        "full_name": "Petroleum Technology Development Facility",
        "latitude": 7.97588646295044,
        "longitude": 5.041485459813603
    }'
```

#### Example Response:
```json
{
    "short_name": "PTDF",
    "full_name": "Petroleum Technology Development Fund",
    "latitude": 7.97588646295044,
    "longitude": 5.041485459813603
}
```


### Venue List
- **URL**: /api/venuelist/
- **Method**: \GET\
- **Description**: API to list the venues

| Parameter  | Type   | Required | Example                                        |
|------------|--------|----------|------------------------------------------------|
| short_name | string | yes      | PTDF                                           |
| full_name  | string | yes      | Petroleum Technology<br/> Development Facility |
| latitude   | number | yes      | 7.97588646295044                               |
| longitude  | number | yes      | 5.041485459813603                              |

#### Example using `cURL`:
```shell
curl --location 'http://localhost:8000/api/venuelist/' \
--header 'Authorization: Token c0af34fd2f8fac7cb84595a9ca18789f465cab35'
```

#### Example Response:
```json
[
    {
        "short_name": "ELF",
        "full_name": "Engineering Lecture Facility",
        "latitude": 7.97539261202521,
        "longitude": 5.04020118110904
    },
    {
        "short_name": "PTDF",
        "full_name": "Petroleum Technology Development Facility",
        "latitude": 7.97588646295044,
        "longitude": 5.041485459813603
    }
]
```

### 3.Token Generator
- **URL**: /api/login/
- **Method**: \POST\
- **Description**: Generates tokens used for authentication

#### Example using `cURL`:
```shell
curl --location 'http://localhost:8000/api/login/' \
--header 'Content-Type: application/json' \
--data '{
    "username": "admin",
    "password": "admin"
}'
```

#### Example Response:
```json

{   
  "token": "c0af34fd2f8fac7cb84595a9ca18789f465cab35",
  "user_id": 1, 
  "username": "admin"
}

```
### Using the login in react 

#### Here’s a simple function using fetch to send a POST request to your Django login API from a React component:
```jsx
const login = async (username, password) => {
  try {
    const response = await fetch('http://localhost:8000/api/custom-login/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ username, password }),
    });

    if (!response.ok) {
      throw new Error('Login failed');
    }

    const data = await response.json();
    console.log('Login successful! Token:', data.token);

    // Optionally, store the token in localStorage for future API requests
    localStorage.setItem('token', data.token);
    
    return data; // Return the response data if needed
  } catch (error) {
    console.error('Error:', error);
  }
};

// Example usage:

 login('admin', 'admin');

```


#### Once you've successfully obtained the token, you can use it in your API requests by including it in the Authorization header. Here's a simple example of how to use the token in subsequent API requests in React:
##### Here’s how you can use the token stored in localStorage for authenticated API requests:
```jsx
const fetchDataWithToken = async () => {
  const token = localStorage.getItem('token'); // Get the token from localStorage

  try {
    const response = await fetch('http://localhost:8000/api/protected-endpoint/', {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Token ${token}`, // Include the token in the Authorization header
      }
    });

    if (!response.ok) {
      throw new Error('Request failed');
    }

    const data = await response.json();
    console.log('Data received:', data);
    
    return data; // Return the fetched data if needed

  } catch (error) {
    console.error('Error:', error);
  }
};

// Example usage:
fetchDataWithToken();

```

Explanation:

-  Token Retrieval: We fetch the token from localStorage where it was saved during the login process.
- Authorization Header: The token is included in the Authorization header as Token <your_token>. 
- API Request: We make a GET request to the protected API endpoint. You can change the method to POST, PUT, etc., if needed.
- Error Handling: If the request fails, it throws an error that can be caught and logged.