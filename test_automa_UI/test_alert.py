import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@allure.title("Automoatisé l'affichage d'alerte")
@allure.description("Ce test ouvre la page, et accepte l'alerte.")

def test_alert():
    with allure.step("Ouvrir le navigateur & accéder à la page"):
        driver = webdriver.Chrome()
        driver.get("https://formy-project.herokuapp.com/switch-window")

    with allure.step("Click sur le bouton qui déclenche l'alerte"):
        alert_button = driver.find_element(By.ID, "alert-button")
        alert_button.click()

    with allure.step("Accepter l'alerte"):
        alert = driver.switch_to.alert
        time.sleep(2)
        alert.accept()

    with allure.step("Attendre 2s & Fermer le navigateur"):
        time.sleep(2)
        driver.quit()