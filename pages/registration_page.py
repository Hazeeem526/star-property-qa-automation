import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage
from utils.helpers import setup_logger

logger = setup_logger()

class RegistrationPage(BasePage):
    """Page Object for starproperty.my registration flow"""

    # ── URLs ──────────────────────────────────────────────
    BASE_URL        = "https://www.starproperty.my/"
    REGISTER_URL    = "https://connect.starproperty.my/auth/register"

    # ── Navigation ────────────────────────────────────────
    LOGIN_BTN       = (By.XPATH, "//a[contains(@href,'login')]")
    CREATE_ACCOUNT  = (By.XPATH, "//a[contains(@href,'register')]")

    # ── Registration Form Fields ──────────────────────────
    EMAIL           = (By.ID, "email")
    PASSWORD        = (By.ID, "password")
    CONFIRM_PASS    = (By.ID, "password_confirmation")
    FIRST_NAME      = (By.ID, "name")
    LAST_NAME       = (By.ID, "last_name")
    PHONE           = (By.ID, "mobile_no")
    DOB             = (By.ID, "date_of_birth")

    # ── Property Agent checkbox ───────────────────────────
    AGENT_CHECKBOX  = (By.ID, "category")

    # ── Agent-specific fields ─────────────────────────────
    AGENCY_ECODE    = (By.ID, "ecode")
    REN_CODE_FIELD  = (By.ID, "ren_code")
    UPLOAD_BIZCARD  = (By.ID, "business_card")

    # ── Newsletter checkbox ───────────────────────────────
    NEWSLETTER_CB   = (By.ID, "newsletter")

    # ── Register button ───────────────────────────────────
    REGISTER_BTN    = (By.ID, "submit-btn")

    # ── T&C / Privacy Policy ─────────────────────────────
    TNC_LINK        = (By.XPATH, "//a[@href='https://www.starproperty.my/terms-and-condition']")
    PRIVACY_LINK    = (By.XPATH, "//a[@href='https://www.starproperty.my/privacy']")

    # ─────────────────────────────────────────────────────
    def navigate_to_register(self):
        logger.info("=== Navigating to Registration Page ===")
        self.open(self.BASE_URL)
        time.sleep(2)

        # Try direct URL first as fallback
        try:
            self.click(*self.LOGIN_BTN)
            time.sleep(1)
            self.click(*self.CREATE_ACCOUNT)
        except Exception:
            logger.info("Direct navigation fallback to register URL")
            self.open(self.REGISTER_URL)

        time.sleep(2)
        logger.info(f"Current URL: {self.driver.current_url}")

    def fill_basic_info(self, first_name, last_name, email, phone, password, dob):
        logger.info("=== Filling Basic Registration Info ===")
        self.type_slowly(*self.EMAIL, email)
        self.type_slowly(*self.PASSWORD, password)
        self.type_slowly(*self.CONFIRM_PASS, password)
        self.type_slowly(*self.FIRST_NAME, first_name)
        self.type_slowly(*self.LAST_NAME, last_name)
        self.type_slowly(*self.PHONE, phone)

        # DOB uses a datepicker (readonly), use JS to set value
        try:
            self.driver.execute_script(
                "document.getElementById('date_of_birth').removeAttribute('readonly');"
            )
            self.type_text(*self.DOB, dob)
            logger.info(f"DOB set to: {dob}")
        except Exception as e:
            logger.warning(f"DOB field issue: {e}")

    def select_property_agent(self):
        logger.info("=== Selecting Property Agent checkbox ===")
        try:
            checkbox = self.driver.find_element(*self.AGENT_CHECKBOX)
            if not checkbox.is_selected():
                checkbox.click()
            logger.info("Property Agent checkbox selected")
        except Exception as e:
            logger.warning(f"Agent checkbox not found: {e}")

    def fill_agent_details(self, agency_ecode, ren_code):
        logger.info(f"=== Filling Agent Details: {agency_ecode}, {ren_code} ===")
        try:
            # Scroll to agent section first
            self.scroll_to_element(*self.AGENCY_ECODE)
            self.type_text(*self.AGENCY_ECODE, agency_ecode)
            self.type_text(*self.REN_CODE_FIELD, ren_code)
        except Exception as e:
            logger.warning(f"Agent detail fields not found: {e}")

    def upload_business_card(self, image_path):
        logger.info(f"=== Uploading Business Card: {image_path} ===")
        try:
            upload_input = self.driver.find_element(*self.UPLOAD_BIZCARD)
            upload_input.send_keys(image_path)
            logger.info("Business card uploaded successfully")
            time.sleep(1)
        except Exception as e:
            logger.warning(f"Upload field not found: {e}")

    def uncheck_newsletter(self):
        logger.info("=== Unchecking Newsletter ===")
        try:
            checkbox = self.driver.find_element(*self.NEWSLETTER_CB)
            if checkbox.is_selected():
                checkbox.click()
                logger.info("Newsletter unchecked")
            else:
                logger.info("Newsletter already unchecked")
        except Exception as e:
            logger.warning(f"Newsletter checkbox not found: {e}")

    def open_tnc_and_privacy(self):
        logger.info("=== Opening T&C and Privacy Policy ===")
        original_handles = self.get_all_window_handles()

        # Click T&C
        try:
            self.click(*self.TNC_LINK)
            time.sleep(2)
            logger.info("T&C link clicked")
        except Exception as e:
            logger.warning(f"T&C link not found: {e}")

        # Click Privacy Policy
        try:
            self.click(*self.PRIVACY_LINK)
            time.sleep(2)
            logger.info("Privacy Policy link clicked")
        except Exception as e:
            logger.warning(f"Privacy Policy link not found: {e}")

        # Close Privacy Policy tab (last opened), keep T&C open
        all_handles = self.get_all_window_handles()
        if len(all_handles) > len(original_handles) + 1:
            # More than 1 new tab was opened
            privacy_handle = all_handles[-1]
            self.driver.switch_to.window(privacy_handle)
            logger.info("Closing Privacy Policy tab")
            self.driver.close()

        # Switch back to original/registration tab
        self.driver.switch_to.window(all_handles[0])
        logger.info("Returned to Registration page")
        time.sleep(1)
