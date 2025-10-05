import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_liste_deroulante():
    with allure.step("Ouvrir le navigateur & accéder à la page"):
        driver = webdriver.Chrome()
        driver.get("https://formy-project.herokuapp.com/dropdown")

    with allure.step("l'affichage pendant 1s avant de continuer le test"):
        time.sleep(1)

    with allure.step("l'affichage pendant 1s avant de continuer le test"):
       dropdown_button = driver.find_element(By.ID, "dropdownMenuButton")
       dropdown_button.click()
       time.sleep(1)
    
    with allure.step("Dérouler l'ensemble de menu"):
       options = driver.find_elements(By.CSS_SELECTOR, ".dropdown-menu a")

    with allure.step("Attendre 2s & Fermer le navigateur"):
       time.sleep(2)
       driver.quit()