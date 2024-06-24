# Simple Flask Project

This project demonstrates how to set up a simple flask project with 3 endpoints that serve data and one cli command.

## Prerequisites

Before you begin, ensure you have the following installed:

- [Python 3.12+](https://www.python.org/downloads/)
- [Poetry](https://python-poetry.org/docs/#installation)
- make

## Setup

**1. Clone the repository:**

```sh
git clone git@github.com:Georg1703/fask_simple_project.git
cd fask_simple_project
```

**2. Start the project:**

```sh
make start_server
```

At this moment service is up and running, you can visit:

* http://localhost:8000/experience
* http://localhost:8000/personal
* http://localhost:8000/education

**3. Run the tests:**

```sh
make test
```

**4. Run cli command to see same info in the cli:**

```sh
make cli_info
```
