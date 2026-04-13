import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pages.registration_page import RegistrationPage
from utils.helpers import (
    setup_logger,
    generate_random_name,
    generate_random_email,
    generate_random_phone,
    generate_dob_above_21,
    generate_agency_ecode,
    generate_ren_code,
    generate_password
)

logger = setup_logger()

def run_test_case_1():
    logger.info("=" * 60)
    logger.info("  TEST CASE 1: User Registration Flow")
    logger.info("=" * 60)

    # ── Setup Driver ──────────────────────────────────────
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")
    # options.add_argument("--headless")  # Uncomment to run headless

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    try:
        page = RegistrationPage(driver)

        # ── Step 1: Navigate to Registration ─────────────
        page.navigate_to_register()

        # ── Step 2: Generate Test Data ────────────────────
        full_name = generate_random_name()
        first_name, last_name = full_name.split(" ", 1)
        email    = generate_random_email()
        phone    = generate_random_phone()
        password = generate_password()
        dob      = generate_dob_above_21()
        ecode    = generate_agency_ecode()
        ren      = generate_ren_code()

        logger.info(f"Test Data → Name: {full_name} | Email: {email} | Phone: {phone}")

        # ── Step 3: Fill Basic Info ───────────────────────
        page.fill_basic_info(first_name, last_name, email, phone, password, dob)

        # ── Step 4: Uncheck Newsletter ────────────────────
        page.uncheck_newsletter()

        # ── Step 5: Select Property Agent ────────────────
        page.select_property_agent()
        time.sleep(1)

        # ── Step 6: Fill Agent Details ────────────────────
        page.fill_agent_details(ecode, ren)

        # ── Step 7: Upload Business Card ──────────────────
        bizcard_path = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..", "assets", "dummy_business_card.jpg")
        )
        page.upload_business_card(bizcard_path)

        # ── Step 8: Open T&C and Privacy Policy ──────────
        page.open_tnc_and_privacy()

        # ── Outcome: Form populated, NOT submitted ────────
        logger.info("=" * 60)
        logger.info("✅ TC1 COMPLETE: Form populated. NOT submitted as required.")
        logger.info("=" * 60)

        time.sleep(3)  # Brief pause so tester can visually verify

    except Exception as e:
        logger.error(f"❌ TC1 FAILED: {e}")
        raise

    finally:
        driver.quit()
        logger.info("Browser closed.")
