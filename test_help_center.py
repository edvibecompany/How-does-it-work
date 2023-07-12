from selene import browser, have, be

def test_open_articles():
    browser.open('https://edvibe.com/Account/Login')
    browser.element('.form-input [name=Email]').type('misha-marinov@mail.ru')
    browser.element('.form-input [name=Password]').type('liveUT00mPE8CB7Z').press_enter()
    browser.wait_until(browser.element('form > button:nth-child(4)').should(be.visible))
    browser.element('form > button:nth-child(4)').click()
    browser.wait_until(have.url_containing('/TeacherAccount/'))

    browser.element('#header .how-it-works-container').click()
    browser.element('.list .item:nth-child(2)').click()

    # Переключение на новую вкладку
    browser.switch_to.window(browser.driver.window_handles[1])
    browser.should(have.title('Курс: Онлайн-уроки от А до Я | База знаний'))