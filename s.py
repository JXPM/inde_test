import time

from selenium import webdriver
from selenium.webdriver.common.by import By

NIKE_TENNIS_URL = "https://www.nike.com/fr/w/tennis-ed1q"


def extraire_produits_depuis_page(driver: webdriver.Chrome) -> list[dict]:
    articles = driver.find_elements(By.CLASS_NAME, "product-card")
    produits = []

    for article in articles:
        url = article.find_element(
            By.CLASS_NAME, "product-card__link-overlay"
        ).get_attribute("href")
        title = article.find_element(By.CLASS_NAME, "product-card__title").text
        description = article.find_element(By.CLASS_NAME, "product-card__subtitle").text
        price = article.find_element(By.CLASS_NAME, "product-price").text
        couleurs = article.find_elements(By.CLASS_NAME, "color-loader__circle")
        liste_couleurs = [
            c.get_attribute("style").replace("background-color:", "").strip()
            for c in couleurs
        ]

        produits.append(
            {
                "url": url,
                "titre": title,
                "description": description,
                "prix": price,
                "nb_couleurs": len(liste_couleurs),
                "couleurs": liste_couleurs,
            }
        )

    return produits


def demo_locale() -> None:
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)

    try:
        driver.get(NIKE_TENNIS_URL)
        time.sleep(5)

        produits = extraire_produits_depuis_page(driver)
        for produit in produits:
            print(produit)
    finally:
        driver.quit()


if __name__ == "__main__":
    demo_locale()
