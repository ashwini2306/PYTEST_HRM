import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="class")
def setup(request):
    global driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))  # Use ChromeDriverManager for driver management
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()
    request.cls.driver = driver  # Make the driver available for test classes
    yield driver
    driver.quit()
