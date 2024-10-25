# PROJECT HBnB

# Introduction

The HBNB Project is a collaborative effort by a team of four, aimed at building a complete web application for property rental, inspired by platforms like Airbnb. This repository includes our UML model for class structure and relationships, Business Logic (BL) detailing core workflows, and a RESTful API for frontend integration.

This project allowed us to deepen our skills in backend development, database management, and teamwork in a dynamic coding environment.


## Usage

```python
curl -X POST "http://127.0.0.1:5000/api/v1/users/" -H "Content-Type: application/json" -d '{
    "first_name": "John",
    "last_name": "Doe",
    "email": "john.doe@example.com"
    }'

# expected response

{
    "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "first_name": "John",
    "last_name": "Doe",
    "email": "john.doe@example.com"
}
// 200 OK
```
Testing invalid input

```python
curl -X POST "http://127.0.0.1:5000/api/v1/users/" -H "Content-Type: application/json" -d '{
    "first_name": "",
    "last_name": "",
    "email": "invalid-email"
}'

# expected response

{
    "error": "Invalid input data"
}

// 400 Bad Request
```

## AUTHORS

The authors are Lucas Lebran, Ema Decot, Jeremy Sousa, Mariama Goudiaby
