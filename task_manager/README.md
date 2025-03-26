# Task Management API

## Setup Instructions
1. Clone the repository
2. Create a virtual environment: `python -m venv venv`
3. Activate it: `source venv/bin/activate` (Linux/Mac) or `venv\Scripts\activate` (Windows)
4. Install dependencies: `pip install -r requirements.txt`
5. Run migrations: `python manage.py migrate`
6. Create superuser: `python manage.py createsuperuser`
7. Start server: `python manage.py runserver`

## API Endpoints

1. Create Task

<!-- 
POST /api/tasks/create/
Request Body:
{
"name": "Task Name",
"description": "Task Description",
"task_type": "NORMAL",
"assigned_user_ids": [1, 2]
}
Response: 201 Created with task details
 -->


2. Assign Task to Users

<!-- 
POST /api/tasks/<task_id>/assign/
Request Body:
{
"user_ids": [1, 2, 3]
}
Response: 200 OK with updated task details
 -->

 
3. Get User's Tasks

<!-- 
GET /api/users/<user_id>/tasks/
Response: 200 OK with list of tasks
 -->

 
## Test Credentials
- Username: admin
- Password: admin123
- Test User IDs: Create through admin panel

## Notes
- Uses Django REST Framework for API development
- Implements proper error handling
- Follows Django best practices

To use this implementation:

1. Set up the project:

    django-admin startproject task_manager
    cd task_manager
    django-admin startapp tasks
    pip install -r requirements.txt
    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser
    python manage.py runserver

2. Test the APIs using curl or Postman with the sample requests from README.

    Meets all requirements with proper API endpoints
    Uses ManyToMany relationship for task-user assignments
    Includes proper serialization and validation
    Follows Django and REST best practices
    Has clean, documented code
    Provides comprehensive setup instructions