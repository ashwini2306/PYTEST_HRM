import pytest
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


# Use the fixture defined in conftest.py
@pytest.mark.usefixtures("setup")
class TestMyInfo:
    # Locators as before
    username = (By.NAME, "username")
    password = (By.NAME, "password")
    login_button = (By.CSS_SELECTOR, ".oxd-button")
    my_info = (By.LINK_TEXT, "My Info")
    personal = (By.LINK_TEXT, "Personal Details")
    first_name = (By.NAME, "firstName")
    gender = (By.XPATH, "(//*[@class = 'oxd-radio-input oxd-radio-input--active --label-right oxd-radio-input'])[2]")
    save = (By.XPATH, "//*[@type = 'submit']")
    contact = (By.LINK_TEXT, "Contact Details")
    address = (By.XPATH, "(//*[@class = 'oxd-input oxd-input--active'])[2]")
    location = (By.XPATH, "(//*[@class = 'oxd-input oxd-input--active'])[4]")
    emergency = (By.LINK_TEXT, "Emergency Contacts")
    add1 = (By.XPATH, "//button[@class='oxd-button oxd-button--medium oxd-button--text']")
    name = (By.XPATH, "(//input)[2]")
    relationship = (By.XPATH, "(//input[@class = 'oxd-input oxd-input--active oxd-input--error'])[1]")
    phone = (By.XPATH, "(//*[@modelmodifiers='[object Object]'])[2]")
    save1 = (By.XPATH, "//button[@type='submit']")
    dependent = (By.LINK_TEXT, "Dependents")
    add2 = (By.XPATH, "(//*[@class = 'oxd-button oxd-button--medium oxd-button--text'])")
    name1 = (By.XPATH, "(//*[@class = 'oxd-input oxd-input--active'])[2]")
    save2 = (By.XPATH, "//button[@type='submit']")
    immigration = (By.LINK_TEXT, "Immigration")
    add3 = (By.XPATH, "//*[@class='oxd-button oxd-button--medium oxd-button--text'][1]")
    passport = (By.XPATH, "//label[normalize-space()='Passport']")
    number = (By.XPATH, "(//*[@class = 'oxd-input oxd-input--active'])[2]")
    issue_date = (By.XPATH, "(//*[@placeholder='yyyy-dd-mm'])[1]")
    expiry_date = (By.XPATH, "(//*[@placeholder='yyyy-dd-mm'])[2]")
    save3 = (By.XPATH, "//*[@type='submit']")
    qualification = (By.LINK_TEXT, "Qualifications")
    add4 = (By.XPATH, "(//button[@class='oxd-button oxd-button--medium oxd-button--text'])[1]")
    company = (By.XPATH, "(//*[@class='oxd-input oxd-input--focus'])")
    job_title = (By.XPATH, "(//*[@class='oxd-input oxd-input--active oxd-input--error'])[2]")
    save4 = (By.XPATH, "//*[@type='submit']")
    membership = (By.LINK_TEXT, "Memberships")
    add5 = (By.XPATH, "(//button[@type='button'][normalize-space()='Add'])[1]")
    member = (By.XPATH, "(//div[@class='oxd-select-text-input'][normalize-space()='-- Select --'])[1]")

    def test_personal_info(self):
        driver = self.driver
        # Login
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(self.username)).send_keys("Admin")
        time.sleep(4)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(self.password)).send_keys("admin123")
        time.sleep(4)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(self.login_button)).click()
        time.sleep(4)

        # Personal Info
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(self.my_info)).click()
        time.sleep(4)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(self.personal)).click()
        time.sleep(4)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(self.first_name)).send_keys("John")
        time.sleep(4)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(self.gender)).click()
        time.sleep(4)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(self.save)).click()
        time.sleep(4)

    def test_contact_details(self):
        driver = self.driver
        # Contact Details
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(self.contact)).click()
        time.sleep(4)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(self.address)).send_keys("Nehru nagar")
        time.sleep(4)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(self.location)).send_keys("coimbatore")
        time.sleep(4)

    # def test_emergency_details(self):
    #     driver = self.driver
    #     # Emergency Contacts
    #     WebDriverWait(driver, 50).until(EC.element_to_be_clickable(self.emergency)).click()
    #     time.sleep(4)
    #     WebDriverWait(driver, 50).until(EC.presence_of_element_located(self.name)).send_keys("Jack")
    #     time.sleep(4)
    #     WebDriverWait(driver, 50).until(EC.presence_of_element_located(self.relationship)).send_keys("Friend")
    #     time.sleep(4)
    #     WebDriverWait(driver, 50).until(EC.presence_of_element_located(self.phone)).send_keys("9876543210")
    #     time.sleep(4)
    #     WebDriverWait(driver, 50).until(EC.element_to_be_clickable(self.save1)).click()
    #     time.sleep(4)

    def test_dependent_details(self):
        driver = self.driver
        # Dependents
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(self.dependent)).click()
        time.sleep(4)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(self.add2)).click()
        time.sleep(4)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(self.name1)).send_keys("Jack")
        time.sleep(4)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(self.save2)).click()
        time.sleep(4)

    def test_immigration_details(self):
        driver = self.driver
        # Immigration
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(self.immigration)).click()
        time.sleep(4)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(self.add3)).click()
        time.sleep(4)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(self.passport)).click()
        time.sleep(4)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(self.number)).send_keys("12")
        time.sleep(4)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(self.issue_date)).send_keys("2024-24-06")
        time.sleep(4)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(self.expiry_date)).send_keys("2026-24-06")
        time.sleep(4)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(self.save3)).click()
        time.sleep(4)

    # def test_qualification_details(self):
    #     driver = self.driver
    #     # Qualifications
    #     WebDriverWait(driver, 10).until(EC.element_to_be_clickable(self.qualification)).click()
    #     time.sleep(4)
    #     WebDriverWait(driver, 10).until(EC.element_to_be_clickable(self.add4)).click()
    #     time.sleep(4)
    #     WebDriverWait(driver, 10).until(EC.presence_of_element_located(self.company)).send_keys("CTS")
    #     time.sleep(4)
    #     WebDriverWait(driver, 10).until(EC.presence_of_element_located(self.job_title)).send_keys("data analyst")
    #     time.sleep(4)
    #     WebDriverWait(driver, 10).until(EC.element_to_be_clickable(self.save4)).click()
    #     time.sleep(4)

    def test_membership_details(self):
        driver = self.driver
        # Memberships
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(self.membership)).click()
        time.sleep(4)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(self.add5)).click()
        time.sleep(4)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(self.member)).click()
        time.sleep(4)
        mem = driver.find_elements(By.CSS_SELECTOR, ".oxd-select-option span")
        for i in mem:
            if i.text == 'British Computer Society (BCS)':
                i.click()
                break
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(self.save4)).click()
        time.sleep(4)
