from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = webdriver.ChromeOptions()
options.headless = False
driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 10)

# -----------------------------
# Step 1: Open Home Page
# -----------------------------
def load_home():
    driver.get("https://airbnb-puce-three.vercel.app/")
    print("[INFO] Home page opened")
    time.sleep(1)

# -----------------------------
# Step 2: Navigate to Login Page
# -----------------------------
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

# -----------------------------
# Step 3: Click SignUp Link on Login Page
# -----------------------------
def go_to_signup():
    signup_link = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//span[normalize-space(text())='SignUp']"))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", signup_link)
    signup_link.click()
    print("[INFO] Signup page opened via login link")
    time.sleep(1)



# -----------------------------
# Step 4: Get Signup Elements
# -----------------------------
def get_elements():
    name_field = wait.until(EC.presence_of_element_located((By.ID, "name")))
    email_field = wait.until(EC.presence_of_element_located((By.ID, "email")))
    password_field = wait.until(EC.presence_of_element_located((By.ID, "password")))
    signup_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='SignUp']")))
    return name_field, email_field, password_field, signup_btn

# -----------------------------
# Step 5: Toast Messages
# -----------------------------
def get_toast_message():
    try:
        toast = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "Toastify__toast-body")))
        return toast.text
    except:
        return None

def clear_fields(fields):
    for f in fields:
        f.clear()

# -----------------------------
# Step 6: Negative Tests First
# -----------------------------
negative_tests = [
    {"desc": "Empty Name", "name": "", "email": "test@gmail.com", "password": "1234"},
    {"desc": "Empty Email", "name": "Aditi", "email": "", "password": "1234"},
    {"desc": "Empty Password", "name": "Aditi", "email": "test@gmail.com", "password": ""},
    {"desc": "Invalid Email", "name": "Aditi", "email": "invalidemail", "password": "1234"},
    {"desc": "Short Password", "name": "Aditi", "email": "test@gmail.com", "password": "12"},
]

for test in negative_tests:
    try:
        load_home()
        go_to_login()
        go_to_signup()
        name_field, email_field, password_field, signup_btn = get_elements()
        clear_fields([name_field, email_field, password_field])

        if test["name"]:
            name_field.send_keys(test["name"])
        if test["email"]:
            email_field.send_keys(test["email"])
        if test["password"]:
            password_field.send_keys(test["password"])

        signup_btn.click()
        time.sleep(1)
        toast_msg = get_toast_message()
        print(f"[NEGATIVE TEST] {test['desc']}: {toast_msg}")

    except Exception as e:
        print(f"[ERROR] {test['desc']} test failed: {e}")

# -----------------------------
# Step 7: Positive Test
# -----------------------------
try:
    load_home()
    go_to_login()
    go_to_signup()
    name_field, email_field, password_field, signup_btn = get_elements()
    clear_fields([name_field, email_field, password_field])

    # Enter valid signup info
    name_field.send_keys("xyz")
    email_field.send_keys("xyz@gmail.com")
    password_field.send_keys("1234")

    signup_btn.click()
    time.sleep(1)
    toast_msg = get_toast_message()
    print(f"[POSITIVE TEST] Valid signup: {toast_msg}")

except Exception as e:
    print(f"[ERROR] Positive signup test failed: {e}")

# -----------------------------
# Step 8: Keep Browser Open for Manual Verification
# -----------------------------
print("[INFO] Browser will stay open for 10 seconds to verify manually...")
time.sleep(2)
driver.quit()
print("[INFO] Browser closed")
