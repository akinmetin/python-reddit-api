# Getting Started for Python Reddit API Server

These instructions will assist you to run the API server.

## Prerequisites

* Python 3.8.6 or above

## Installing & Preparation for Local Environment

1. Download the repository and extract it to any folder.
2. Create a virtual environment in the root folder with using ``python -m venv venv`` command.
3. Activate the virtual environment with using ``source venv/bin/activate`` for MacOS/Linux and ``venv\Scripts\activate`` for Windows.
4. Enter into root folder and install required python packages with using ``pip install -r requirements.txt``.

## Running Locally

1. Define environmental variable ``DEBUG_MODE=1`` to run the Flask API with DEBUG mode or set ``DEBUG_MODE=0`` to run the Flask API without DEBUG mode. You can set your environmental variable with putting this into ``.env`` file in the folder or exporting with ``export DEBUG_MODE=1`` for MacOS/Linux systems.
2. Execute ``python app.py`` command.

### Allowed API HTTP(s) requests

| Request Type | Use                                 |
| ------------ |:----------------------------------- |
| ``GET``      | Get a resource or list of resources |

## API Endpoints

| Request Type      | Endpoint                    | What it does                                                          |
| ----------------- |:--------------------------- |:--------------------------------------------------------------------- |
| ``GET``           | ``/posts/top``              | Returns the top 5 post titles based on the score in descending order  |

### Description of Usual Server Responses

*   200 OK - the request was successful.
*   201 Created - the request was successful and a resource was created.
*   204 No Content - the request was successful but there is no representation to return (i.e. the response is empty).
*   400 Bad Request - the request could not be understood or was missing required parameters.
*   401 Unauthorized - authentication failed or user doesn't have permissions for requested operation.
*   403 Forbidden - access denied.
*   404 Not Found - resource was not found.
*   405 Method Not Allowed - requested method is not supported for resource.
*   500 Internal Server Error - the server encountered an unexpected condition which prevented it from fulfilling the request.

## Development

* ``flake8`` and ``pylint`` libraries are used for coding standards and quality testing.

## Testing
1. Enter into root folder and and execute ``python -m unittest discover -s tests/``.

## Coverage

1. Enter into root folder and execute ``coverage run -m unittest discover -s tests/ -p test_*.py``.
2. Execute ``coverage report -m`` command to get the coverage report.

| File Name              | Coverage                       |
| ---------------------- |:------------------------------ |
| ``app.py``             | ``100%``                       |
| ``utils.py``           | ``100%``                       |
