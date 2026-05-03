# Shopy Backend

Shopy Backend is a Flask API for a full stack product inventory project. It stores products in an in-memory Python list, validates incoming JSON data, and exposes product APIs for the frontend application.

## Features

- Flask application setup.
- Working `GET` API to return product data.
- Working `POST` API to create products from JSON request body.
- In-memory list storage.
- Backend validation for required and invalid fields.
- Optional search, update, delete, and get-by-id endpoints.
- CORS enabled for frontend integration.

## Tech Stack

- Python
- Flask
- Flask-CORS
- In-memory list data store

## Run Locally

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

The API runs at:

```text
http://localhost:5050
```

## APIs

| Method | Endpoint | Description |
| --- | --- | --- |
| `GET` | `/` | Health check route |
| `GET` | `/api/products` | Returns all products |
| `GET` | `/api/products?search=lamp` | Filters products by name, category, or description |
| `GET` | `/api/products/<id>` | Returns one product |
| `POST` | `/api/products` | Creates a new product |
| `PUT` | `/api/products/<id>` | Updates an existing product |
| `DELETE` | `/api/products/<id>` | Deletes a product |

## Product JSON

```json
{
  "name": "Notebook",
  "price": 149,
  "quantity": 20,
  "category": "Stationery",
  "description": "A ruled notebook for class notes."
}
```

## Validation Rules

- `name` is required and cannot be empty.
- `price` is required and must be greater than zero.
- `quantity` is required and cannot be negative.
- `category` is required and cannot be empty.
- `description` is required and cannot be empty.

## Example Requests

Get products:

```bash
curl http://localhost:5050/api/products
```

Create product:

```bash
curl -X POST http://localhost:5050/api/products \
  -H "Content-Type: application/json" \
  -d '{"name":"Notebook","price":149,"quantity":20,"category":"Stationery","description":"A ruled notebook for class notes."}'
```

## Frontend Repository

Frontend GitHub Pages app:

https://abhishek58754-ship-it.github.io/shopy-frontend/

Frontend source repository:

https://github.com/abhishek58754-ship-it/shopy-frontend

## Project Requirements Covered

- Separate backend repository.
- Basic Flask setup.
- Product `GET` API.
- Product `POST` API with JSON body.
- Data stored in list/dictionary style in-memory storage.
- Data validation.
- Optional CRUD endpoints for scoring advantage.
