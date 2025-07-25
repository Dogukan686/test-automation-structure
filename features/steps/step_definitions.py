from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

@given('kullanıcı e-ticaret sitesine gider')
def step_impl(context):
    browser = context.config.userdata.get("browser", "chrome").lower()
    if browser == "firefox":
        context.driver = webdriver.Firefox()
    else:
        context.driver = webdriver.Chrome()
    context.driver.get("https://demowebshop.tricentis.com/")  # Örnek demo site
    context.driver.maximize_window()

@given('kullanıcı giriş yapar')
def step_impl(context):
    driver = context.driver
    driver.find_element(By.LINK_TEXT, "Log in").click()
    driver.find_element(By.ID, "Email").send_keys("testuser@example.com")
    driver.find_element(By.ID, "Password").send_keys("Test1234")
    driver.find_element(By.CSS_SELECTOR, "input.login-button").click()

@when('kullanıcı "cep telefonu" araması yapar')
def step_impl(context):
    driver = context.driver
    search_box = driver.find_element(By.ID, "small-searchterms")
    search_box.send_keys("phone")
    search_box.send_keys(Keys.RETURN)

@when('fiyat aralığını 15000 - 20000 TL olarak filtreler')
def step_impl(context):
    # Bu demo sitede fiyat filtresi yok; gerçek siteye göre adapte edilir
    pass

@when('en alt sıradaki ürünü seçip detayına gider')
def step_impl(context):
    driver = context.driver
    products = driver.find_elements(By.CSS_SELECTOR, ".product-item")
    if products:
        products[-1].find_element(By.TAG_NAME, "a").click()

@when('en düşük puanlı satıcının ürününü sepete ekler')
def step_impl(context):
    driver = context.driver
    driver.find_element(By.ID, "add-to-cart-button-18").click()  # Örnek ID

@then('ürünün sepete doğru şekilde eklendiği kontrol edilir')
def step_impl(context):
    driver = context.driver
    time.sleep(2)
    cart_qty = driver.find_element(By.CSS_SELECTOR, "span.cart-qty").text
    assert cart_qty != "(0)", "Ürün sepete eklenemedi!"
    driver.quit()
