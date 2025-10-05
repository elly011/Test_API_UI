import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_modal():
    with allure.step("Ouvrir le navigateur & accéder à la page"):
        driver = webdriver.Chrome()
        driver.get("https://formy-project.herokuapp.com/radiobutton")

    with allure.step("selectionner button radio"):
        radio2 = driver.find_element(By.CSS_SELECTOR, "input[value='option2']")
        radio2.click()
        time.sleep(2)
    
    with allure.step("fermer fenetre"):
        driver.quit()