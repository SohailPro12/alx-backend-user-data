# Simple API

Simple HTTP API for playing with `User` model.

## Files

### `models/`

- `base.py`: base of all models of the API - handle serialization to file
- `user.py`: user model

### `api/v1`

- `app.py`: entry point of the API
- `views/index.py`: basic endpoints of the API: `/status` and `/stats`
- `views/users.py`: all users endpoints

## Setup

```
$ pip3 install -r requirements.txt
```

## Run

```
$ API_HOST=0.0.0.0 API_PORT=5000 python3 -m api.v1.app
```

## Routes

- `GET /api/v1/status`: returns the status of the API
- `GET /api/v1/stats`: returns some stats of the API
- `GET /api/v1/users`: returns the list of users
- `GET /api/v1/users/:id`: returns an user based on the ID
- `DELETE /api/v1/users/:id`: deletes an user based on the ID
- `POST /api/v1/users`: creates a new user (JSON parameters: `email`, `password`, `last_name` (optional) and `first_name` (optional))
- `PUT /api/v1/users/:id`: updates an user based on the ID (JSON parameters: `last_name` and `first_name`)

### What Authentication Means

**Authentication** is the process of verifying the identity of a user, device, or entity in a computer system. It ensures that the person or device requesting access is indeed who or what it claims to be.

Common authentication methods include:

- **Passwords**: The most common form of authentication.
- **Tokens**: Usually used in API calls.
- **Biometrics**: Fingerprints, retina scans, etc.
- **Multi-Factor Authentication (MFA)**: Combining two or more authentication methods.

### What Base64 Is

**Base64** is an encoding scheme that converts binary data into text format so that it can be easily transmitted over text-based protocols such as HTTP. Base64 is often used to encode data that needs to be stored and transferred over media that are designed to deal with textual data.

### How to Encode a String in Base64

To encode a string in Base64 in Python, you can use the `base64` module.

Here’s an example:

```python
import base64

# Original string
original_string = "Hello, World!"

# Encode the string
encoded_bytes = base64.b64encode(original_string.encode("utf-8"))
encoded_string = encoded_bytes.decode("utf-8")

print(f"Encoded string: {encoded_string}")
```

This will output:

```
Encoded string: SGVsbG8sIFdvcmxkIQ==
```

### What Basic Authentication Means

**Basic Authentication** is a simple authentication scheme built into the HTTP protocol. It uses a username and password to authenticate a user and is base64 encoded. The username and password are combined into a single string `"username:password"` and then encoded using Base64.

### How to Send the Authorization Header

When using Basic Authentication, the credentials are sent in the `Authorization` header. Here’s how you can do it in Python using the `requests` library:

```python
import base64
import requests

# Your credentials
username = "myUsername"
password = "myPassword"

# Encode the credentials in Base64
credentials = f"{username}:{password}"
encoded_credentials = base64.b64encode(credentials.encode("utf-8")).decode("utf-8")

# URL of the API endpoint
url = "https://api.example.com/data"

# Set up the headers with the Authorization header
headers = {
    "Authorization": f"Basic {encoded_credentials}"
}

# Make the request
response = requests.get(url, headers=headers)

# Print the response
print(response.status_code)
print(response.text)
```

In this example, the `Authorization` header is constructed with the `Basic` keyword followed by the base64-encoded credentials.

### Summary

- **Authentication** verifies the identity of a user or device.
- **Base64** is an encoding scheme that converts binary data into text.
- **Basic Authentication** uses a base64-encoded string of the username and password to authenticate a user.
- The **Authorization header** is used to send the encoded credentials in an HTTP request.

Understanding these concepts is essential for handling authentication in web applications and APIs.
