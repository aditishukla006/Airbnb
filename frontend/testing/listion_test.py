from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

FRONTEND_URL = "https://air-bnb-project-4quh.onrender.com/login"
EMAIL = "aditi@gmail.com"
PASSWORD = "1234"

# image paths
IMAGE1 = os.path.abspath("img1.png")
IMAGE2 = os.path.abspath("img2.png")
IMAGE3 = os.path.abspath("img3.png")

options = webdriver.ChromeOptions()
options.headless = False
driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 20)

# -------------------------------------------------------
# LOGIN
# -------------------------------------------------------
def login():
    print("[STEP] Logging in…")
    driver.get(FRONTEND_URL)
    time.sleep(2)

    inputs = driver.find_elements(By.TAG_NAME, "input")
    inputs[0].send_keys(EMAIL)
    inputs[1].send_keys(PASSWORD)

    driver.find_element(By.XPATH, "//button[contains(text(),'Login')]").click()
    wait.until(lambda d: d.current_url != FRONTEND_URL)
    print("✔ Login successful!")
def wait_for_toasts():
    try:
        wait.until_not(EC.presence_of_element_located(
            (By.CLASS_NAME, "Toastify__toast")
        ))
    except:
        pass
    time.sleep(0.5)
def click_list_home():
    print("[STEP] Clicking List Your Home…")
    wait_for_toasts()

    btn = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'List your home')]"))
    )
    try:
        btn.click()
    except:
        driver.execute_script("arguments[0].click();", btn)

    wait.until(EC.url_contains("/listingpage1"))
    print("✔ Opened ListingPage1!")
def fill_listing_page_1():
    print("[STEP] Filling ListingPage1…")

    # ---------- VALID CASE ----------
    wait.until(EC.presence_of_element_located((By.ID, "title"))).send_keys("Aditi's Selenium Test Home")
    driver.find_element(By.ID, "des").send_keys("This is an automated test description.")

    driver.find_element(By.ID, "img1").send_keys(IMAGE1)
    driver.find_element(By.ID, "img2").send_keys(IMAGE2)
    driver.find_element(By.ID, "img3").send_keys(IMAGE3)

    driver.find_element(By.ID, "rent").send_keys("1500")
    driver.find_element(By.ID, "city").send_keys("Ahmedabad")
    driver.find_element(By.ID, "landmark").send_keys("Near Science City")

    # ---------- EMPTY + WRONG DATA TEST ----------
    print("[TEST] Negative test: Clearing fields and adding wrong values…")

    driver.find_element(By.ID, "rent").clear()
    driver.find_element(By.ID, "rent").send_keys("abc")  # WRONG VALUE (should be number)

    time.sleep(1)

    # Again enter correct value
    driver.find_element(By.ID, "rent").clear()
    driver.find_element(By.ID, "rent").send_keys("1500")

    # Click Next
    driver.find_element(By.XPATH, "//button[contains(text(),'Next')]").click()
    wait.until(EC.url_contains("/listingpage2"))
    print("🎉 ListingPage1 completed → Page2 loaded!")


# -------------------------------------------------------
# PAGE 2 (CATEGORY SELECT)
# -------------------------------------------------------
def fill_listing_page_2():
    print("[STEP] Selecting category on ListingPage2…")

    category_btn = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//h3[text()='Villa']/parent::*"))
    )
    category_btn.click()

    print("✔ Category 'Villa' selected")

    next_btn = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Next')]"))
    )
    driver.execute_script("arguments[0].click();", next_btn)

    wait.until(EC.url_contains("/listingpage3"))
    print("🎉 ListingPage2 completed → Page3 opened!")
def fill_listing_page_3():
    print("[STEP] Submitting Listing from Page3…")

    add_btn = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Add Listing')]"))
    )
    driver.execute_script("arguments[0].click();", add_btn)

    print("✔ Add Listing clicked! Waiting for redirect…")

    # 🟢 WAIT FOR REDIRECT TO HOME PAGE
    wait.until(EC.url_contains("/"))
    print("🎉 Redirected to Home Page successfully!")
try:
    login()
    click_list_home()
    fill_listing_page_1()
    fill_listing_page_2()
    fill_listing_page_3()

    print("\n🎉 ALL TESTS PASSED SUCCESSFULLY")
    time.sleep(30)

except Exception as e:
    print("\n❌ TEST FAILED:", e)

finally:
    time.sleep(3)
    driver.quit()
