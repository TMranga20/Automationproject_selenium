# QA Automation Fresher Profile

Hi, I am **Talari Mohana Ranga**, a QA Automation fresher.
This project shows my hands-on practice with Selenium, Python, and Pytest using Page Object Model (POM).

![Top Language](https://img.shields.io/github/languages/top/TMranga20/Automationproject_selenium)
![Repo Size](https://img.shields.io/github/repo-size/TMranga20/Automationproject_selenium)
![Stars](https://img.shields.io/github/stars/TMranga20/Automationproject_selenium?style=social)
![Last Commit](https://img.shields.io/github/last-commit/TMranga20/Automationproject_selenium)
![Issues](https://img.shields.io/github/issues/TMranga20/Automationproject_selenium)

## Career Objective

To start my career as a QA Automation Engineer and contribute to building reliable, high-quality web applications through effective test automation.

## About This Project

This is an automation test framework for `https://automationexercise.com`.
It covers important user flows like login, signup, product checks, cart flow, and regression scenarios.

## 🧰 Tech Stack

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?logo=python&logoColor=white)
![Selenium](https://img.shields.io/badge/Selenium-WebDriver-43B02A?logo=selenium&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-Test%20Runner-000000?logo=pytest&logoColor=white)
![POM](https://img.shields.io/badge/Pattern-Page_Object_Model-0B5394)
![Git](https://img.shields.io/badge/Git-GitHub-181717?logo=git&logoColor=white)
![VS Code](https://img.shields.io/badge/IDE-VS%20Code-007ACC?logo=visual-studio-code&logoColor=white)

Built with: Python • Selenium WebDriver • Pytest • Page Object Model (POM) • Git & GitHub • VS Code

## ✨ Key Highlights

- Structured test framework with reusable page classes
- Separate `tests/`, `pages/`, and `utils/` folders
- Screenshot capture for failed tests
- HTML report support using `pytest-html`

## 🗂 Project Structure

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

## ▶️ How To Run (Windows PowerShell)

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

## 📬 Contact

- Name: Talari Mohana Ranga
- Role: QA Automation Fresher
- LinkedIn: https://www.linkedin.com/in/talarimohana/
- Email: mohanranga7290@gmal.com


## 🔭 Roadmap / Next improvements (suggested)

- Add GitHub Actions CI workflow to run tests on push / PR (matrix: Python versions, browsers)
- Add test reporting (pytest-html and/or Allure)
- Add browser driver management (webdriver-manager) and Dockerized test runner
- Add sample test data and more example test cases in `tests/`

## Note

- If `pytest` command is not recognized, use `python -m pytest`.
- In VS Code, select interpreter: `.\\venv\\Scripts\\python.exe`.
