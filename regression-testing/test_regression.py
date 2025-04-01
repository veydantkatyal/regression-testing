import pytest
from selenium.webdriver.common.by import By
from webdriver_setup import get_driver

@pytest.fixture
def setup():
    """Fixture to initialize and quit the driver."""
    driver = get_driver()
    driver.get("https://demo.opencart.com/")
    yield driver
    driver.quit()

def test_valid_login(setup):
    """Test case to verify login functionality."""
    driver = setup
    driver.find_element(By.LINK_TEXT, "My Account").click()
    driver.find_element(By.LINK_TEXT, "Login").click()
    driver.find_element(By.ID, "input-email").send_keys("test@example.com")
    driver.find_element(By.ID, "input-password").send_keys("password")
    driver.find_element(By.XPATH, "//input[@value='Login']").click()
    
    # Verify if login is successful
    assert "My Account" in driver.title

def test_search_functionality(setup):
    """Test case to verify search functionality."""
    driver = setup
    search_box = driver.find_element(By.NAME, "search")
    search_box.send_keys("Laptop")
    search_box.submit()
    
    # Verify if search results appear
    assert "Search" in driver.title
