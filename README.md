# Selenium Python Test Automation Framework

## Setup Instructions

1. **Install Python** in your local machine
2. **Create virtual environment** so that any libraries or changes will be specific in the venv environment not global.
   - `python -m venv venv`
   - `.\venv\Scripts\activate`
3. **Install needed packages** for Selenium Python
   - `pip install -r requirements.txt`
4. **Get latest chromedriver**. Make sure the chromedriver is compatible with your local chrome (https://googlechromelabs.github.io/chrome-for-testing/#stable)

## Project Structure

```
AssessmentSeleniumPython/
│
├── 📄 config.yaml                    # Configuration file (URLs, paths, etc.)
├── 📄 requirements.txt               # Python dependencies
├── 📄 README.md                      # Project documentation
│
├── 🚗 drivers/
│   └── chromedriver.exe              # Chrome WebDriver executable
│
├── 🧪 tests/
│   ├── AssessmentTest.py             # Main test file (unittest)
│   └── resources/
│       └── testdata.xlsx             # Test data (Excel file)
│
├── 📊 reports/
│   └── unittest_report.html          # HTML test reports (pytest-html)
│
├── ⚙️ utils/
│   ├── browser.py                    # WebDriver initialization
│   ├── config.py                     # YAML config reader
│   ├── testdataprovider.py           # Excel data reader
│   └── wait_utils.py                 # Explicit wait utilities
│
├── 🎭 actions/
│   ├── Common.py                     # Common actions (open page, popup handling)
│   ├── SwagLoginPageActions.py       # Login page specific actions
│   └── ProductPageActions.py         # Product page specific actions
│
├── 📄 pages/
│   ├── LoginPage/
│   │   ├── SwagLoginPage.py          # Login page object
│   │   └── locators/
│   │       └── SwagLoginPageLocators.py  # Login page element locators
│   └── ProductPage/
│       ├── ProductPage.py            # Product page object
│       └── locators/
│           └── ProductPageLocators.py     # Product page element locators
│
└── 🐍 venv/ & .venv/                 # Python virtual environments
```

## Hierarchy of Classes

```
Test Class (test/AssessmentTest.py)
    ↓ (Test execution and WebDriver management)
Actions Class (actions/SwagLoginPageActions.py) / Common Class
    ↓ (Handles browser actions and business logic)
Page Object (pages/SwagLoginPage.py)
    ↓ (Handles page interactions)
Locators (pages/locators/SwagLoginPageLocators.py)
    (Handles elements locators)
```

## Utility Classes

- **browser.py** - WebDriver setup
- **config.py** - Configuration management
- **testdataprovider.py** - Test data management
- **wait_utils.py** - Explicit wait utilities for waiting on elements

### Using wait_utils.py

The `wait_utils` class provides static methods for explicit waits using Selenium's WebDriverWait. **Always ensure the timeout argument is an integer (default is 10 seconds).**

**Example usage:**

```python
from utils.wait_utils import wait_utils
from selenium.webdriver.common.by import By

# Wait for a single element to be present
wait_utils.wait_for_element(driver, By.CLASS_NAME, "login_logo")

# Wait for all elements matching a locator
wait_utils.wait_for_all_elements(driver, By.CLASS_NAME, "cart_item")

# Wait for an element to be visible using a function that returns a WebElement
wait_utils.wait_for_element_displayed(driver, lambda: driver.find_element(By.ID, "finish"))
```

## Configuration

- **config.yaml** - Centralized configuration
- **testdata.xlsx** - Test data storage

## How to Run

```bash
# Using pytest with HTML report
python -m pytest -s tests/AssessmentTest.py --html=reports/report.html

# Using unittest
python -m unittest tests/AssessmentTest.py
```

## Test Scenarios

### 1. Validate Login Page and Error
- **Unsuccessful Login**
    - Check the username is required error
    - Password is required error
    - Error both in username and password

### 2. Validate User Purchase in Product Page
- **Successful Login**
    - Add to Cart
    - Remove Items to Cart
    - Checkout
- **Successful Logout**

