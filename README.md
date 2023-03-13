# interai

![GitHub License](https://img.shields.io/github/license/Chippers255/interai)](https://github.com/Chippers255/interai/blob/main/LICENSE)
[![GitHub Issues](https://img.shields.io/github/issues/Chippers255/interai)](https://github.com/Chippers255/interai/issues)
[![Build Status](https://img.shields.io/github/actions/workflow/status/Chippers255/interai/python-package.yml?branch=main)](https://github.com/Chippers255/interai/actions/workflows/python-package.yml)
[![codecov](https://codecov.io/gh/Chippers255/interai/branch/main/graph/badge.svg?token=H3XAEWR13D)](https://codecov.io/gh/Chippers255/interai)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)

My personal toolset for working with LLMs.

## Development

### Setup
```bash
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip setuptools wheel
pip install .[test]
```

### Tests
```bash
pytest
```