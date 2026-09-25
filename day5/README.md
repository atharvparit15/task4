# Week 4 - Day 5

## Django PUT and DELETE APIs

### Topics Learned

1. PUT Request
2. DELETE Request
3. Updating Database Records
4. Deleting Database Records
5. URL Parameters
6. Error Handling

### PUT API

The PUT API was created to update an existing task.

### PUT Endpoint

```text
PUT http://127.0.0.1:8000/tasks/update/<task_id>/
```

### Update View

```python
@csrf_exempt
def update_task(request, task_id):
    if request.method == "PUT":
        try:
            task = Task.objects.get(id=task_id)
        except Task.DoesNotExist:
            return JsonResponse({"error": "Task not found"}, status=404)

        data = json.loads(request.body)

        task.title = data.get("title", task.title)
        task.description = data.get("description", task.description)
        task.completed = data.get("completed", task.completed)
        task.save()

        return JsonResponse({
            "id": task.id,
            "title": task.title,
            "description": task.description,
            "completed": task.completed,
        })

    return JsonResponse(
        {"error": "PUT request required"},
        status=400
    )
```

### DELETE API

The DELETE API was created to remove a task from the database.

### DELETE Endpoint

```text
DELETE http://127.0.0.1:8000/tasks/delete/<task_id>/
```

### Delete View

```python
@csrf_exempt
def delete_task(request, task_id):
    if request.method == "DELETE":
        try:
            task = Task.objects.get(id=task_id)
        except Task.DoesNotExist:
            return JsonResponse({"error": "Task not found"}, status=404)

        task.delete()

        return JsonResponse({
            "message": "Task deleted successfully"
        })

    return JsonResponse(
        {"error": "DELETE request required"},
        status=400
    )
```

### URL Configuration

```python
path("tasks/update/<int:task_id>/", update_task, name="update-task"),
path("tasks/delete/<int:task_id>/", delete_task, name="delete-task"),
```

### Update Example

Task 1 was updated with:

```json
{
    "title": "Learn Django Updated",
    "description": "Django backend completed",
    "completed": true
}
```

### Delete Example

Task 2 was deleted successfully using the DELETE API.

### Day 5 Result

The PUT and DELETE APIs were successfully created and tested. Tasks can now be updated and deleted through Django API endpoints.
