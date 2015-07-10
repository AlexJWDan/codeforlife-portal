from portal.tests.pageObjects.portal.base_page import BasePage

class StudentPasswordResetFormPage(BasePage):
    def __init__(self, browser):
        super(StudentPasswordResetFormPage, self).__init__(browser)

        self.browser.find_element_by_id('studentPasswordResetForm_page')
        assert self.browser.find_element_by_id('id_username').get_attribute('placeholder') == 'rosie_f'

    def cancel(self):
        self.browser.find_element_by_id('cancel_button').click()
        from portal.tests.pageObjects.portal.home_page import HomePage

        return HomePage(self.browser)
