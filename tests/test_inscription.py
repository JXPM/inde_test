import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def test_inscription_anime_sama():
    options = Options()
    options.add_argument("--headless") 
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    # Ajout de cette option pour éviter les blocages réseaux en CI
    options.add_argument("--ignore-certificate-errors") 
    
    driver = webdriver.Chrome(options=options)
    
    try:
        # Testez avec .fr ou .tv selon ce qui marche chez vous aujourd'hui
        driver.get("https://anime-sama.tv/login/") 
        wait = WebDriverWait(driver, 20)

        # Utilisation de PARTIAL_LINK_TEXT pour être plus flexible sur le texte exact
        creer_compte_btn = wait.until(
            EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Créer"))
        )
        creer_compte_btn.click()

        pseudo_field = wait.until(
            EC.visibility_of_element_located((By.ID, "registerPseudo"))
        )
        pseudo_field.send_keys("monPseudoTest123")
        
        assert pseudo_field.get_attribute("value") == "monPseudoTest123"
        
    finally:
        driver.quit()