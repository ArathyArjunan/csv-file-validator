# csv-file-validator


## Description  
Develop a Django REST Framework (DRF) API endpoint that processes user data from a CSV
file. This task evaluates your ability to build APIs, handle file uploads, validate data, and
interact with a database effectively.
## Features  
- RESTful API development   
- Unit testing with Django  

## Installation  

### Prerequisites  
- Python 3 
- Django 5.1.5

### Steps to Install  
1. Clone the repository:  
   - git clone [repository-link]
   - cd [project-directory]
   - create virtual environment if needed (python -m venv venv)
   - pip install -r requirements.txt  
   - python manage.py runserver
3. Create .env file
4. copy content of .env.sample and replace secret key value
5. API ENDPOINT:http://127.0.0.1:8000/api/file-upload/
    - {
    "file":""}
  provide a csv file
6. Unit test can be done using
   - python manage.py test

