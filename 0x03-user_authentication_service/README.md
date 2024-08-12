### 1. How to Declare API Routes in a Flask App

In Flask, routes are used to map URLs to functions, which handle requests made to those URLs. Declaring routes in a Flask app is straightforward:

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')  # Root route
def index():
    return "Welcome to the homepage!"

@app.route('/api/data', methods=['GET'])  # API route for GET requests
def get_data():
    return {"data": "Here is some data"}

@app.route('/api/data', methods=['POST'])  # API route for POST requests
def post_data():
    return {"message": "Data received"}, 201

if __name__ == '__main__':
    app.run(debug=True)
```

- **`@app.route()`** is used to declare a route. The first argument is the URL path, and the `methods` argument specifies the allowed HTTP methods (e.g., GET, POST).
- **Functions** mapped to routes handle incoming requests to those URLs.

### 2. How to Get and Set Cookies

Flask makes it easy to get and set cookies in your app:

- **Setting Cookies**: You can set cookies using the `set_cookie()` method on the response object.

```python
from flask import Flask, make_response

@app.route('/set-cookie')
def set_cookie():
    response = make_response("Cookie is set")
    response.set_cookie('username', 'Sohail')
    return response
```

- **Getting Cookies**: You can retrieve cookies from the request using the `request.cookies` dictionary.

```python
from flask import Flask, request

@app.route('/get-cookie')
def get_cookie():
    username = request.cookies.get('username')
    return f'Username is {username}'
```

### 3. How to Retrieve Request Form Data

To retrieve data submitted via an HTML form (usually through POST requests), you use the `request.form` dictionary:

```python
from flask import Flask, request

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    return f"Logged in as {username} with password {password}"
```

- **`request.form.get('key')`** retrieves the value associated with the form input named `key`.

### 4. How to Return Various HTTP Status Codes

Flask allows you to return HTTP status codes along with your responses easily:

```python
from flask import Flask, jsonify

@app.route('/success')
def success():
    return jsonify(message="Success!"), 200  # 200 OK

@app.route('/created')
def created():
    return jsonify(message="Resource created"), 201  # 201 Created

@app.route('/bad-request')
def bad_request():
    return jsonify(error="Bad request"), 400  # 400 Bad Request

@app.route('/not-found')
def not_found():
    return jsonify(error="Not found"), 404  # 404 Not Found
```

- **Status codes** are specified as the second element in the return tuple. Flask will return the appropriate status code to the client.
  
By understanding these concepts, you can effectively create and manage API routes, handle cookies, process form data, and return appropriate HTTP responses in a Flask app.
