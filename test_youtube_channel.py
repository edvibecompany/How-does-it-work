from selene import browser, have, be

def test_open_youtube_channel():
    browser.open('https://preview.edvibe.com/Account/Login')
    browser.element('.form-input [name=Email]').type('misha-marinov@mail.ru')
    browser.element('.form-input [name=Password]').type('liveUT00mPE8CB7Z').press_enter()
    browser.wait_until(browser.element('form > button:nth-child(4)').should(be.visible))
    browser.element('form > button:nth-child(4)').click()
    browser.wait_until(have.url_containing('/TeacherAccount/'))

    browser.element('#header .how-it-works-container').click()
    browser.element('.additional .item:nth-child(2)').click()

    # Переключение на новую вкладку
    browser.switch_to.window(browser.driver.window_handles[1])
    browser.should(have.url('https://www.youtube.com/channel/UCCiL05p57jmbPhcZz9xkVvQ'))