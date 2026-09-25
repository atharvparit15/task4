# Week 4 - Day 3

## Django GET API

### Topics Learned

1. Django Views
2. JsonResponse
3. URL Routing
4. GET Request
5. Creating a REST API endpoint

### GET API

A GET API was created to retrieve all tasks from the database.

### API Endpoint

```text
GET http://127.0.0.1:8000/tasks/
```

### View Code

```python
from django.http import JsonResponse
from .models import Task


def task_list(request):
    tasks = Task.objects.all()

    data = [
        {
            "id": task.id,
            "title": task.title,
            "description": task.description,
            "completed": task.completed,
        }
        for task in tasks
    ]

    return JsonResponse(data, safe=False)
```

### URL Configuration

`tasks/urls.py`

```python
from django.urls import path
from .views import task_list

urlpatterns = [
    path("tasks/", task_list, name="task-list"),
]
```

### Project URL Configuration

`tasktracker/urls.py`

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("tasks.urls")),
]
```

### API Response

```json
[
    {
        "id": 1,
        "title": "Learn Django",
        "description": "Complete Django backend practice",
        "completed": false
    }
]
```

### Day 3 Result

The GET API was successfully created and tested. It retrieves task data from the Django database and returns it in JSON format.

