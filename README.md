# SMS Bombing Using Python Selenium
Automated Login Script Using Selenium

This Python script automates the process of logging into various websites using a mobile number for SMS-based login. The script simulates login attempts on multiple e-commerce and service websites by entering a mobile number into the login forms and submitting them.

The script uses Selenium WebDriver with Microsoft Edge to interact with the web pages, automatically filling in the login fields for websites such as Flipkart, Amazon, Boat, Udemy, Dominos, KFC, OYO, Naukri, Spotify, and AngelOne. Each login attempt is executed in a loop, allowing for multiple interactions in a single run.

# Features:
- Multiple Website Automation: Automates login attempts on several popular websites by interacting with their login forms.
- Mobile Number Login: Uses a mobile number (stored as a variable no) for login attempts.
- Simulated Form Submissions: Uses Selenium to locate and fill out the login fields, then submit the form.
- Error Handling: The script continues running even if an error occurs during one of the login attempts.

# Requirements:
- Python 3.x
- Selenium
- Microsoft Edge WebDriver

# Setup:
- pip install selenium
