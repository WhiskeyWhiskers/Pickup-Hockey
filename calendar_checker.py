import requests
import sys
import ipdb
from hamcrest import *


LOGIN_URL = "https://oaklandice.maxgalaxy.net/Login.aspx"
CALENDAR_URL = "http://oaklandice.maxgalaxy.net/Schedule.aspx?ID=2"


class ScheduleChecker(object):
    def __init__(self, current_month, next_month):
        self.current_month = current_month
        self.next_month = next_month

    def check_current_month(self):
        payload = {"ctl00$ContentPlaceHolder1$txtUserName": "stephen.akerson@gmail.com",
                   "ctl00$ContentPlaceHolder1$txtPassword": "ToughCookie11!"}
        headers = {
                   "Accept":                      "text/html,application/xhtml+xml,\
                                                  application/xml;q=0.9,image/webp,*/*;q=0.8",
                   "Accept-Encoding":             "gzip, deflate, br",
                   "Accept-Language":             "en-US,en;q=0.8",
                   "Cache-Control":               "max-age=0",
                   "Connection":                  "keep - alive",
                   "Content-Length":              "10576",
                   "Content-Type":                "application / x - www - form - urlencoded",
                   "Host":                        "oaklandice.maxgalaxy.net",
                   "Origin":                      "https: // oaklandice.maxgalaxy.net",
                   "Referer":                     "https: // oaklandice.maxgalaxy.net / Login.aspx",
                   "Upgrade-Insecure-Requests":   "1",
                   "User-Agent":                  "Mozilla / 5.0(Macintosh; Intel Mac OS X 10_12_5)\
                                                  AppleWebKit / 537.36(KHTML, like Gecko) \
                                                  Chrome / 58.0.3029.110 Safari / 537.36"
                   }

        r1 = requests.get(LOGIN_URL)
        cookie_name = r1.cookies.keys()[0]
        cookie_val = r1.cookies[cookie_name]
        payload[cookie_name] = cookie_val
        ipdb.set_trace()
        session = requests.Session()
        resp = session.post(LOGIN_URL, headers=headers, data=payload)
        print resp.status_code
        ipdb.set_trace()
        #print("{0}: {1}".format(self.current_month, r.text.count(self.current_month)))
        #print("{0}: {1}".format(self.next_month, r.text.count(self.next_month)))
        assert_that(r.text.count(self.current_month), greater_than(r.text.count(self.next_month)))
        assert_that(r.text.count(self.next_month), greater_than_or_equal_to(1))

if __name__ == "__main__":
    current_month = sys.argv[1]
    next_month = sys.argv[2]
    s = ScheduleChecker(current_month, next_month)
    s.check_current_month()
