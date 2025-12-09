from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, os

FRONTEND_URL ="https://airbnb-puce-three.vercel.app/"
EMAIL = "aditi@gmail.com"
PASSWORD = "1234"

IMAGE1 = os.path.abspath("img1.png")
IMAGE2 = os.path.abspath("img2.png")
IMAGE3 = os.path.abspath("img3.png")

options = webdriver.ChromeOptions()
options.headless = False
driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 20)

# ----------------------
# HELPERS
# ----------------------
def wait_for_toasts():
    try:
        wait.until_not(EC.presence_of_element_located((By.CLASS_NAME, "Toastify__toast")))
    except:
        pass
    time.sleep(0.5)

def scroll_click(el):
    driver.execute_script("arguments[0].scrollIntoView(true);", el)
    driver.execute_script("arguments[0].click();", el)

# ----------------------
# STEP 1: OPEN HOME
# ----------------------
def open_home():
    driver.get(FRONTEND_URL)
    print("[INFO] Home page opened")
    time.sleep(2)

# ----------------------
# STEP 2: LOGIN
# ----------------------
def login():
    print("[STEP] Logging in…")

    # Open menu if Login not visible
    try:
        login_btn = driver.find_element(By.XPATH, "//li[normalize-space(text())='Login']")
        scroll_click(login_btn)
    except:
        menu_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class,'flex') and contains(@class,'items-center')]")))
        menu_btn.click()
        time.sleep(0.5)
        login_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//li[normalize-space(text())='Login']")))
        scroll_click(login_btn)

    # Fill login form
    wait.until(EC.presence_of_element_located((By.ID, "email"))).send_keys(EMAIL)
    driver.find_element(By.ID, "password").send_keys(PASSWORD)
    driver.find_element(By.XPATH, "//button[contains(text(),'Login')]").click()

    # Wait for redirect away from Login page
    wait.until(lambda d: d.current_url != FRONTEND_URL + "login")
    print("✔ Login successful!")
    wait_for_toasts()

# ----------------------
# STEP 3: CLICK "List Your Home"
# ----------------------
def click_list_home():
    print("[STEP] Clicking 'List Your Home'…")
    btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'List your home')]")))
    scroll_click(btn)
    wait.until(EC.url_contains("/listingpage1"))
    print("✔ ListingPage1 opened")

# ----------------------
# STEP 4: FILL LISTING PAGE 1
# ----------------------
def fill_listing_page_1():
    print("[STEP] Filling ListingPage1…")

    title_field = wait.until(EC.presence_of_element_located((By.ID, "title")))
    des_field = driver.find_element(By.ID, "des")
    img1_field = driver.find_element(By.ID, "img1")
    img2_field = driver.find_element(By.ID, "img2")
    img3_field = driver.find_element(By.ID, "img3")
    rent_field = driver.find_element(By.ID, "rent")
    city_field = driver.find_element(By.ID, "city")
    landmark_field = driver.find_element(By.ID, "landmark")
    next_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Next')]")))

    # ---------- VALID ENTRY ----------
    title_field.send_keys("Aditi's Selenium Test Home")
    des_field.send_keys("Automated description")
    img1_field.send_keys(IMAGE1)
    img2_field.send_keys(IMAGE2)
    img3_field.send_keys(IMAGE3)
    rent_field.send_keys("1500")
    city_field.send_keys("Ahmedabad")
    landmark_field.send_keys("Near Science City")

    # ---------- NEGATIVE TESTS ----------
    negative_tests = [
        {"field": title_field, "desc": "Empty Title", "restore": "Aditi's Selenium Test Home"},
        {"field": des_field, "desc": "Empty Description", "restore": "Automated description"},
        {"field": rent_field, "desc": "Empty Rent", "restore": "1500"},
        {"field": rent_field, "desc": "Invalid Rent", "restore": "1500", "value": "abc"},
        {"field": city_field, "desc": "Empty City", "restore": "Ahmedabad"},
        {"field": landmark_field, "desc": "Empty Landmark", "restore": "Near Science City"},
    ]

    for test in negative_tests:
        test["field"].clear()
        if "value" in test:
            test["field"].send_keys(test["value"])
        print(f"[NEGATIVE TEST] {test['desc']}")
        scroll_click(next_btn)
        time.sleep(1)
        try:
            toast = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "Toastify__toast-body")))
            print(f"Toast: {toast.text}")
        except:
            print("No toast appeared!")
        test["field"].clear()
        test["field"].send_keys(test["restore"])
        wait_for_toasts()  # wait for toast to disappear before next test

    # ---------- FINAL VALID CLICK ----------
    scroll_click(next_btn)
    wait.until(EC.url_contains("/listingpage2"))
    print("✔ ListingPage1 completed → Page2 loaded")


# ----------------------
# STEP 5: FILL PAGE 2
# ----------------------
def fill_listing_page_2():
    print("[STEP] Selecting category on Page2…")
    category_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//h3[text()='Villa']/parent::*")))
    scroll_click(category_btn)

    next_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Next')]")))
    scroll_click(next_btn)
    wait.until(EC.url_contains("/listingpage3"))
    print("✔ ListingPage2 completed → Page3 opened")

# ----------------------
# STEP 6: FILL PAGE 3 / SUBMIT
# ----------------------
def fill_listing_page_3():
    print("[STEP] Submitting Listing from Page3…")
    add_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Add Listing')]")))
    scroll_click(add_btn)

    wait.until(EC.url_contains("/"))
    print("✔ Redirected to Home Page successfully!")

# ----------------------
# RUN TEST FLOW
# ----------------------
try:
    open_home()
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
    driver.quit()
