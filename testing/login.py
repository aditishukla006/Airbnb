from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = webdriver.ChromeOptions()
options.headless = False
driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 12)

#---------------------------
# STEP 1: Open Home Page
#---------------------------
def load_home():
    driver.get("https://airbnb-puce-three.vercel.app/")
    print("[INFO] Home page opened")
    time.sleep(2)

#---------------------------
# STEP 2: Go to Login
#---------------------------
def go_to_login():
    # Click hamburger menu to show popup
    menu_btn = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(@class,'flex') and contains(@class,'items-center')]"))
    )
    menu_btn.click()
    time.sleep(0.5)
    print("[INFO] Hamburger menu clicked")

    # Wait for popup <ul> to appear
    wait.until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(@class,'absolute')]/ul"))
    )
    print("[INFO] Popup menu appeared")

    # Click Login <li>
    login_btn = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//li[normalize-space(text())='Login']"))
    )
    login_btn.click()
    print("[INFO] Login page opened")
    time.sleep(1)

#---------------------------
# STEP 3: Get Login Elements
#---------------------------
def get_elements():
    email = wait.until(EC.presence_of_element_located((By.ID, "email")))
    password = wait.until(EC.presence_of_element_located((By.ID, "password")))
    btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Login']")))
    return email, password, btn

#---------------------------
# STEP 4: Toast Messages
#---------------------------
def get_toast():
    try:
        toast = wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "Toastify__toast-body"))
        )
        return toast.text
    except:
        return None

#---------------------------
# RUN NEGATIVE TESTS
#---------------------------
negative_tests = [
    {"desc": "Empty Email", "email": "", "password": "1234"},
    {"desc": "Empty Password", "email": "abc@gmail.com", "password": ""},
    {"desc": "Invalid Email", "email": "invalid@gmail.com", "password": "1234"},
    {"desc": "Wrong Password", "email": "shuklaaditi02004@gmail.com", "password": "wrong"},
]

for t in negative_tests:
    load_home()
    go_to_login()
    email, password, btn = get_elements()

    email.clear()
    password.clear()

    if t["email"]:
        email.send_keys(t["email"])
    if t["password"]:
        password.send_keys(t["password"])

    btn.click()
    time.sleep(1)
    print(f"[NEGATIVE TEST] {t['desc']}: {get_toast()}")

#---------------------------
# RUN POSITIVE TEST
#---------------------------
load_home()
go_to_login()
email, password, btn = get_elements()

email.clear()
password.clear()
email.send_keys("shuklaaditi02004@gmail.com")
password.send_keys("1234")
btn.click()
time.sleep(3)
print("[POSITIVE TEST] Valid login tested")

time.sleep(5)
driver.quit()
