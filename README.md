# logging-extended-handlers

|     |     |
| --- | --- |
| Version | [![PyPI - Version](https://img.shields.io/pypi/v/logging-extended-handlers.svg)](https://pypi.org/project/logging-extended-handlers) [![PyPI - Python Version](https://img.shields.io/pypi/pyversions/logging-extended-handlers.svg)](https://pypi.org/project/logging-extended-handlers) |
| Project | ![GitHub License](https://img.shields.io/github/license/m-birke/logging-extended-handlers) ![PyPI - Status](https://img.shields.io/pypi/status/logging-extended-handlers) ![PyPI - Format](https://img.shields.io/pypi/format/logging-extended-handlers) ![PyPI - Implementation](https://img.shields.io/pypi/implementation/logging-extended-handlers) |
| CI | ![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/m-birke/logging-extended-handlers/static-code-check.yml) |
| Code | ![PyPI - Types](https://img.shields.io/pypi/types/logging-extended-handlers) [![Checked with mypy](https://www.mypy-lang.org/static/mypy_badge.svg)](https://mypy-lang.org/) [![Linting: Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black) |

-----

Extending logging.handlers

## Table of Contents

- [About](#about)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## About

This package contains the following loggers:

- `HTTPHandlerCustomHeader`: Like `logging.handlers.HTTPHandler` but with full freedom of the HTTP header
- `BufferingSMTPHandler`: Buffers the logs like `logging.handlers.BufferingHandler` and sends it via smtp

Similar projects with differen handlers:

- [logging-nice-handlers](https://pypi.org/project/logging-nice-handlers/)
- [external-logging-handlers](https://pypi.org/project/external-logging-handlers/)
- [aws-logging-handlers](https://pypi.org/project/aws-logging-handlers/)
- []()

## Installation

```console
pip install logging-extended-handlers
```

## Usage

```python
logger = logging.getLogger()
logger.setLevel("DEBUG")
my_logger = MyLogger(...)
my_logger.setLevel("INFO")
my_formatter = logging.Formatter(
    fmt="%(asctime)s %(levelname)s by %(funcName)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    style="%",
)
my_logger.setFormatter(my_formatter)
logger.addHandler(my_logger)
```

## License

`logging-extended-handlers` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
