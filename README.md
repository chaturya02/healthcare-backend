# Healthcare Backend

A robust healthcare backend system built with Django and Django REST Framework that manages patients, doctors, and their relationships.

## Features

- User Authentication with JWT
- Patient Management
- Doctor Management
- Patient-Doctor Relationship Management
- RESTful API
- PostgreSQL Database
- Secure Environment Configuration

## Prerequisites

- Python 3.8+
- PostgreSQL
- pip (Python package manager)

## Installation

1. Clone the repository

```bash
git clone <repository-url>
cd Healthcare
```

2. Create a virtual environment and activate it

```bash
python -m venv venv
# On Windows
.\venv\Scripts\activate
# On Unix or MacOS
source venv/bin/activate
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Create a .env file in the root directory with the following variables:

```
DEBUG=True
SECRET_KEY=your-secret-key
DB_NAME=healthcare_db
DB_USER=your-db-user
DB_PASSWORD=your-db-password
DB_HOST=localhost
DB_PORT=5432
```

5. Run migrations

```bash
python manage.py migrate
```

6. Create a superuser

```bash
python manage.py createsuperuser
```

7. Run the development server

```bash
python manage.py runserver
```

## API Endpoints

### Authentication

- `POST /api/auth/register/` - Register a new user
- `POST /api/auth/login/` - Login and get JWT token
- `POST /api/auth/token/refresh/` - Refresh JWT token

### Patients

- `GET /api/patients/` - List all patients
- `POST /api/patients/` - Create a new patient
- `GET /api/patients/<id>/` - Get a specific patient
- `PUT /api/patients/<id>/` - Update a patient
- `DELETE /api/patients/<id>/` - Delete a patient

### Doctors

- `GET /api/doctors/` - List all doctors
- `POST /api/doctors/` - Create a new doctor
- `GET /api/doctors/<id>/` - Get a specific doctor
- `PUT /api/doctors/<id>/` - Update a doctor
- `DELETE /api/doctors/<id>/` - Delete a doctor

### Patient-Doctor Mappings

- `GET /api/mappings/` - List all mappings
- `POST /api/mappings/` - Create a new mapping
- `GET /api/mappings/<id>/` - Get a specific mapping
- `PUT /api/mappings/<id>/` - Update a mapping
- `DELETE /api/mappings/<id>/` - Delete a mapping

## Models

### Patient

- First Name
- Last Name
- Date of Birth
- Gender
- Contact Number
- Email
- Address
- Medical History
- Created At
- Updated At

### Doctor

- First Name
- Last Name
- Specialization
- License Number
- Contact Number
- Email
- Address
- Created At
- Updated At

### PatientDoctorMapping

- Patient (Foreign Key)
- Doctor (Foreign Key)
- Assigned Date
- Notes
- Active Status

## Authentication

The API uses JWT (JSON Web Tokens) for authentication. To access protected endpoints:

1. Obtain a token by logging in
2. Include the token in the Authorization header:

```
Authorization: Bearer <your-token>
```

## Development

1. Make sure all tests pass:

```bash
python manage.py test
```

2. Check code style:

```bash
flake8
```

## Security Considerations

- Environment variables are used for sensitive data
- JWT authentication for API security
- PostgreSQL for robust data storage
- CORS configuration for frontend security

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request
