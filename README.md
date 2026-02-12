# QA Automation Fresher Profile

Hi, I am **Talari Mohana Ranga**, a QA Automation fresher.
This project shows my hands-on practice with Selenium, Python, and Pytest using Page Object Model (POM).

## Career Objective

To start my career as a QA Automation Engineer and contribute to building reliable, high-quality web applications through effective test automation.

## About This Project

This is an automation test framework for `https://automationexercise.com`.
It covers important user flows like login, signup, product checks, cart flow, and regression scenarios.

## Skills Used

- Python
- Selenium WebDriver
- Pytest
- Page Object Model (POM)
- Git and GitHub
- VS Code

## Key Highlights

- Structured test framework with reusable page classes
- Separate `tests/`, `pages/`, and `utils/` folders
- Screenshot capture for failed tests
- HTML report support using `pytest-html`

## Project Structure

```text
Automationproject_selenium/
|-- tests/
|-- pages/
|-- utils/
|-- screenshots/
|-- reports/
|-- conftest.py
|-- pytest.ini
|-- requirements.txt
```

## How To Run (Windows PowerShell)

1. Create virtual environment:

```powershell
python -m venv venv
```

2. Activate virtual environment:

```powershell
.\venv\Scripts\Activate.ps1
```

3. Install dependencies:

```powershell
python -m pip install -r requirements.txt
```

4. Run all tests:

```powershell
python -m pytest -v
```

5. Run regression tests:

```powershell
python -m pytest -m regression -v
```

6. Generate HTML report:

```powershell
python -m pytest --html=reports/report.html
```

## Contact

- Name: Talari Mohana Ranga
- Role: QA Automation Fresher
- LinkedIn: https://www.linkedin.com/in/talarimohana/
- Email: mohanranga7290@gmal.com

## Note

- If `pytest` command is not recognized, use `python -m pytest`.
- In VS Code, select interpreter: `.\\venv\\Scripts\\python.exe`.
