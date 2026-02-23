import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

def test_nike_extraction():
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    
    driver.get("https://www.nike.com/fr/w/tennis-ed1q")
    time.sleep(5) # Attente du chargement des produits

    articles = driver.find_elements(By.CLASS_NAME, "product-card")
    
    # Assertion : On vérifie qu'on a extrait au moins un article
    assert len(articles) > 0, "Aucun article trouvé sur Nike"
    driver.quit()