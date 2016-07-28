import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestLogin():

    @pytest.fixture
    def driver(self, request):
        driver_ = webdriver.Firefox()

        def quit():
            driver_.quit()

        request.addfinalizer(quit)
        return driver_

    def test_valid_credentials(self,driver):
        driver.get("https://app.invoiceninja.com/login")
        driver.find_element(By.ID,"email").send_keys("henrycychen@gmail.com")
        driver.find_element(By.ID,"password").send_keys("qatesting123@")
        driver.find_element(By.ID,"loginButton").click()
        assert driver.find_element(By.CSS_SELECTOR,".active").is_displayed()