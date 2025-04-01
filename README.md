# Regression Testing Tool

## Overview
Automated regression testing using **Selenium, PyTest, and Allure Reports**.

## Features
- Web UI automation
- Test execution & reporting
- Parallel execution
- CI/CD integration

## Installation
```bash
pip install selenium pytest webdriver-manager
```

## Run Tests
```bash
pytest --html=report.html
```

## CI/CD Setup (GitHub Actions)
```yaml
name: Regression Tests
on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Install dependencies
        run: pip install selenium pytest webdriver-manager
      - name: Run tests
        run: pytest --html=report.html
