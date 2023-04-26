from typing import Any

import calendar
import pytz

from datetime import datetime



class OzoneDate:

    def __init__(self, day, month, year, hours, minutes, timezone, ampm=""):

        self.day = self.setUpDay(day)
        self.month = self.setUpMonth(month)
        self.year = self.setUpYear(year)

        self.ampm = ampm.lower()
        self.hours = self.setUpHours(hours)
        self.minutes = self.setUpMinutes(minutes)

        self.timezone = self.setUpTimezone(timezone)

        self.dateTime = None

    def __str__(self):
        return f"{self.day:02d}.{self.month:02d}.{self.year:04d} {self.hours:02d}:{self.minutes:02d} {self.ampm} {self.timezone}"

    def getDateTimeLocalized(self) -> datetime:
        if self.dateTime is None:
            self.dateTime = self.timezone.localize(datetime(
                self.year,
                self.month,
                self.day,
                self.hours,
                self.minutes
            ))
        return self.dateTime



    def setUpDay(self, day: Any) -> int:
        formattedDay = 0

        # Try for week day number
        try:
            return int(day)
        except:
            pass

        # Try for week day names and abbreviations
        dayNames = {str(day).lower(): index for index, day in enumerate(calendar.day_name) if day}
        dayNamesAbbr = {str(day).lower(): index for index, day in enumerate(calendar.day_abbr) if day}

        if type(day) is str:
            if day.lower() in dayNames:
                formattedDay = dayNames[day.lower()]
            elif day.lower() in dayNamesAbbr:
                formattedDay = dayNamesAbbr[day.lower()]

        return formattedDay

    def setUpMonth(self, month: Any) -> int:
        formattedMonth = 0

        # Try for month number
        try:
            return int(month)

        except:
            pass

        # Try for month names and abbreviations
        monthNames = {str(month).lower(): index for index, month in enumerate(calendar.month_name) if month}
        monthNamesAbbr = {str(month).lower(): index for index, month in enumerate(calendar.month_abbr) if month}

        if type(month) is str:
            if month.lower() in monthNames:
                formattedMonth = monthNames[month.lower()]
            elif month.lower() in monthNamesAbbr:
                formattedMonth = monthNamesAbbr[month.lower()]

        return formattedMonth

    def setUpYear(self, year: Any) -> int:
        formattedYear = 0

        try:
            return int(year)

        except:
            pass

        return formattedYear

    def setUpHours(self, hours: Any) -> int:
        formattedHours = 0

        try:
            formattedHours = int(hours)

            if self.ampm == "pm":
                if formattedHours == 12:
                    return 12
                formattedHours += 12

            elif self.ampm == "am":
                if formattedHours == 12:
                    return 0

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

    def setUpTimezone(self, timezone: Any) -> pytz.timezone:
        # Where the fun lies
        formattedZone = ""

        try:
            formattedZone = pytz.timezone(timezone)

        except:
            pass

        return formattedZone




