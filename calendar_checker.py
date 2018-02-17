import requests
import sys
import ipdb
from data.form_data import LOGIN_FORM_DATA, LOGOUT_FORM_DATA

CAL_URL = 'https://oaklandice.maxgalaxy.net/DayCampSelection.aspx?DayCampID={MONTH_ID}'
COOKIE = {'ASP.NET_SessionId': 'y2sovzczlybdoc0wajkpfjr0'}

class ScheduleChecker(object):
    def __init__(self, month_id):
        self.cal_url = CAL_URL.format(MONTH_ID=month_id)
        self.login_url = 'https://oaklandice.maxgalaxy.net/Login.aspx'
        self.session = self.create_session()

    def create_session(self):
        s = requests.Session()
        s.headers.update({
            'Upgrade-Insecure-Requests': '1',
            'Cache-Control'            : 'max-age=0',
            'Content-Type'             : 'application/x-www-form-urlencoded',
            'User-Agent'               : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36',
            'Referer'                  : 'https://oaklandice.maxgalaxy.net/Login.aspx',
            'Accept'                   : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding'          : 'gzip, deflate, br',
            'Host'                     : 'oaklandice.maxgalaxy.net',
            'Accept-Language'          : 'en-US,en;q=0.9',
            'Cookie'                   : 'ASP.NET_SessionId=y2sovzczlybdoc0wajkpfjr0; BIGipServer~maxgalaxy~maxgalaxy_lvprod_leg_http=3701503754.20480.0000'
        })
        cj = requests.utils.cookiejar_from_dict(COOKIE)
        s.cookies = cj
        return s

    def login(self):
        self.session.post(url=self.login_url, data=LOGIN_FORM_DATA)

    def logout(self):
        self.session.post(url=self.cal_url, data=LOGOUT_FORM_DATA)

    def check_current_month(self):
        r_cal = self.session.get(self.cal_url)
        if 'does not' in r_cal.text:
            print("Nothing posted yet")
        else:
            print("New spots are up!")

if __name__ == "__main__":
    month = sys.argv[1]
    s = ScheduleChecker(month)
    s.login()
    s.check_current_month()
    s.logout()
