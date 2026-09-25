# Week 4 - Day 4

## Django POST API

### Topics Learned

1. POST Request
2. JSON Request Body
3. Creating Database Records
4. JsonResponse
5. CSRF Exemption
6. API Testing

### POST API

A POST API was created to add a new task to the database.

### API Endpoint

```text
POST http://127.0.0.1:8000/tasks/create/
```

### View Code

```python
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Task


@csrf_exempt
def create_task(request):
    if request.method == "POST":
        data = json.loads(request.body)

        task = Task.objects.create(
            title=data.get("title", ""),
            description=data.get("description", ""),
        )

        return JsonResponse({
            "id": task.id,
            "title": task.title,
            "description": task.description,
            "completed": task.completed,
        })

    return JsonResponse(
        {"error": "POST request required"},
        status=400
    )
```

### URL Configuration

`tasks/urls.py`

```python
path("tasks/create/", create_task, name="create-task"),
```

### Request Body

```json
{
    "title": "Practice API",
    "description": "Learn POST request in Django"
}
```

### API Response

```json
{
    "id": 2,
    "title": "Practice API",
    "description": "Learn POST request in Django",
    "completed": false
}
```

### Testing

The POST API was tested using PowerShell by sending a JSON request to the API endpoint.

### Day 4 Result

The POST API was successfully created and tested. A new task was added to the Django database using a JSON request.
