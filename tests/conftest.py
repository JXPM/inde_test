import sys
from pathlib import Path

import pytest
from selenium import webdriver

# Permet d'importer les scripts du dossier racine (inscription.py, s.py).
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1400,1000")

    instance = webdriver.Chrome(options=options)
    try:
        yield instance
    finally:
        instance.quit()
