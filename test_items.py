link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_add_to_basket_button(browser):
    browser.get(link)
    basket_button = browser.find_elements_by_css_selector(".btn-add-to-basket")
    assert len(basket_button) > 0, "На странице товара не найдена кнопка добавления в корзину"