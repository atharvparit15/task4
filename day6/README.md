# Week 4 - Day 6

## API Testing with Postman

### Topics Learned

1. Postman
2. GET Request
3. POST Request
4. PUT Request
5. DELETE Request
6. API Testing

### Postman

Postman was used to test the Django backend APIs and verify that all API operations were working correctly.

### API Endpoints Tested

| Method | Endpoint                   | Purpose           |
| ------ | -------------------------- | ----------------- |
| GET    | `/tasks/`                  | Get all tasks     |
| POST   | `/tasks/create/`           | Create a new task |
| PUT    | `/tasks/update/<task_id>/` | Update a task     |
| DELETE | `/tasks/delete/<task_id>/` | Delete a task     |

### GET Request

```text
GET http://127.0.0.1:8000/tasks/
```

Used to retrieve all available tasks.

### POST Request

```text
POST http://127.0.0.1:8000/tasks/create/
```

Request Body:

```json
{
    "title": "Postman Task",
    "description": "Testing Django API with Postman"
}
```

### PUT Request

```text
PUT http://127.0.0.1:8000/tasks/update/3/
```

Request Body:

```json
{
    "title": "Updated Postman Task",
    "description": "Task updated using Postman",
    "completed": true
}
```

### DELETE Request

```text
DELETE http://127.0.0.1:8000/tasks/delete/3/
```

Used to delete the selected task.

### Testing Result

* GET request: Successful
* POST request: Successful
* PUT request: Successful
* DELETE request: Successful

### Server

The Django development server was also tested using:

```text
python manage.py runserver
```

Server URL:

```text
http://127.0.0.1:8000/
```

### Day 6 Result

All Django API endpoints were successfully tested using Postman. GET, POST, PUT, and DELETE operations were working correctly.
