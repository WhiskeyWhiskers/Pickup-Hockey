from logging import info
import requests
import sys
from hamcrest import *


CALENDAR_URL = "http://oaklandice.maxgalaxy.net/Schedule.aspx?ID=2"


class ScheduleChecker(object):
    def __init__(self, current_month, next_month):
        self.current_month = current_month
        self.next_month = next_month

    def check_current_month(self):
        r = requests.get(CALENDAR_URL)
        print("{0}: {1}".format(self.current_month, r.text.count(self.current_month)))
        print("{0}: {1}".format(self.next_month, r.text.count(self.next_month)))
        assert_that(r.text.count(self.current_month), greater_than(r.text.count(self.next_month)))
        assert_that(r.text.count(self.next_month), greater_than_or_equal_to(1))

if __name__ == "__main__":
    current_month = sys.argv[1]
    next_month = sys.argv[2]
    s = ScheduleChecker(current_month, next_month)
    s.check_current_month()
