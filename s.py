from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

driver = webdriver.Chrome()
driver.get("https://www.nike.com/fr/w/tennis-ed1q")

# Attendre le chargement
time.sleep(5)

articles = driver.find_elements(By.CLASS_NAME, "product-card")

produits = []

for article in articles:
    url = article.find_element(By.CLASS_NAME, "product-card__link-overlay").get_attribute("href")
    title = article.find_element(By.CLASS_NAME, "product-card__title").text
    description = article.find_element(By.CLASS_NAME, "product-card__subtitle").text
    price = article.find_element(By.CLASS_NAME, "product-price").text
    couleurs = article.find_elements(By.CLASS_NAME, "color-loader__circle")
    liste_couleurs = [c.get_attribute("style").replace("background-color:", "").strip() for c in couleurs]
    nb_couleurs = len(liste_couleurs)
    
    produits.append({
    "url": url,
    "titre": title,
    "description": description,
    "prix": price,
    "nb_couleurs": nb_couleurs,
    "couleurs": liste_couleurs
                         })
    
    print(f"URL: {url}\nTitle: {title}\nDescription: {description}\nPrice: {price}\nNombre de couleurs: {nb_couleurs}\nCouleurs: {liste_couleurs}\n")


for produit in produits:
    print(produit)

driver.quit()