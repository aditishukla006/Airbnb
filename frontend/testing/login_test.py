from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
options = webdriver.ChromeOptions()
options.headless = False
driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 10)
def load_login_page():
    driver.get("https://airbnb-8nr7.onrender.com/login")
    print("[INFO] Login page opened")
    time.sleep(1) 
def get_elements():
    email_field = wait.until(EC.presence_of_element_located((By.ID, "email")))
    password_field = wait.until(EC.presence_of_element_located((By.ID, "password")))
    login_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Login']")))
    return email_field, password_field, login_btn
def get_toast_message():
    try:
        toast = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "Toastify__toast-body")))
        return toast.text
    except:
        return None
def clear_fields(email_field, password_field):
    email_field.clear()
    password_field.clear()
load_login_page()
email_field, password_field, login_btn = get_elements()
email_field.send_keys("shuklaaditi02004@gmail.com")
password_field.send_keys("1234")
login_btn.click()
wait.until(lambda driver: "/" in driver.current_url.lower() or driver.find_elements(By.ID, "dashboard"))
print(f"[PASS] Login success with valid credentials. Current URL: {driver.current_url}")
time.sleep(2)
negative_tests = [
    {"desc": "Empty Email", "email": "", "password": "1234"},
    {"desc": "Empty Password", "email": "shuklaaditi02004@gmail.com", "password": ""},
    {"desc": "Invalid Email", "email": "invalid@gmail.com", "password": "1234"},
    {"desc": "Incorrect Password", "email": "shuklaaditi02004@gmail.com", "password": "wrongpass"},
    {"desc": "Both Fields Empty", "email": "", "password": ""}
]
for test in negative_tests:
    try:
        load_login_page()
        email_field, password_field, login_btn = get_elements()
        clear_fields(email_field, password_field)
        if test["email"]:
            email_field.send_keys(test["email"])
        if test["password"]:
            password_field.send_keys(test["password"])
        login_btn.click()
        toast_msg = get_toast_message()
        print(f"[PASS] {test['desc']} test: {toast_msg}")
        time.sleep(1)
    except Exception as e:
        print(f"[ERROR] {test['desc']} test failed: {e}")
print("[INFO] Browser will stay open for 30 seconds to verify manually...")
time.sleep(30)

driver.quit()
print("[INFO] Browser closed")

