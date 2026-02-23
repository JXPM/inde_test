from urllib.parse import quote

from inscription import remplir_formulaire_inscription


def test_remplir_formulaire_anime_sama(driver):
    html = """
    <html>
      <body>
        <div id='loginForm'>
          <a onclick='document.getElementById("registerForm").style.display="block";'>Créer un compte</a>
        </div>
        <div id='registerForm' style='display:none;'>
          <input id='registerPseudo' type='text' />
          <input id='registerPassword' type='password' />
          <input id='registerPassword2' type='password' />
        </div>
      </body>
    </html>
    """
    url = "data:text/html;charset=utf-8," + quote(html)

    remplir_formulaire_inscription(
        driver=driver,
        pseudo="monPseudoTest123",
        password="MonMdpTest123!",
        url=url,
    )

    assert driver.find_element("id", "registerPseudo").get_attribute("value") == "monPseudoTest123"
    assert driver.find_element("id", "registerPassword").get_attribute("value") == "MonMdpTest123!"
    assert driver.find_element("id", "registerPassword2").get_attribute("value") == "MonMdpTest123!"
