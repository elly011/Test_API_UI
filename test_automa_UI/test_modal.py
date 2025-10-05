import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_modal():
    with allure.step("Ouvrir le navigateur & accéder à la page"):
        driver = webdriver.Chrome()
        driver.get("https://formy-project.herokuapp.com/modal")
        driver.maximize_window()

    with allure.step("Attendre & cliquer sur le bouton Open modal"):
        open_modal = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "modal-button"))
        )
        open_modal.click()

    with allure.step("Attendre que le modal soit visible"):
        WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "exampleModal"))
        )
 
    with allure.step("Cliquer sur le bouton Close"):
        close_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "close-button"))
        )

        time.sleep(1)
        close_button.click()

        time.sleep(2)
        driver.quit()
