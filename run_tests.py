"""
====================================================
  STAR MEDIA GROUP — QA Practical Test
  Main Runner: python run_tests.py
====================================================
  Test Case 1: User Registration Flow
  Test Case 2: Enquiry & Bookmark Flow
====================================================
"""

import sys
import os

# Ensure project root is in path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from utils.helpers import setup_logger
from tests.test_case_1_registration import run_test_case_1
from tests.test_case_2_enquiry_bookmark import run_test_case_2

logger = setup_logger()


def main():
    logger.info("🚀 Starting Star QA Automation Test Suite")
    logger.info("=" * 60)

    results = {}

    # ── Test Case 1 ───────────────────────────────────────
    try:
        logger.info("▶ Running Test Case 1: User Registration Flow")
        run_test_case_1()
        results["TC1"] = "✅ PASSED"
    except Exception as e:
        results["TC1"] = f"❌ FAILED — {e}"
        logger.error(f"TC1 encountered an error: {e}")

    # ── Test Case 2 ───────────────────────────────────────
    try:
        logger.info("▶ Running Test Case 2: Enquiry & Bookmark Flow")
        run_test_case_2()
        results["TC2"] = "✅ PASSED"
    except Exception as e:
        results["TC2"] = f"❌ FAILED — {e}"
        logger.error(f"TC2 encountered an error: {e}")

    # ── Summary ───────────────────────────────────────────
    logger.info("")
    logger.info("=" * 60)
    logger.info("  TEST SUITE SUMMARY")
    logger.info("=" * 60)
    for tc, result in results.items():
        logger.info(f"  {tc}: {result}")
    logger.info("=" * 60)


if __name__ == "__main__":
    main()
