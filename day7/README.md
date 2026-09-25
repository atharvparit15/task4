# Week 4 - Day 7

## React + Django Integration

### Topics Learned

1. CORS
2. React and Django Integration
3. Frontend-Backend Connection
4. Fetch API
5. GET, POST, PUT and DELETE Requests
6. Full Stack API Integration

### CORS

CORS was configured to allow the React frontend to communicate with the Django backend.

### Package Installed

```text
pip install django-cors-headers
```

### Settings Configuration

In `tasktracker/settings.py`:

```python
INSTALLED_APPS = [
    'corsheaders',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tasks',
]
```

### Middleware

```python
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
```

### CORS Configuration

```python
CORS_ALLOW_ALL_ORIGINS = True
```

### API Connection

The React frontend was connected to the Django backend using the API URL:

```javascript
const API_URL = "http://127.0.0.1:8000/tasks";
```

### React + Django Features Tested

* Display tasks from Django backend
* Create a new task
* Mark a task as completed
* Update task status
* Delete a task

### Testing Result

The React frontend successfully communicated with the Django backend.

A task was:

1. Loaded from Django
2. Created from React
3. Updated using PUT request
4. Deleted using DELETE request

### Day 7 Result

The React frontend and Django backend were successfully integrated. The complete Task Tracker application was tested with GET, POST, PUT and DELETE API operations.
