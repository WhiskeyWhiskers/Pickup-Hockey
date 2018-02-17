from selenium import webdriver
import sys
import os


EMAIL = os.getenv('OIC_EMAIL')
PW = os.getenv('OIC_PW')
LOGIN_URL = 'http://oaklandice.maxgalaxy.net/BrowseDayCamps.aspx'
CAL_URL = 'http://oaklandice.maxgalaxy.net/DayCampSelection.aspx?DayCampID={}'


class ScheduleChecker(object):
    def __init__(self, next_month_id):
        self.next_camp_url = CAL_URL.format(next_month_id)
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def check_next_month(self):
        self.driver.get(LOGIN_URL)

        login_btn = self.driver.find_element_by_id('cmdLogin')
        login_btn.click()

        email_box = self.driver.find_element_by_id('ContentPlaceHolder1_txtUserName')
        pw_box = self.driver.find_element_by_id('ContentPlaceHolder1_txtPassword')
        login_sbt_btn = self.driver.find_element_by_id('ctl00_ContentPlaceHolder1_cmdSubmit_input')

        email_box.send_keys(EMAIL)
        pw_box.send_keys(PW)
        login_sbt_btn.click()

        try:
            self.driver.get(self.next_camp_url)
            too_early_message = self.driver.find_element_by_id(
                'ctl00_ContentPlaceHolder1_ctl00_ContentPlaceHolder1_litErrorPanel').text.lower()
            assert 'registration does not fall within' not in too_early_message
            raise Exception("New month is up!")
        except AssertionError:
            print "Nothing posted yet."


if __name__ == "__main__":
    next_month_id = sys.argv[1]
    s = ScheduleChecker(next_month_id)
    s.check_next_month()
