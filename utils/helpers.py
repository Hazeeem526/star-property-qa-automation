import random
import string
import logging
from datetime import datetime

# ─────────────────────────────────────────
#  Logger Setup
# ─────────────────────────────────────────
def setup_logger(name="StarQA"):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            "[%(asctime)s] %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger

logger = setup_logger()


# ─────────────────────────────────────────
#  Random Data Generators
# ─────────────────────────────────────────
def generate_random_phone():
    """Generate a random MY mobile number e.g. +60112345678"""
    prefix = random.choice(["+6011", "+6012", "+6013", "+6014", "+6016", "+6017", "+6018", "+6019"])
    suffix = "".join(random.choices(string.digits, k=7))
    phone = f"{prefix}{suffix}"
    logger.info(f"Generated phone: {phone}")
    return phone

def generate_random_email():
    """Generate a random email address"""
    username = "testuser_" + "".join(random.choices(string.ascii_lowercase + string.digits, k=6))
    email = f"{username}@mailtest.com"
    logger.info(f"Generated email: {email}")
    return email

def generate_random_name():
    """Generate a random full name"""
    first_names = ["Ahmad", "Nurul", "Muhammad", "Siti", "Hazim", "Farah", "Amir", "Lina"]
    last_names = ["Bin Ali", "Binti Omar", "Bin Hassan", "Binti Yusof", "Bin Zain"]
    name = f"{random.choice(first_names)} {random.choice(last_names)}"
    logger.info(f"Generated name: {name}")
    return name

def generate_dob_above_21():
    """Return a DOB string for a user aged 21+, format DD/MM/YYYY"""
    year = random.randint(1980, 2003)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    dob = f"{day:02d}/{month:02d}/{year}"
    logger.info(f"Generated DOB: {dob}")
    return dob

def generate_ren_code():
    """Generate a dummy REN code"""
    return "E" + "".join(random.choices(string.digits, k=5))

def generate_agency_ecode():
    """Generate a dummy Agency E-code"""
    return "AGC" + "".join(random.choices(string.digits, k=4))

def generate_password():
    """Generate a valid password"""
    return "Test@" + "".join(random.choices(string.digits, k=4))
