import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import sys
import os
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

from pages.property_page import PropertyPage
from utils.helpers import (
    setup_logger,
    generate_random_name,
    generate_random_email,
    generate_random_phone
)

logger = setup_logger()

# ──────────────────────────────────────────────────────────────
#  PRE-REGISTERED GENERAL USER CREDENTIALS
#  Replace these with a real registered account before running!
# ──────────────────────────────────────────────────────────────
TEST_EMAIL    = "ceiwimmessallu-4287@yopmail.com"
TEST_PASSWORD = "StarProperty526&"


import pytest

@pytest.mark.smoke
@pytest.mark.tc2
@pytest.mark.enquiry
def test_case_2_enquiry_bookmark():
    run_test_case_2 = locals()['run_test_case_2']  # Access function
    logger.info("=" * 60)
    logger.info("  TEST CASE 2: Enquiry & Bookmark Flow")
    logger.info("=" * 60)

    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    try:
        page = PropertyPage(driver)

        # ── Step 1: Login ──────────────────────────────────
        page.login(TEST_EMAIL, TEST_PASSWORD)

        # ── Step 2: Search To Buy random ─────────────────────
        page.search_to_buy()

        # ── Step 3: Capture first 2 listings ──────────────
        listings = page.capture_first_two_listings()
        print("\n📋 CAPTURED LISTINGS:")
        for item in listings:
            print(f"  [{item['index']}] Price: {item['price']} | Location: {item['location']}")

        # ── Step 4: Bookmark first 2 ──────────────────────
        page.bookmark_first_two()

        # ── Step 5: Verify bookmark count = 2 ─────────────
        page.verify_bookmark_count(expected=2)

        # ── Step 6: Compare bookmarked properties ──────────
        page.compare_bookmarked()

        # ── Step 7: Fill enquiry form for 2nd record ───────
        name  = generate_random_name()
        email = generate_random_email()
        phone = generate_random_phone()
        page.fill_enquiry_form_second_record(name, email, phone)

        # ── Step 8: Logout ─────────────────────────────────
        page.logout()

        logger.info("=" * 60)
        logger.info("✅ TC2 COMPLETE: Bookmarked, compared, enquiry filled (not submitted), logged out.")
        logger.info("=" * 60)

        time.sleep(2)

    except Exception as e:
        logger.error(f"❌ TC2 FAILED at URL: {driver.current_url}")
        logger.error(f"❌ Error: {e}")
        raise

    finally:
        driver.quit()
        logger.info("Browser closed.")
