from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
options = webdriver.ChromeOptions()
options.headless = False
driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 10)
def load_signup_page():
    driver.get("https://air-bnb-project-4quh.onrender.com/signup")
    print("[INFO] SignUp page opened")
    time.sleep(1)
def get_elements():
    name_field = wait.until(EC.presence_of_element_located((By.ID, "name")))
    email_field = wait.until(EC.presence_of_element_located((By.ID, "email")))
    password_field = wait.until(EC.presence_of_element_located((By.ID, "password")))
    signup_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='SignUp']")))
    return name_field, email_field, password_field, signup_btn
def get_toast_message():
    try:
        toast = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "Toastify__toast-body")))
        return toast.text
    except:
        return None
def clear_fields(fields):
    for f in fields:
        f.clear()
load_signup_page()
name_field, email_field, password_field, signup_btn = get_elements()
name_field.send_keys("Aditi Shukla")
email_field.send_keys("shuklaaditi02004@gmail.com")
password_field.send_keys("1234")
signup_btn.click()
toast_msg = get_toast_message()
print(f"[PASS] Valid signup test: {toast_msg}")
time.sleep(2)
negative_tests = [
    {"desc": "Empty Name", "name": "", "email": "test@gmail.com", "password": "1234"},
    {"desc": "Empty Email", "name": "Aditi", "email": "", "password": "1234"},
    {"desc": "Empty Password", "name": "Aditi", "email": "test@gmail.com", "password": ""},
    {"desc": "Invalid Email", "name": "Aditi", "email": "invalidemail", "password": "1234"},
    {"desc": "Short Password", "name": "Aditi", "email": "test@gmail.com", "password": "12"},
]
for test in negative_tests:
    try:
        load_signup_page()
        name_field, email_field, password_field, signup_btn = get_elements()
        clear_fields([name_field, email_field, password_field])
        if test["name"]:
            name_field.send_keys(test["name"])
        if test["email"]:
            email_field.send_keys(test["email"])
        if test["password"]:
            password_field.send_keys(test["password"])
        signup_btn.click()
        toast_msg = get_toast_message()
        print(f"[PASS] {test['desc']} test: {toast_msg}")
        time.sleep(1)
    except Exception as e:
        print(f"[ERROR] {test['desc']} test failed: {e}")
print("[INFO] Browser will stay open for 30 seconds to verify manually...")
time.sleep(30)
driver.quit()
print("[INFO] Browser closed")