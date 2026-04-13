# StarProperty QA Automation

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Tests](https://img.shields.io/badge/Tests-PASSED-brightgreen.svg)](run_tests.py)

## 🎯 Project Overview
StarProperty.my QA Automation using **Page Object Model (POM)**, Selenium, Chrome.

**Requirements Met:**
- ✅ PyCharm compatible
- ✅ `python run_tests.py` → TC1 + TC2 fully automated
- ✅ Forms filled, **NOT submitted**
- ✅ Modular code, logging, exception handling

## 🚀 Quick Start

```bash
# 1. Clone & Install
git clone <repo>
cd star_qa_test
pip install -r requirements.txt

# 2. Run Full Suite
python run_tests.py
```

## 📋 Test Cases

### TC1: User Registration Flow
- Generate random data (name, email, phone, DOB>21, etc.)
- Fill form, agent details, upload biz card
- Open T&C/Privacy → **Form ready, NOT submitted**

### TC2: Enquiry & Bookmark Flow
- Login with pre-registered account
- Random To Buy search (Bangi/PJ/Kajang/Bangsar)
- Bookmark first 2 listings
- Verify count=2, compare, enquiry 2nd → **Filled, NOT submitted**

## 🛠 Project Structure
```
.
├── run_tests.py          # Main runner: python run_tests.py
├── pages/                # POM classes
│   ├── base_page.py
│   ├── property_page.py
│   └── registration_page.py
├── tests/                # Test cases
│   ├── test_case_1_registration.py
│   └── test_case_2_enquiry_bookmark.py
├── utils/                # Helpers (logger, random data)
└── requirements.txt      # Dependencies
```

## 🔧 Setup

**Requirements:**
- Python 3.8+
- Chrome browser

**Auto-installs:** ChromeDriver via webdriver_manager

**Credentials:** 
- TC2 uses pre-registered: `ceiwimmessallu-4287@yopmail.com` / `StarProperty526&`
- Update in `tests/test_case_2_enquiry_bookmark.py`

## 🧪 Run Specific Tests

```bash
# TC1 only
python tests/test_case_1_registration.py

# TC2 only  
python tests/test_case_2_enquiry_bookmark.py
```

## 📊 Expected Logs
```
▶ Running Test Case 1: User Registration Flow
✅ TC1 COMPLETE: Form populated. NOT submitted

▶ Running Test Case 2: Enquiry & Bookmark Flow  
✅ Bookmarked listing 1
✅ Verified 2/2 new bookmarks
✅ Compare page confirmed
✅ TC2 COMPLETE: Enquiry filled (not submitted)
```




