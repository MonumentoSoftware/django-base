# Django Base Monumento [![build](https://github.com/MonumentoSoftware/django-base/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/MonumentoSoftware/django-base/actions/workflows/main.yml) 

A clean and simple Django project template.
Used as a base for Monumento Software OilDjangoPro

- [Django Base ](#django-base-)
- [Install](#install)
- [Usage](#usage)
  - [Database seed](#database-seed)
  - [Documentação da API](#documentação-da-api)
    - [Interface gráfica](#interface-gráfica)
    - [Incrementando a documentação](#incrementando-a-documentação)
  - [Unit Testing](#unit-testing)
    - [Test Coverage](#test-coverage)
  - [Architecture](#architecture)
  - [Useful Commands](#useful-commands)
    - [Create an app](#create-an-app)
    - [Enter a container](#enter-a-container)
    - [Open the Django shell](#open-the-django-shell)
    - [Reset the database](#reset-the-database)
    - [Update translations from English](#update-translations-from-english)

# Install 

Basic installation:
```bash
make setup_install
```
You can also create a virtual environment:

```bash
make setup_venv
```
# Usage
To start the project, run the following command:
```bash
make up
```
## Database seed

Seed the database:
```bash
make seed
```

## Documentação da API

### Interface gráfica

We use Swagger UI to document the API. To access it, follow the steps:

1. Run the project with `make up`.
2. Access `http://localhost:8000/swagger/`.

### Incrementando a documentação

The file *docs/openapi.json* describes the API using the OpenAPI specification. It must be manually edited over the project's lifetime to keep the documentation in compliance with the API. A tool that can speed up this process is the *generateschema* command from Django REST Framework. It can be used to generate the project's automatic documentation based on the existing views. However, care must be taken not to overwrite the original *openapi.json* file. To use the tool, follow the tutorial:

1. Run the command `make generate_schema` to create the file **docs/temp-schema.json**.
2. Identify the desired part in the generated file (e.g., some new *view*) and move it to **docs/openapi.json**.
3. Delete the file **docs/temp-schema.json**.

## Unit Testing

We use the **pytest** library to run unit tests. Its configuration file is *pytest.ini*.

- To run the tests, use the command `make test`.

Since tests reuse the generated database by default, if there are new migrations, it is necessary to recreate the database.

- To recreate the database, use the command `pytest --create-db`.

### Test Coverage

- `make coverage`

or

- `make coverage_html`, for an HTML report.

## Architecture

- `apps`: here should be all the local Django apps that should be created throughout the project's development. In the base project, this folder will only contain the `user` app (and the `tenant`, if it is a tenant-based project). To create a new app, use the *make startapp* command at the project's root to create it in the correct place and following the base project's template.
- `conf`: module containing the project's configuration files.
    - `app_template`: template used for creating new apps. Generally, it should not be altered.
    - `settings`: folder with Django settings files. It is modularized to have a settings file for each environment: local, production, etc.
    - `urls.py`: project's URL file. It is preferable to only include the URLs of other apps, leaving the specific configuration of each module in its own urls.py file.
    - `wsgi.py`: standard Django WSGI file for deployment.
- `docs`: module containing files related to the project's documentation.
    - `openapi.json`: file containing the REST API schema. It is used in the *swagger-ui* container.
- `lib`: module containing classes that should be shared throughout the project, such as a base model, a generic view, etc.
    - `models.py`: contains base models for the project that automatically include timestamp fields (created_at or updated_at) or safe delete feature.
- `requirements`: contains the project's dependencies, separated by environment (local, production, etc.).
- `scripts`: contains useful shell scripts for the project.
- `env.example`: example env file to start the project. It should be copied to a `.env` file (not versioned).
- `docker-compose.yml` and `Dockerfile`: Docker configuration files.
- `Makefile`: contains useful commands, such as entering a container or creating an app.

## Useful Commands

### Create an app

`make startapp [app_name]`

### Enter a container

`make enter [service_name]`

### Open the Django shell

`make shell`

### Reset the database

`make reset_schema`

### Update translations from English

`make compilemessages`
