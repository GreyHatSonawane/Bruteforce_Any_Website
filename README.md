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

### Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/GreyHatsonawane/Bruteforce.git
    ```

2. **Navigate to the project directory:**

    ```sh
    cd Bruteforce
    ```

3. **Install the required dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

### Installing ChromeDriver for Linux-based Systems

1. **Download ChromeDriver:**

    Visit the [ChromeDriver download page](https://sites.google.com/chromium.org/driver/downloads) and download the version that matches your installed Chrome version.

2. **Extract the downloaded file:**

    ```sh
    unzip chromedriver_linux64.zip
    ```

3. **Move the ChromeDriver to a directory included in your system's PATH:**

    ```sh
    sudo mv chromedriver /usr/local/bin/
    ```

4. **Verify the installation:**

    ```sh
    chromedriver --version
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
