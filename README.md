# UI Course Automation Tests

This project implements automated tests for the [UI Course Test Application](https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login). The tests are written using **Python**, **Pytest**, **Allure** and **Playwright**. The test application's source code is available on [GitHub](https://github.com/Nikita-Filonov/qa-automation-engineer-ui-course).

## Project Overview

The goal of this project is to automate the testing of the UI Course application. The automated tests verify various functionalities of the application including authentication, course management, and dashboard features to ensure its stability and correctness. The project structure follows best practices for organizing test code with clear, maintainable scripts using the Page Object Model pattern.

## Technologies Used

- **Python 3.12+** - Programming language
- **Pytest** - Testing framework
- **Playwright** - Browser automation library
- **Allure** - Test reporting framework
- **Pydantic** - Data validation and settings management
- **UI Coverage Tool** - Test coverage tracking for UI elements

## Project Structure

```
autotests-ui/
├── pages/                  # Page Object Model classes
├── tests/                  # Test files organized by functionality
│   ├── authentication/     # Authentication tests
│   ├── courses/           # Course management tests
│   └── dashboard/         # Dashboard tests
├── fixtures/              # Pytest fixtures
├── components/            # Reusable UI components
├── elements/              # UI elements and coverage tracking
├── templates/             # Test data templates
├── testdata/              # Test data files
├── tools/                 # Utility tools and helpers
├── videos/                # Test execution videos
├── tracing/               # Playwright traces
├── allure-results/        # Allure test results
└── allure-report/         # Generated Allure reports
```

## Features

- **Multi-browser support**: Chromium, Firefox, WebKit
- **Parallel test execution** with pytest-xdist
- **Rich test reporting** with Allure
- **Video recording** of test failures
- **Playwright tracing** for debugging
- **UI Coverage tracking** to monitor tested elements
- **Automated test reruns** on failures
- **GitHub Actions CI/CD** integration

## Test Categories

The tests are organized with the following markers:
- `regression` - Full regression test suite
- `smoke` - Quick smoke tests
- `critical` - Critical functionality tests
- `authorization` - Authentication and authorization tests
- `courses` - Course management tests
- `dashboard` - Dashboard page tests
- `ui` - UI-specific tests

## Getting Started

### Prerequisites

- Python 3.12 or higher
- Git

### Clone the Repository

To get started, clone the project repository using Git:

```bash
git clone https://github.com/l-SK-l/autotests-ui.git
cd autotests-ui
```

### Create a Virtual Environment

It's recommended to use a virtual environment to manage project dependencies. Follow the instructions for your operating system:

#### Linux / MacOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

#### Windows

```bash
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### Install Dependencies

Once the virtual environment is activated, install the project dependencies listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

### Additional Playwright Setup

Install the required browsers for Playwright:

```bash
playwright install
```

## Running Tests

### Run All Tests

To run all tests with default settings:

```bash
pytest
```

### Run Tests by Category

Run specific test categories using markers:

```bash
# Run only smoke tests
pytest -m smoke

# Run regression tests
pytest -m regression

# Run authentication tests
pytest -m authorization

# Run course-related tests
pytest -m courses
```

### Run Tests in Parallel

For faster execution, run tests in parallel:

```bash
pytest -n auto  # Auto-detect number of CPUs
pytest -n 4     # Use 4 parallel workers
```

### Run Tests with Video Recording

```bash
pytest --video=on
```

### Run Tests with Tracing

```bash
pytest --tracing=on
```

## Viewing Test Reports

### Allure Reports

After running tests, generate and view the Allure report:

```bash
allure serve allure-results
```

This command will open the Allure report in your default web browser with detailed test results, screenshots, videos, and traces.

You can also view example reports from this project published on GitHub Pages: [https://l-sk-l.github.io/autotests-ui/40/](https://l-sk-l.github.io/autotests-ui/40/)

### UI Coverage Reports

View UI coverage reports to see which UI elements have been tested:

```bash
# Coverage reports are generated in coverage-report.json
# View the coverage history in coverage-history.json
```

## Configuration

The project uses environment-based configuration. Create a `.env` file in the root directory to customize settings:

```env
APP_URL=https://nikita-filonov.github.io/qa-automation-engineer-ui-course
HEADLESS=true
BROWSERS=["chromium", "firefox", "webkit"]
TEST_USER.EMAIL=test@example.com
TEST_USER.USERNAME=testuser
TEST_USER.PASSWORD=password123
```

## GitHub Actions CI/CD

The project includes GitHub Actions workflow that:
- Runs tests on every push and pull request to main branch
- Executes tests in parallel across multiple browsers
- Generates and publishes Allure reports
- Tracks UI coverage metrics

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the ISC License.
