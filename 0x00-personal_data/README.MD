### What Is PII, non-PII, and Personal Data?

**Personally Identifiable Information (PII)**:

- PII refers to information that can be used to identify, contact, or locate a single person.
- Examples: Full name, Social Security number, email address, home address, phone number, passport number.

**Non-PII**:

- Non-PII is information that cannot be used to identify an individual on its own.
- Examples: Gender, race, religion, preferences, aggregated data.

**Personal Data**:

- Personal data is any information related to an identified or identifiable person.
- This term is often used in the context of data protection laws, like GDPR.

### Logging Documentation

Python’s `logging` module provides a flexible framework for emitting log messages from Python programs.

- **Documentation**: [Python Logging Documentation](https://docs.python.org/3/library/logging.html)
- **Basic Usage**:

  ```python
  import logging

  logging.basicConfig(level=logging.INFO)
  logging.info("This is an info message")
  ```

### Bcrypt Package

**bcrypt** is a library to help hash passwords. It's designed to be computationally expensive in order to protect against brute-force attacks.

- **Installation**:

  ```bash
  pip install bcrypt
  ```

- **Usage**:

  ```python
  import bcrypt

  # Hashing a password
  password = b"super secret password"
  hashed = bcrypt.hashpw(password, bcrypt.gensalt())

  # Checking a password
  if bcrypt.checkpw(password, hashed):
      print("It matches")
  else:
      print("It does not match")
  ```

### Logging to Files, Setting Levels, and Formatting

- **Logging to Files**:

  ```python
  logging.basicConfig(filename='app.log', level=logging.INFO)
  logging.info("This will be logged to the file")
  ```

- **Setting Levels**:

  ```python
  logging.basicConfig(level=logging.DEBUG)
  logging.debug("Debug information")
  ```

- **Formatting**:
  ```python
  logging.basicConfig(
      format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
      level=logging.INFO
  )
  ```

### Examples of Personally Identifiable Information (PII)

- Full name
- Social Security number
- Driver’s license number
- Bank account number
- Credit card number
- Email address
- Home address
- Phone number
- Date of birth

### How to Implement a Log Filter that Will Obfuscate PII Fields

You can create a custom log filter to obfuscate PII fields in your logs.

- **Example**:

  ```python
  import logging
  import re

  class PIIObfuscationFilter(logging.Filter):
      def filter(self, record):
          record.msg = re.sub(r'\b\d{3}-\d{2}-\d{4}\b', 'XXX-XX-XXXX', record.msg)
          record.msg = re.sub(r'\b\d{4}-\d{4}-\d{4}-\d{4}\b', 'XXXX-XXXX-XXXX-XXXX', record.msg)
          return True

  logger = logging.getLogger()
  logger.addFilter(PIIObfuscationFilter())
  logging.basicConfig(level=logging.INFO)
  logging.info("User SSN is 123-45-6789 and credit card number is 1234-5678-9012-3456")
  ```

### How to Encrypt a Password and Check the Validity of an Input Password

Using the `bcrypt` package as shown above, you can hash passwords and verify them.

- **Hashing a Password**:

  ```python
  hashed = bcrypt.hashpw(password, bcrypt.gensalt())
  ```

- **Checking a Password**:
  ```python
  if bcrypt.checkpw(password, hashed):
      print("It matches")
  else:
      print("It does not match")
  ```

### How to Authenticate to a Database Using Environment Variables

Using environment variables is a secure way to manage database credentials.

- **Setting Environment Variables**:

  ```bash
  export DB_USER='myuser'
  export DB_PASSWORD='mypassword'
  export DB_HOST='localhost'
  export DB_NAME='mydatabase'
  ```

- **Using Environment Variables in Python**:

  ```python
  import os
  import psycopg2  # Example for PostgreSQL

  DB_USER = os.getenv('DB_USER')
  DB_PASSWORD = os.getenv('DB_PASSWORD')
  DB_HOST = os.getenv('DB_HOST')
  DB_NAME = os.getenv('DB_NAME')

  conn = psycopg2.connect(
      dbname=DB_NAME,
      user=DB_USER,
      password=DB_PASSWORD,
      host=DB_HOST
  )

  # Do database operations
  ```

Understanding these concepts will help you handle sensitive data securely and perform efficient logging, encryption, and authentication in your applications.
