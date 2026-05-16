# Python REST API Inventory Management System

## Overview
This project is a Flask-based REST API inventory management system.
It allows users to create, read, update, and delete inventory items while also integrating with the OpenFoodFacts API to fetch product information by barcode.

## Features
- View all inventory items
- View a single inventory item
- Add new inventory items
- Update inventory items
- Delete inventory items
- Search products using OpenFoodFacts API
- CLI frontend for interacting with the API
- Unit testing with pytest

## Technologies Used
- Python
- Flask
- Requests
- Pytest
- Git/GitHub

## API Routes

### Inventory Routes
- `GET /inventory`
- `GET /inventory/<id>`
- `POST /inventory`
- `PATCH /inventory/<id>`
- `DELETE /inventory/<id>`

### External API Route
- `GET /food/<barcode>`

## Installation

Clone the repository:

```bash
git clone <your-repo-url>
```

Navigate into the project folder:

```bash
cd python-REST-API-inventory-system
```

Create virtual environment:

```bash
python -m venv venv
```

Activate virtual environment:

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the Application

Start Flask server:

```bash
python app.py
```

Run CLI frontend:

```bash
python cli.py
```

## Running Tests

```bash
pytest
```

## Author
Alyssa Mercado
