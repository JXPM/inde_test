import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

ANIME_SAMA_LOGIN_URL = "https://anime-sama.tv/login/"

def remplir_formulaire_inscription(
    driver: webdriver.Chrome,
    pseudo: str,
    password: str,
    url: str = ANIME_SAMA_LOGIN_URL,
) -> None:
    driver.get(url)
    wait = WebDriverWait(driver, 15)

    wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//div[@id='loginForm']//a[contains(., 'Créer un compte')]")
        )
    ).click()

    wait.until(EC.visibility_of_element_located((By.ID, "registerPseudo"))).send_keys(
        pseudo
    )
    driver.find_element(By.ID, "registerPassword").send_keys(password)
    driver.find_element(By.ID, "registerPassword2").send_keys(password)


def demo_locale() -> None:
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)

    try:
        remplir_formulaire_inscription(
            driver=driver,
            pseudo="ADOlasolution",
            password="MonMdp123!",
        )

        time.sleep(10)
    finally:
        driver.quit()


if __name__ == "__main__":
    demo_locale()
