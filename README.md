# Lookup CLI Repository

## Overview

🚀 **Lookup CLI** is a command-line tool designed to search and retrieve data from a YAML file. It is packaged with Docker support and includes GitHub Actions workflows for automated testing and linting. This repository provides a robust solution for managing YAML-based lookups with high code quality enforced by `pylint` and unit tests.
The **Lookup CLI** is a command-line tool designed to search and retrieve data from a YAML file. It is packaged with Docker support and includes GitHub Actions workflows for automated testing and linting. This repository provides a robust solution for managing YAML-based lookups with high code quality enforced by `pylint` and unit tests.

---

## File Structure

```
lookup-cli-main/
    .gitignore
    Dockerfile
    README.md
    __init__.py
    docker-compose.yml
    lookup_cli.py
    requirements.txt
    .github/
        workflows/
            py_ut_check.yml
            pylint_check.yml
    data/
        people.yaml
    tests/
        __init__.py
        test_lookup_cli.py
```

### Key Files and Directories

- **`lookup_cli.py`**: The main CLI script.
- **`data/people.yaml`**: Example YAML file used for lookups.
- **`tests/`**: Contains unit tests for the CLI tool.
- **`.github/workflows/`**: GitHub Actions workflows for automated testing and linting.
- **`docker-compose.yml`**: Configuration file for running the CLI tool with Docker Compose.
- **`requirements.txt`**: Python dependencies for the project.
- **`Dockerfile`**: Docker image configuration.

---

## Getting Started

### Prerequisites

🔧 **Required Tools**:

- Python 3.11+
- Docker and Docker Compose
- Git

### Installation

1. Clone the repository:

   ```bash
   git clone <repository_url>
   cd lookup-cli-main
   ```
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

### Running Locally

💻 **Local Usage**:

1. Set the `YAML_FILE_PATH` environment variable:

   ```bash
   export YAML_FILE_PATH=./data/people.yaml
   ```
2. Run the CLI tool:

   ```bash
   python lookup_cli.py <name> [<output_field>]
   ```

   Example:

   ```bash
   python lookup_cli.py Alice age
   ```

### Running with Docker

🐳 **Docker Usage**:

1. Build the Docker image:

   ```bash
   docker build -t lookup-cli .
   ```
2. Run the CLI tool:

   ```bash
   docker run -e YAML_FILE_PATH=/app/data/people.yaml -v $(pwd)/data:/app/data lookup-cli Alice age
   ```

### Running with Docker Compose

1. Start the container:

   ```bash
   docker-compose up
   ```
2. Use the CLI tool interactively:

   ```bash
   $ docker exec -it <container_name> bash
   ```

   In container:
   ```bash
   $ lookup-cli Alice age
   ```

---

## Testing

### Unit Tests

🧪 **Run Tests**:

Run the tests with:

```bash
python -m unittest discover -s tests
```

### Linting

Run `pylint` to check the code quality:

```bash
pylint lookup_cli.py
```

---

## GitHub Actions Workflows

- **`pylint_check.yml`**: Runs `pylint` on pull requests.
- **`py_ut_check.yml`**: Executes unit tests on pull requests.

These workflows enforce high code quality and maintain reliable functionality.

---

## Contributing

1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature/new-feature
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add new feature"
   ```
4. Push to the branch:
   ```bash
   git push origin feature/new-feature
   ```
5. Open a pull request.

---
