README.md
# Online Course Management API

This project is a RESTful API designed for managing instructors, courses, and lessons. It provides functionality to create, update, delete, list, and retrieve data.

## 📋 Features

- Instructor Management: Add, list, update, delete, and view instructors.
- Course Management: Manage course information with start and end date validation.
- Lesson Management: Create and organize lessons with course association and order validation.

---

## 🛠 Installation and Setup



Create and activate a virtual environment:
- python -m venv venv
- source venv/bin/activate  # For Linux/Mac
- venv\Scripts\activate     # For Windows







Run migrations:
python manage.py makemigrations
python manage.py migrate



Start the development server:
python manage.py runserver




🛠 API Endpoints
Instructors



Method
Endpoint
Description




GET
/api/instructor/
List all instructors


POST
/api/instructor/
Add a new instructor


GET
/api/instructor/<id>/
Get instructor details


PUT
/api/instructor/<id>/
Update an instructor


DELETE
/api/instructor/<id>/
Delete an instructor



Courses



Method
Endpoint
Description




GET
/api/course/
List all courses


POST
/api/course/
Add a new course


GET
/api/course/<id>/
Get course details


PUT
/api/course/<id>/
Update a course


DELETE
/api/course/<id>/
Delete a course



Lessons



Method
Endpoint
Description




GET
/api/lesson/
List all lessons


POST
/api/lesson/
Add a new lesson


GET
/api/lesson/<id>/
Get lesson details


PUT
/api/lesson/<id>/
Update a lesson


DELETE
/api/lesson/<id>/
Delete a lesson




📂 Code Structure

online-course-api/
├── api/
│   ├── serializers.py       # Data serialization and validation
│   ├── views.py             # API views for handling requests
│   ├── models.py            # Database models
│   ├── urls.py              # API endpoints
│   ├── tests.py             # Unit tests for the API
├── manage.py                # Django's CLI tool
├── requirements.txt         # Project dependencies
├── db.sqlite3               # Default SQLite database

🔧 Key Features and Validation


Models:

Instructor: Stores instructor name, email (unique), and specialty.
Course: Includes title, description, start & end dates, and instructor.
Lesson: Contains lesson title, content, course reference, and order.



Serializers:

InstructorSerializer: Validates unique email and correct format.
CourseSerializer: Ensures start date is before end date.
LessonSerializer: Validates order to be a positive number.



Validation Methods:

validate_email for email format.
validate in CourseSerializer for date constraints.
validate_order for ensuring positive order numbers.




🚀 Usage
Add a New Instructor
Request:


POST /api/instructors/
Content-Type: application/json

Body:


{
  "name": "John Doe",
  "email": "john.doe@example.com",
  "specialty": "Data Science"
}

Response:


{
  "id": 1,
  "name": "John Doe",
  "email": "john.doe@example.com",
  "specialty": "Data Science"
}
