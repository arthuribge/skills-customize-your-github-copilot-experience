# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small REST API with FastAPI to manage tasks, practice HTTP routes, request validation, and JSON responses, and understand how a modern Python web framework handles CRUD operations.

## 📝 Tasks

### 🛠️ Set up a FastAPI app

#### Descrição
Create a new FastAPI application that starts from a simple in-memory task list and exposes a health check endpoint.

#### Requisitos
O programa concluído deve:

- Import `FastAPI` and create an app instance.
- Expose a `GET /health` endpoint returning a JSON object such as:
  ```json
  {"status": "ok"}
  ```
- Run the app with Uvicorn using a local development command such as:
  ```bash
  uvicorn main:app --reload
  ```
- Confirm that the app loads successfully in the browser or Swagger UI at `/docs`.

### 🛠️ Create the task model

#### Descrição
Define a task model and use Pydantic to validate incoming data for creating and updating tasks.

#### Requisitos
O programa concluído deve:

- Create a `Task` model with fields such as `id`, `title`, and `completed`.
- Create a `TaskCreate` model for incoming requests.
- Validate that `title` is required and not empty.
- Return JSON responses in a consistent format.
- Example request body:
  ```json
  {
    "title": "Learn FastAPI",
    "completed": false
  }
  ```

### 🛠️ Implement CRUD endpoints

#### Descrição
Build the API endpoints to list, create, read, update, and delete tasks.

#### Requisitos
O programa concluído deve:

- Implement `GET /tasks` to return all tasks.
- Implement `POST /tasks` to create a new task.
- Implement `GET /tasks/{task_id}` to return one task by ID.
- Implement `PUT /tasks/{task_id}` to update a task.
- Implement `DELETE /tasks/{task_id}` to remove a task.
- Return `404` with an appropriate error when a task is not found.
- Use an in-memory list or dictionary as the data store for this assignment.

### 🛠️ Add validation and error handling

#### Descrição
Improve the API by adding response validation, clean error messages, and route-level checks.

#### Requisitos
O programa concluído deve:

- Return a proper HTTP status code for each operation (`200`, `201`, `404`, `204`, etc.).
- Validate that task IDs are numeric and valid.
- Handle missing or invalid values gracefully with clear messages.
- Keep the responses structured and easy to consume in JSON.
- Example response:
  ```json
  {
    "id": 1,
    "title": "Learn FastAPI",
    "completed": true
  }
  ```

### 🛠️ Bonus: query parameters and filtering

#### Descrição
Extend the API by adding a simple filter or query parameter feature.

#### Requisitos
O programa concluído deve:

- Support a query parameter such as `completed=true`.
- Filter tasks according to the selected value.
- Example route:
  ```http
  GET /tasks?completed=true
  ```
- Return only tasks matching the query.

