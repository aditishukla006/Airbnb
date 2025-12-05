from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

FRONTEND_URL = "http://localhost:5173/login"
EMAIL = "aditi@gmail.com"
PASSWORD = "1234"

options = webdriver.ChromeOptions()
options.headless = False
driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 20)
##search baki,listing page bki

def login():
    print("[STEP] Login process starting...")
    driver.get(FRONTEND_URL)
    time.sleep(2)

    inputs = driver.find_elements(By.TAG_NAME, "input")
    email_input = inputs[0]
    pass_input = inputs[1]

    email_input.clear()
    email_input.send_keys(EMAIL)
    pass_input.clear()
    pass_input.send_keys(PASSWORD)

    login_button = driver.find_element(By.XPATH, "//button[contains(text(),'Login')]")
    login_button.click()

    wait.until(lambda d: d.current_url != FRONTEND_URL)
    print("✔ Login successful")


def wait_for_toasts_and_loaders():
    print("[STEP] Waiting for toasts/loaders to disappear...")

    try:
        # Wait for toast
        wait.until_not(EC.presence_of_element_located(
            (By.CLASS_NAME, "Toastify__toast")
        ))
    except:
        pass

    try:
        # Wait for backdrop/UI overlays
        wait.until_not(EC.presence_of_element_located(
            (By.XPATH, "//*[contains(@class,'backdrop') or contains(@class,'overlay')]")
        ))
    except:
        pass

    time.sleep(1)


def click_list_home():
    print("[STEP] Clicking 'List your home'...")

    wait_for_toasts_and_loaders()

    list_home_btn = wait.until(EC.presence_of_element_located(
        (By.XPATH, "//span[contains(text(),'List your home')]")
    ))

    # Try normal click first
    try:
        list_home_btn.click()
    except:
        print("⚠ Normal click failed — using JS force click")
        driver.execute_script("arguments[0].click();", list_home_btn)

    print("✔ Clicked successfully, waiting for navigation...")

    wait.until(EC.url_contains("/listingpage1"))
    print("🎉 Navigated to Listing Page")


# ================= RUN ==================
try:
    login()
    click_list_home()
except Exception as e:
    print("❌ TEST FAILED:", e)
finally:
    time.sleep(3)
    driver.quit()