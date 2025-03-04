from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def get_driver():
    """Initializes and returns a Chrome WebDriver instance."""
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Run in headless mode for CI/CD
    options.add_argument("--disable-gpu")
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver
