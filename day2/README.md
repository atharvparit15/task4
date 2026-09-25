# Week 4 - Day 2

## Django Models and Admin Panel

### Topics Learned

1. Django Models
2. Model Fields
3. SQLite Database
4. Migrations
5. Django Admin Panel
6. Superuser

### Task Model

The `Task` model was created with the following fields:

* `title` - Task title
* `description` - Task description
* `completed` - Task completion status
* `created_at` - Task creation date and time

### Model Code

```python
from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
```

### Migrations

The database migrations were created and applied using:

```text
python manage.py makemigrations
python manage.py migrate
```

### Django Admin

The `Task` model was registered in the Django Admin Panel.

### Admin Code

```python
from django.contrib import admin
from .models import Task

admin.site.register(Task)
```

### Superuser

A Django superuser was created to access the Admin Panel.

### Command Used

```text
python manage.py createsuperuser
```

### Admin URL

```text
http://127.0.0.1:8000/admin/
```

### Task Created

**Title:** Learn Django

**Description:** Complete Django backend practice

### Day 2 Result

The Task model was successfully created, migrated to the SQLite database, registered in the Django Admin Panel, and a task was created using the admin interface.
