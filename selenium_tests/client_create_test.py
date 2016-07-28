import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from helper_library_selenium_in import *
from selenium.webdriver.support.ui import Select

#Global variables
g = Generate_information()
name = g.create_name()
id_number = g.create_id_num()
vat_number = g.create_vat_num()
website = g.create_website(name)
work_phone = g.create_phone()
address1 = g.create_street_address()
address2 = g.create_apt_suite()
city = g.create_first_name()
state = g.create_state_or_province()
postal_code = g.create_postal_code()
first_name = g.create_first_name()
last_name = g.create_last_name()
personal_email = g.create_email(name)
phone = g.create_phone()
email = g.create_email(name)

class TestLogin():

    @pytest.fixture
    def driver(self, request):
        driver_ = webdriver.Firefox()

        #def quit():
        #    driver_.quit()

        #request.addfinalizer(quit)
        return driver_

    def test_create_client(self,driver):
        driver.get("https://app.invoiceninja.com/login")
        driver.find_element(By.ID,"email").send_keys("henrycychen@gmail.com")
        driver.find_element(By.ID,"password").send_keys("qatesting123@")
        driver.find_element(By.ID,"loginButton").click()
        assert driver.find_element(By.CSS_SELECTOR,".active").is_displayed()

        #Clicking on client button
        driver.find_element(By.XPATH,"/html/body/nav/div/div[2]/ul/li[2]/a").click()
        time.sleep(5)
        assert driver.find_element(By.CSS_SELECTOR,".breadcrumb").is_displayed()

        #Need this delay to click on create new client
        time.sleep(10)

        #Clicking on new client
        driver.find_element(By.XPATH,"/html/body/div[1]/form/div[3]/a[2]").click()
        assert driver.find_element(By.CSS_SELECTOR,".active").is_displayed()

        driver.find_element(By.ID,"name").send_keys(name)

        driver.find_element(By.ID,"id_number").send_keys(id_number)

        driver.find_element(By.ID,"vat_number").send_keys(vat_number)

        driver.find_element(By.ID,"website").send_keys(website)

        driver.find_element(By.ID,"work_phone").send_keys(work_phone)

        driver.find_element(By.ID,"address1").send_keys(address1)

        driver.find_element(By.ID,"address2").send_keys(address2)

        driver.find_element(By.ID,"city").send_keys(city)

        driver.find_element(By.ID,"state").send_keys(state)

        driver.find_element(By.ID,"postal_code").send_keys(postal_code)

        driver.find_element(By.ID,"first_name").send_keys(first_name)

        driver.find_element(By.ID,"last_name").send_keys(last_name)

        #Personal Email
        driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/form/div[2]/div[2]/div[1]/div[2]/div/div[3]/div/input").send_keys(email)

        driver.find_element(By.ID,"phone").send_keys(phone)

        currency = Select(driver.find_element_by_id("currency_id"))
        currency.select_by_value('23')

        language_id = Select(driver.find_element_by_id("language_id"))
        language_id.select_by_value('4')

        payment_terms = Select(driver.find_element_by_id("payment_terms"))
        payment_terms.select_by_value('-1')

        size_id = Select(driver.find_element_by_id("size_id"))
        size_id.select_by_value('1')

        industry_id = Select(driver.find_element_by_id("industry_id"))
        industry_id.select_by_value('1')

        #private notes
        driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/form/div[2]/div[2]/div[2]/div[2]/div[6]/div/textarea").send_keys("test")

        #Clicking save to create client
        driver.find_element(By.CSS_SELECTOR, "html body.body div.container div.row form.form-horizontal.col-md-12.warn-on-exit center.buttons button.btn.btn-success.btn-lg").click()

        element = driver.find_element(By.CLASS_NAME, "col-md-3")
        check_assert = str(element.text)
        assert str(vat_number) in check_assert and \
               str(id_number) in check_assert and \
               str(address1) in check_assert and \
               str(address2) in check_assert and \
               city in check_assert and \
               state in check_assert and \
               website in check_assert and \
               "test" in check_assert and \
               "French" in check_assert and \
               "Net -1" in check_assert

        element2 = driver.find_element(By.CSS_SELECTOR, "html body.body div.container div.row div.col-md-7 div span")
        check_assert2 = str(element2.text)
        assert name == check_assert2


