flipkart-test-suite/
├── .github/
│   └── workflows/
│       └── test.yml
├── tests/
│   └── test_homepage.py
├── requirements.txt
└── README.md

# File: requirements.txt
selenium
pytest

# File: tests/test_homepage.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def test_flipkart_title():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(options=options)
    driver.get("https://www.flipkart.com")

    assert "Flipkart" in driver.title
    driver.quit()


# File: .github/workflows/test.yml
name: Run Flipkart Selenium Tests

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout code
      uses: actions/checkout@v3

    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: 3.10

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt

    - name: Install Chrome & Chromedriver
      run: |
        sudo apt-get update
        sudo apt-get install -y wget unzip xvfb
        wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
        sudo apt install -y ./google-chrome-stable_current_amd64.deb
        sudo ln -s /usr/bin/google-chrome /usr/bin/chrome
        wget -O /tmp/chromedriver.zip https://chromedriver.storage.googleapis.com/$(curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE)/chromedriver_linux64.zip
        unzip /tmp/chromedriver.zip -d /tmp/
        sudo mv /tmp/chromedriver /usr/local/bin/chromedriver
        sudo chmod +x /usr/local/bin/chromedriver

    - name: Run Selenium tests
      run: |
        pytest tests/


# File: README.md
# Flipkart UI Automation Test Suite

This project contains UI automation tests for Flipkart using Python, Selenium, and GitHub Actions.

## ✅ Features
- Headless Chrome tests
- GitHub Actions CI
- Basic homepage title check

## 🚀 Getting Started

### Prerequisites:
- Python 3.10+
- Chrome and Chromedriver

### Installation:
```bash
pip install -r requirements.txt
```

### Run Tests:
```bash
pytest tests/
```

### CI/CD:
- Tests run automatically on push to `main` branch via GitHub Actions
