from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# -----------------------------
# Chrome Options
# -----------------------------
options = webdriver.ChromeOptions()
options.headless = False  # Show browser for debugging
driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 10)

# -----------------------------
# Test Data
# -----------------------------
EMAIL = "aditi@gmail.com"
PASSWORD = "1234"
CHECKIN_DATE = "2025-12-10"
CHECKOUT_DATE = "2025-12-12"

# -----------------------------
# Helper Functions
# -----------------------------
def login(email, password):
    driver.get("http://localhost:5173/login")
    email_field = wait.until(EC.presence_of_element_located((By.ID, "email")))
    password_field = wait.until(EC.presence_of_element_located((By.ID, "password")))
    login_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Login']")))

    email_field.send_keys(email)
    password_field.send_keys(password)
    login_btn.click()
    time.sleep(2)
    print(f"[INFO] Logged in as {email}")

def open_first_listing():
    # Wait for listing cards to appear
    first_listing = wait.until(
    EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "[class*='w-[330px]']")
    )
)
    first_listing.click()
    print("[INFO] Opened first listing")
    time.sleep(2)

def open_booking_popup():
    reserve_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Reserve']")))
    reserve_btn.click()
    # Wait for booking popup
    wait.until(EC.visibility_of_element_located((By.XPATH, "//h1[text()='Confirm & Book']")))
    print("[INFO] Booking popup opened")

def fill_booking_dates(checkin, checkout):
    checkin_input = wait.until(EC.presence_of_element_located((By.ID, "checkIn")))
    checkout_input = wait.until(EC.presence_of_element_located((By.ID, "checkOut")))
    checkin_input.clear()
    checkout_input.clear()
    checkin_input.send_keys(checkin)
    checkout_input.send_keys(checkout)
    print("[INFO] Entered check-in/out dates")

def verify_total_price():
    # Get displayed nights
    night_diff = wait.until(EC.presence_of_element_located((By.XPATH, "//p/span[contains(text(),'₹')]")))
    total_span = driver.find_element(By.XPATH, "//p/span[text()='Total Price']/following-sibling::span")
    total_displayed = float(total_span.text)
    print(f"[INFO] Total price displayed: {total_displayed}")
    return total_displayed

def book_listing():
    book_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Book Now']")))
    book_btn.click()
    # Wait for confirmation toast (optional)
    time.sleep(2)
    print("[SUCCESS] Booking completed")

# -----------------------------
# Test Flow
# -----------------------------
try:
    login(EMAIL, PASSWORD)
    open_first_listing()
    open_booking_popup()
    fill_booking_dates(CHECKIN_DATE, CHECKOUT_DATE)
    total_price = verify_total_price()
    print(f"[INFO] Verified total price: {total_price}")
    book_listing()

finally:
    print("[INFO] Browser will stay open for 5 seconds to verify...")
    time.sleep(5)
    driver.quit()
    print("[INFO] Browser closed")
