import pytz, calendar

from enum import Enum
from typing import Any, List


class OzoneConstants(Enum):
    # REGEX
    format = r'(\$.*)\s*$'

    timezones = r'\s+(\D\S*)\s?(\D\S*)$'

    dmy = r''

    mdy = r''

    ydm = r''

    ymd = r''

    Mdy = r''

    h12 = r'\s+(?P<hours_start>\d{1,2})\s?:?\s?(?P<minutes_start>\d{0,2})\s?(?P<ampm_start>[AaPp]?\.?[Mm]?)\s?[->]?\s?' \
          r'(?P<hours_end>\d{1,2})\s?:?\s?(?P<minutes_end>\d{0,2})\s?(?P<ampm_end>[AaPp]?\.?[Mm]?)\s*'

    h24 = r''

    # MONTHS

    monthNames: List[str] = [str(month).lower() for month in calendar.month_name if month]

    monthNamesAbbr: List[str] = [str(month).lower() for month in calendar.month_abbr if month]


class OzoneDate:

    def __init__(self, day, month, year, hours, minutes, timezone, ampm=""):

        self.day = self.setUpDay(day)
        self.month = self.setUpMonth(month)
        self.year = self.setUpYear(year)

        self.hours = self.setUpHours(hours)
        self.minutes = self.setUpMinutes(minutes)
        self.ampm = ampm

        self.timezone = self.setUpTimezone(timezone)

    def setUpDay(self, day: Any) -> int:
        formattedDay = 0

        try:
            formattedDay = int(day)

        except:
            pass

        return formattedDay

    def setUpMonth(self, month: Any) -> int:
        formattedMonth = 0

        try:
            formattedMonth = int(month)

        except:
            pass

        return formattedMonth

    def setUpYear(self, year: Any) -> int:
        formattedYear = 0

        try:
            formattedYear = int(year)

        except:
            pass

        return formattedYear

    def setUpHours(self, hours: Any) -> int:
        formattedHours = 0

        try:
            formattedHours = int(hours)

        except:
            pass

        return formattedHours

    def setUpMinutes(self, minutes: Any) -> int:
        formattedMinutes = 0

        try:
            formattedMinutes = int(minutes)

        except:
            pass

        return formattedMinutes

    def setUpTimezone(self, timezone: Any) -> str:
        # Where the fun lies
        formattedZone = ""

        try:
            formattedZone = pytz.timezone(timezone)

        except:
            pass

        return formattedZone


