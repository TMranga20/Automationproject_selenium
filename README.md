# 🚀 Selenium Automation Framework – Python | Pytest | POM | DDT

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Selenium](https://img.shields.io/badge/Selenium-WebDriver-green)
![Pytest](https://img.shields.io/badge/Pytest-Framework-orange)
![POM](https://img.shields.io/badge/Design-Page%20Object%20Model-purple)
![DDT](https://img.shields.io/badge/Data%20Driven-CSV-yellow)
![Status](https://img.shields.io/badge/Build-Passing-brightgreen)
![Git](https://img.shields.io/badge/Git-Version%20Control-orange?logo=git)
![GitHub](https://img.shields.io/badge/GitHub-Repository-black?logo=github)

---

## 📌 Project Overview

This project is a **Selenium Automation Testing Framework** developed using **Python and Pytest** implementing the **Page Object Model (POM)** design pattern and **Data Driven Testing (DDT)**.

The framework automates core functionalities of the website:  
🔗 https://automationexercise.com

It is designed with scalability, reusability, and maintainability following **industry best practices**.

---

## ✨ Key Features

✔ Selenium WebDriver with Python  
✔ Pytest Test Framework  
✔ Page Object Model (POM)  
✔ Data Driven Testing using CSV  
✔ Regression Test Suite  
✔ Product & Cart Module Automation  
✔ Implicit & Explicit Waits  
✔ Screenshot capture for failed tests  
✔ HTML Test Reports  
✔ Modular and Scalable Framework  

---

## 🛠️ Tech Stack

- **Language:** Python  
- **Automation Tool:** Selenium WebDriver  
- **Test Framework:** Pytest  
- **Design Pattern:** Page Object Model (POM)  
- **Data Driven:** CSV + Pytest Parametrize  
- **IDE:** VS Code  
- **Version Control:** Git & GitHub  

---

## 📂 Project Structure

```
Automationproject_selenium/
│
├── tests/
│   ├── test_home.py
│   ├── test_login.py
│   ├── test_login_ddt.py
│   ├── test_products.py
│   ├── test_cart.py
│   ├── test_regression.py
│
├── pages/
│   ├── base_page.py
│   ├── home_page.py
│   ├── login_page.py
│   ├── products_page.py
│   ├── cart_page.py
│
├── utilities/
│   ├── driver_setup.py
│   ├── read_csv.py
│
├── test_data/
│   ├── login_data.csv
│
├── screenshots/
│
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

---

## ▶️ How to Run the Project

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/<your-username>/Automationproject_selenium.git
cd Automationproject_selenium
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run All Test Cases

```bash
pytest -v
```

### 4️⃣ Run Specific Test Suites

Run regression suite:

```bash
pytest -m regression -v
```

Run product tests:

```bash
pytest -m products -v
```

Run cart tests:

```bash
pytest -m cart -v
```

Run data-driven tests:

```bash
pytest -m ddt -v
```

---

## 📊 Generate HTML Report

```bash
pytest --html=report.html
```

After execution, open:

```
report.html
```

to view detailed test results.

---

## 🧪 Test Coverage

🔹 Home Page Validation  
🔹 Login Functionality  
🔹 Data Driven Login Tests  
🔹 Product Page Automation  
🔹 Add to Cart Flow  
🔹 Cart Validation  
🔹 End-to-End Regression Suite  

Total: **30+ Automated Test Cases**

---

## 📸 Screenshot on Failure

The framework automatically captures screenshots for failed test cases and stores them in:

```
screenshots/
```

---

## 🧠 Framework Highlights

- Reusable page classes using POM  
- Pytest fixtures for driver setup and teardown  
- CSV-based test data management  
- Modular test execution using Pytest markers  
- Clean separation of test logic and locators  

---

## 🚀 Future Enhancements

- Allure Reporting  
- Jenkins CI/CD Integration  
- Parallel Test Execution (pytest-xdist)  
- Headless Browser Execution  
- Excel-based Data Driven Testing  

---

## 👨‍💻 Author

**Talari Mohana Ranga**  
QA Automation Engineer (Fresher)  
🔗 GitHub: https://github.com/<your-username>  

---

## ⭐ If you found this project useful, please give it a star!
