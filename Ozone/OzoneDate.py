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

        self.timeZone = self.setUpTimezone(timezone)

        try:
            self._dateTime: datetime = pytz.timezone(timezone).localize(datetime(
                self.year,
                self.month,
                self.day,
                self.hours,
                self.minutes
            ))

        except ValueError as ve:
            print(ve.__traceback__)

    def __str__(self):
        return f"{self.day:02d}.{self.month:02d}.{self.year:04d} {self.hours:02d}:{self.minutes:02d} ({self.ampm}) {self.timeZone}"

    def asTimeZone(self, timezone: Any) -> Any:
        return self._dateTime.astimezone(pytz.timezone(timezone))

    def setUpDay(self, day: Any) -> int:
        formattedDay = 0

        # Try for week day number
        try:
            return int(day)
        except Exception as e:
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

        except Exception as e:
            pass

        # Try for month names and abbreviations
        monthNames = {str(month).lower(): index for index, month in enumerate(calendar.month_name) if month}
        monthNamesAbbr = {str(month).lower(): index for index, month in enumerate(calendar.month_abbr) if month}

        if type(month) is str:
            month = month.strip()
            if month.lower() in monthNames:
                formattedMonth = monthNames[month.lower()]
            elif month.lower() in monthNamesAbbr:
                formattedMonth = monthNamesAbbr[month.lower()]

        return int(formattedMonth)

    def setUpYear(self, year: Any) -> int:
        formattedYear = 0

        try:
            return int(year)

        except Exception as e:
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

        except Exception as e:
            pass

        return formattedHours

    def setUpMinutes(self, minutes: Any) -> int:
        formattedMinutes = 0

        try:
            formattedMinutes = int(minutes)

        except Exception as e:
            pass

        return formattedMinutes

    def setUpTimezone(self, timezone: Any) -> pytz.timezone:
        # Where the fun lies
        formattedZone = ""

        try:
            formattedZone = pytz.timezone(timezone)

        except Exception as e:
            pass

        return formattedZone




