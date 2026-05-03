# Shopy Backend

Flask backend for the Shopy product project. Products are stored in an in-memory Python list, so data resets when the server restarts.

## Run

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

The API runs at `http://localhost:5050`.

## APIs

- `GET /api/products` returns all products.
- `GET /api/products?search=lamp` filters products by name, category, or description.
- `GET /api/products/<id>` returns one product.
- `POST /api/products` creates a product using JSON body.
- `PUT /api/products/<id>` updates a product.
- `DELETE /api/products/<id>` deletes a product.

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
