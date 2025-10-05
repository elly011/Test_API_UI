import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

def test_glisser_im():
    with allure.step("Ouvrir le navigateur & accéder à la page"):
        driver = webdriver.Chrome()
        driver.get("https://formy-project.herokuapp.com/dragdrop")

    with allure.step("Chercher bu id"):
        image = driver.find_element(By.ID, "image")
        zone = driver.find_element(By.ID, "box")
 
    with allure.step("L'action de drag and drop"):
        actions = ActionChains(driver)
        actions.drag_and_drop(image, zone).perform()

    with allure.step("Attendre 2s & Fermer le navigateur"):
        time.sleep(2)
        driver.quit()
