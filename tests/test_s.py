from urllib.parse import quote

from s import extraire_produits_depuis_page


def test_extraire_produits_depuis_page(driver):
    html = """
    <html>
      <body>
        <div class='product-card'>
          <a class='product-card__link-overlay' href='https://example.com/p1'></a>
          <div class='product-card__title'>Chaussure A</div>
          <div class='product-card__subtitle'>Homme</div>
          <div class='product-price'>129,99 EUR</div>
          <span class='color-loader__circle' style='background-color: red;'></span>
          <span class='color-loader__circle' style='background-color: blue;'></span>
        </div>
      </body>
    </html>
    """
    driver.get("data:text/html;charset=utf-8," + quote(html))

    produits = extraire_produits_depuis_page(driver)

    assert len(produits) == 1
    assert produits[0]["url"] == "https://example.com/p1"
    assert produits[0]["titre"] == "Chaussure A"
    assert produits[0]["description"] == "Homme"
    assert produits[0]["prix"] == "129,99 EUR"
    assert produits[0]["nb_couleurs"] == 2
