import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def remplir_formulaire_inscription() -> None:
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)

    try:
        driver.get("https://anime-sama.tv/login/")
        wait = WebDriverWait(driver, 15)

        # 1) Aller sur "Créer un compte"
        wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//div[@id='loginForm']//a[contains(., 'Créer un compte')]")
            )
        ).click()

        # 2) Remplir pseudo, mot de passe, confirmation (IDs exacts)
        wait.until(EC.visibility_of_element_located((By.ID, "registerPseudo"))).send_keys(
            "monPseudoTest123"
        )
        driver.find_element(By.ID, "registerPassword").send_keys("MonMdpTest123!")
        driver.find_element(By.ID, "registerPassword2").send_keys("MonMdpTest123!")

        # Laisse quelques secondes pour voir le résultat
        time.sleep(10)

    finally:
        driver.quit()


if __name__ == "__main__":
    remplir_formulaire_inscription()
