import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Task


@csrf_exempt
def task_list(request, task_id=None):

    # GET - Get all tasks
    if request.method == "GET":
        tasks = Task.objects.all()

        data = []

        for task in tasks:
            data.append({
                "id": task.id,
                "name": task.name,
                "description": task.description,
                "status": task.status,
                "created_date": task.created_date,
            })

        return JsonResponse(data, safe=False)

    # POST - Create new task
    elif request.method == "POST":
        try:
            body = json.loads(request.body)

            task = Task.objects.create(
                name=body.get("name", ""),
                description=body.get("description", ""),
                status=body.get("status", "Pending")
            )

            return JsonResponse({
                "id": task.id,
                "name": task.name,
                "description": task.description,
                "status": task.status,
                "created_date": task.created_date,
            }, status=201)

        except json.JSONDecodeError:
            return JsonResponse({
                "error": "Invalid JSON"
            }, status=400)

    # PUT - Update task
    elif request.method == "PUT":
        try:
            if task_id is None:
                return JsonResponse({
                    "error": "Task ID is required"
                }, status=400)

            task = Task.objects.get(id=task_id)

            body = json.loads(request.body)

            task.name = body.get("name", task.name)
            task.description = body.get(
                "description",
                task.description
            )
            task.status = body.get(
                "status",
                task.status
            )

            task.save()

            return JsonResponse({
                "id": task.id,
                "name": task.name,
                "description": task.description,
                "status": task.status,
                "created_date": task.created_date,
            })

        except Task.DoesNotExist:
            return JsonResponse({
                "error": "Task not found"
            }, status=404)

        except json.JSONDecodeError:
            return JsonResponse({
                "error": "Invalid JSON"
            }, status=400)

    # DELETE - Delete task
    elif request.method == "DELETE":
        try:
            if task_id is None:
                return JsonResponse({
                    "error": "Task ID is required"
                }, status=400)

            task = Task.objects.get(id=task_id)

            task.delete()

            return JsonResponse({
                "message": "Task deleted successfully"
            })

        except Task.DoesNotExist:
            return JsonResponse({
                "error": "Task not found"
            }, status=404)

    # Method not allowed
    return JsonResponse({
        "error": "Method not allowed"
    }, status=405)
