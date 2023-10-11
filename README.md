# Flask REST API TEMPLATE

This is a Flask REST API project with clean code, linters, unit tests, Dockerfile, OpenAPI specification.

## Project Structure

The project has the following directory structure:

```
davi-coe-flask-mngr-template
├── app
│   ├── __init__.py
│   ├── config.py
│   ├── controllers
│   │   ├── __init__.py
│   │   └── controller.py
│   ├── models
│   │   ├── __init__.py
│   │   └── model.py
│   ├── routes
│   │   ├── __init__.py
│   │   └── routes.py
│   ├── schemas
│   │   ├── __init__.py
│   │   └── schema.py
│   ├── services
│   │   ├── __init__.py
│   │   └── service.py
│   └── utils
│       ├── __init__.py
│       ├── database.py
│       ├── logger.py
│       └── response.py
├── tests
│   ├── __init__.py
│   ├── controllers
│   │   ├── __init__.py
│   │   └── test_controller.py
│   ├── models
│   │   ├── __init__.py
│   │   └── test_model.py
│   ├── routes
│   │   ├── __init__.py
│   │   └── test_routes.py
│   ├── schemas
│   │   ├── __init__.py
│   │   └── test_schema.py
│   └── services
│       ├── __init__.py
│       └── test_service.py
├── .github
│   └── workflows
│       └── deploy.yml
├── .dockerignore
├── .gitignore
├── Dockerfile
├── openapi.json
├── README.md
├── requirements.txt
├── requirements-gcp.txt
├── main.py
└── wsgi.py
```

The `app` directory contains the Flask application code, including the controllers, models, routes, schemas, services, and utility modules. The `tests` directory contains the unit tests for the application. The `.github` directory contains the GitHub Actions workflow for deploying the application to GCP Functions. The `Dockerfile` contains the instructions to build a Docker image for the application. The `openapi.json` file contains the OpenAPI specification for the application. The `README.md` file contains the documentation for the project. The `requirements.txt` file lists the Python dependencies for the application. The `requirements-dev.txt` file lists the Python dependencies for development and testing. The `requirements-gcp.txt` file lists the Python dependencies for deployment on GCP Functions. The `main.py` file is the entry point for the application when running on GCP Functions. The `wsgi.py` file is the entry point for the application when running on a WSGI server.

## Installation

To install the application, clone the repository and install the dependencies:

```
git clone https://github.com/davivienda-colombia/davi-coe-flask-mngr-template
cd flask-rest-api
python3 -m venv venv
source ./venv/bin/activate
pip install -r requirements-dev.txt
pip install -r requirements.txt
```

## Usage

To run the application, use the following command:

```
python main.py
```

This will start the Flask development server on `http://localhost:5000`.

## Testing

To run the unit tests, use the following command:

```
pytest
```

## Deployment

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.


## Other necessary commands

python -m flask run --reload

docker build -t api:client .

docker run -it --rm -p 8080:80 api:client


## Command to run unit tests

python -m unittest discover tests
