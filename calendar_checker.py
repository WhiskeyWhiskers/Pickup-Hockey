import requests
from hamcrest import *


CALENDAR_URL = "http://oaklandice.maxgalaxy.net/Schedule.aspx?ID=2"


class ScheduleChecker(object):
    def __init__(self, month, year):
        self.month = month
        self.year = year

    def check_current_month(self):
        r = requests.get(CALENDAR_URL)
        assert_that(r.text, contains_string("{month}, {year}".format(month=self.month, year=self.year)))

if __name__ == "__main__":
    s = ScheduleChecker("March", "2017")
    s.check_current_month()

