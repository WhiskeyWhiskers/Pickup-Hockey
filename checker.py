#!/Users/Akerson/.virtualenvs/pickup-hockey/bin/python

import os
import sys
import urllib

import requests

from data.posts import LOGIN_FORM_DATA, LOGOUT_FORM_DATA


class ScheduleChecker(object):
    def __init__(self, month_id):
        self.cal_url = 'https://oaklandice.maxgalaxy.net/DayCampSelection.aspx?DayCampID=%s' % month_id
        self.login_url = 'https://oaklandice.maxgalaxy.net/Login.aspx'

        self.month_ready_msg = 'Drop-In Hockey'
        self.month_unready_msg = 'Registration does not fall within'
        self.logged_out_msg = 'You must be logged in to register'

        self.pw = urllib.quote(os.getenv('OIC_PW'))
        self.email = urllib.quote(os.getenv('OIC_EMAIL'))

        self.session = self.create_session()
        self.login_form_data = LOGIN_FORM_DATA.format(OIC_PW=self.pw, OIC_EMAIL=self.email)

    def create_session(self):
        s = requests.Session()
        s.headers.update({'Content-Type': 'application/x-www-form-urlencoded'})
        return s

    def login(self):
        self.session.post(url=self.login_url, data=self.login_form_data)

    def logout(self):
        self.session.post(url=self.cal_url, data=LOGOUT_FORM_DATA)

    def check_current_month(self):
        r_cal = self.session.get(self.cal_url)
        if self.logged_out_msg in r_cal.text:
            print("Logged out of Oakland Ice!")
        elif self.month_unready_msg in r_cal.text:
            print("Nothing posted yet")
        elif self.month_ready_msg in r_cal.text:
            print("New spots are up!")
        else:
            raise RuntimeError('The dom has changed! Time to update this script...')

if __name__ == "__main__":
    month = sys.argv[1]
    s = ScheduleChecker(month)
    s.login()
    s.check_current_month()
    s.logout()
