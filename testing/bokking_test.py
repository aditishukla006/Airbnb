from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# -----------------------
# CONFIG
# -----------------------
options = webdriver.ChromeOptions()
options.headless = False  
driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 15)  # slightly longer wait

EMAIL = "shuklaaditi02004@gmail.com"
PASSWORD = "1234"
CHECKIN_DATE = "2025-12-10"
CHECKOUT_DATE = "2025-12-12"
FRONTEND_URL = "https://airbnb-puce-three.vercel.app/"

# -----------------------
# HELPERS
# -----------------------
def open_home():
    driver.get(FRONTEND_URL)
    print("[INFO] Home page opened")
    time.sleep(2)

def login(email, password):
    driver.get(FRONTEND_URL)
    time.sleep(2)

    # Try to find "Login" button in navbar or menu
    try:
        login_btn = driver.find_element(By.XPATH, "//li[normalize-space(text())='Login']")
        driver.execute_script("arguments[0].click();", login_btn)
        print("[INFO] Navigated to Login page")
    except:
        # If Login button not visible, try menu
        menu_btn = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(@class,'flex') and contains(@class,'items-center')]")
        ))
        menu_btn.click()
        time.sleep(0.5)
        login_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//li[normalize-space(text())='Login']")))
        driver.execute_script("arguments[0].click();", login_btn)
        print("[INFO] Opened Login page via menu")

    # Fill login form
    email_input = wait.until(EC.presence_of_element_located((By.ID, "email")))
    password_input = wait.until(EC.presence_of_element_located((By.ID, "password")))
    email_input.send_keys(email)
    password_input.send_keys(password)
    driver.find_element(By.XPATH, "//button[text()='Login']").click()

    # Wait until URL changes or login success indicator
    wait.until(lambda d: d.current_url != FRONTEND_URL)
    print(f"[INFO] Logged in as {email}")


def open_first_listing():
    first_listing = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "[class*='w-[330px]']"))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", first_listing)
    driver.execute_script("arguments[0].click();", first_listing)
    print("[INFO] Opened first listing")
    time.sleep(2)

def open_booking_popup():
    reserve_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Reserve']")))
    reserve_btn.click()   
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
    total_span = wait.until(
        EC.presence_of_element_located((By.XPATH, "//p/span[text()='Total Price']/following-sibling::span"))
    )
    total_displayed = float(total_span.text.replace("₹","").replace(",",""))
    print(f"[INFO] Total price displayed: {total_displayed}")
    return total_displayed

def book_listing():
    book_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Book Now']")))
    driver.execute_script("arguments[0].scrollIntoView(true);", book_btn)
    driver.execute_script("arguments[0].click();", book_btn)
    time.sleep(2)
    print("[SUCCESS] Booking completed")

# -----------------------
# TEST FLOW
# -----------------------
try:
    open_home()
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
