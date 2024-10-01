
# Attendance System

## Overview
This project is an attendance system built with Django, which includes an API to calculate the distance of a user from a specified venue. The purpose of the API is to determine the proximity of users to the venue for attendance verification.

### Features:
- API to get the distance between a user and a venue
- Django Rest Framework for handling API requests
- JSON responses
- More Incoming

## Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.x
- Django 3.x or later
- Django Rest Framework (DRF)

## Installation

### 1. Clone the Repository

\`\`\`bash
git clone https://github.com/yourusername/attendance-system.git
cd attendance-system
\`\`\`


### 2. Install the Requirements

\`\`\`bash
pip install django
pip install djangorestframework
pip install vincenty
\`\`\`



### 3. Run the Server

Start the Django development server:

\`\`\`bash
python manage.py runserver
\`\`\`

The project will be available at \`http://127.0.0.1:8000/\`.

## API Endpoint

### 1. **Get Distance of User from Venue**

- **URL**: \`/api/get_distance/\`
- **Method**: \GET\
- **Description**: This API calculates the distance of the user from a venue based on the user's current latitude and longitude, and the venue’s latitude and longitude.


#### Example Response:

\`\`\`json
{
  "distance_km": 4.12
}
\`\`\`

#### Example using `cURL`:

\`\`\`bash
curl --location 'http://localhost:8000/api/get_distance/?name=ELF&latitude=5.043280051864717&longitude=7.973864477393281' \
--header 'Content-Type: application/json'
\`\`\`

This will return the distance between the user's location and the venue in kilometers.
The coordinates given are for the hostel in perm site just to get a frame of reference

