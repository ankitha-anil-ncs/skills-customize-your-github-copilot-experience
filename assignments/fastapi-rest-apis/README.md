# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build fast, modern REST APIs using the FastAPI framework. You'll create a complete API with endpoints for managing resources, handling requests and responses, and implementing best practices for web development.

## 📝 Tasks

### 🛠️ Create a Task Management API

#### Description
Build a REST API for managing tasks using FastAPI. This API should handle CRUD operations (Create, Read, Update, Delete) for a task list with different endpoints for various operations.

#### Requirements
Completed program should:

- Define a Task model with properties like id, title, description, and completed status
- Implement GET endpoint to retrieve all tasks or a specific task by ID
- Implement POST endpoint to create a new task
- Implement PUT endpoint to update an existing task
- Implement DELETE endpoint to remove a task
- Use proper HTTP status codes for different responses

### 🛠️ Add Data Validation and Error Handling

#### Description
Enhance your API with robust data validation and comprehensive error handling to ensure data integrity and provide meaningful feedback to clients.

#### Requirements
Completed program should:

- Use Pydantic models for request/response validation
- Validate task input data (e.g., title is not empty, required fields are present)
- Handle and return appropriate error messages for invalid requests
- Return 404 status when a task is not found
- Include proper documentation for all endpoints using FastAPI's automatic documentation
