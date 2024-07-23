# Bruteforce

**Bruteforce** is a Python-based tool designed for performing brute-force attacks on website login pages. This repository includes a script that automates the process of testing login forms with a list of usernames and passwords to identify potential security vulnerabilities. It leverages Selenium to interact with web elements and simulate user actions.

## 🔍 Features

- **Automated Brute-Force Attacks:** Test login forms by attempting multiple username and password combinations.
- **Customizable Inputs:** Configure the script to target specific login fields and adjust attack parameters.
- **Detailed Logging:** Output results for each login attempt, including successes and failures.
- **URL Verification:** Check for changes in the URL to determine if a login attempt was successful based on a specific success indicator.

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- `pip` (Python package installer)
- Google Chrome browser (or another supported browser with corresponding WebDriver)

### Webdriver Installation for Linux_based_systems


1. **Run the following Lines One by One:**

    ```sh
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome-stable_current_amd64.deb
sudo apt-get install -f  # Install dependencies

# Install ChromeDriver
CHROME_DRIVER_VERSION=`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`
wget https://chromedriver.storage.googleapis.com/$CHROME_DRIVER_VERSION/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
sudo mv chromedriver /usr/local/bin/

    ```

    
### Installation for windows

Make sure you installed the web-browser with its corresponding webdriver .

If you did not know how to do that search it on youtube .

1. **Clone the repository:**

    ```sh
    git clone https://github.com/GreyHatsonawane/Bruteforce.git
    ```

2. **Navigate to the project directory:**

    ```sh
    cd Bruteforce_Any_Website
    ```

3. **Install the required dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

4. **(Optional) Configure the script** with the target website URL, field XPaths, and paths to username and password files.

### Usage

1. **Run the script:**

    ```sh
    python bruteforce.py
    ```

2. **Follow the prompts** to enter the target website URL, XPaths of login fields, paths to the username and password files, and a success indicator.

    ```plaintext
    Enter the Target Website Url: http://example.com/login
    Enter the xpath of username field: //input[@name='username']
    Enter the xpath of password field: //input[@name='password']
    Enter the xpath of login/submit button field: //button[@type='submit']
    Enter path of username file: usernames.txt
    Enter path of the password file: passwords.txt
    Enter a word which comes in successful login Url: dashboard
    ```

   *Follow the instructions after running the code.*

## ⚠️ Disclaimer

This tool is intended for educational and ethical hacking purposes only. Unauthorized use of this tool against systems without explicit permission is illegal and unethical. The author is not responsible for any misuse or damage caused by this tool.

## 🤝 Contributing

Contributions are welcome! If you have improvements, bug fixes, or new features, please submit a pull request. Ensure that your code follows the project's coding standards and includes appropriate documentation.

## 📝 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## ✨ Author

**GreyHatsonawane**
