import re, pytz, calendar

from datetime import datetime
from enum import Enum
from typing import Tuple, List


class OzoneRegex(Enum):
    format = r'(\$.*)\s*$'
    timezones = r'\s+(\D\S*)\s?(\D\S*)$'

    dmy = r''
    mdy = r''
    ydm = r''
    ymd = r''
    Mdy = r''
    h12 = r'\s+(?P<hours>\d{1,2})\s?:?\s?(?P<minutes>\d{0,2})\s?(?P<ampm>[AaPp]?\.?[Mm]?)\s+'
    h24 = r''


class OzoneDate:

    def __init__(self, day, month, year, hours, minutes, ampm, timezone):

        self.day = day
        self.month = month
        self.year = year

        self.hours = hours
        self.minutes = minutes
        self.ampm = ampm

        self.timezone = timezone


class Ozone:

    @staticmethod
    def ozonize(text: str) -> Tuple[str, str]:


        # Initialize the values
        text = text.strip()
        strippedText = ""

        outputStart = ""
        outputEnd = ""

        userInputZone = ""
        userOutputZone = ""

        # Work backwards, format -> zones -> time(s) -> date

        # Check for passed format, else set default and shorten the user input text
        try:
            userFormat = re.search(OzoneRegex.format.value, text)[0]
            strippedText = text.replace(userFormat, "").strip()

        except Exception as e:
            userFormat = "$dmy$24"
            strippedText = text.strip()

        formatList = userFormat.split("$")[1::]

        # Check for the timezones, else set default and shorten the user input text
        try:
            zones = re.findall(OzoneRegex.timezones.value, strippedText)

            userInputZone = zones[0][0]
            userOutputZone = zones[0][1]

            # 3 chains?
            strippedText = strippedText.replace(userInputZone, "")
            strippedText = strippedText.replace(userOutputZone, "")
            strippedText = strippedText.strip()

        except Exception as e:
            userInputZone = "CET"
            userOutputZone = "GMT"

        # Get regular expression pattern for set format
        regex = Ozone.getRegex(formatList)

        try:
            dateTimeMatchBox = re.match(regex, strippedText)

            userInputDay = dateTimeMatchBox.group('day')
            userInputMonth = dateTimeMatchBox.group('month')
            userInputYear = dateTimeMatchBox.group('year')

            userInputHoursStart = dateTimeMatchBox.group('hours')
            userInputMinutesStart = dateTimeMatchBox.group('minutes')
            userInputAmPmStart = dateTimeMatchBox.group('ampm')

            userInputHoursEnd = dateTimeMatchBox.group('hours')
            userInputMinutesEnd = dateTimeMatchBox.group('minutes')
            userInputAmPmEnd = dateTimeMatchBox.group('ampm')

        except Exception as e:
            now = datetime.now()
            userInputDay = now.day
            userInputMonth = now.month
            userInputYear = now.year

            userInputHoursStart = now.hour
            userInputMinutesStart = now.minute
            userInputAmPmStart = ""

        userInputDateTimeStart = OzoneDate(
            userInputDay,
            userInputMonth,
            userInputYear,
            userInputHoursStart,
            userInputMinutesStart,
            userInputAmPmStart
        )

        print(f"Input: {text}")
        print(f"Format: {userFormat}")
        print(f"Input Timezone: {userInputZone}")
        print(f"Output Timezone: {userOutputZone}")

        return outputStart, outputEnd


    @staticmethod
    def getRegex(formatList: List[str]) -> str:

        dateRegex = ""
        timeRegex = ""

        for format in formatList:

            match format:

                case "12":
                    timeRegex = OzoneRegex.h12.value

                case "24":
                    timeRegex = OzoneRegex.h24.value

                case "dmy":
                    dateRegex = OzoneRegex.dmy.value

                case "mdy":
                    dateRegex = OzoneRegex.mdy.value

                case "ymd":
                    dateRegex = OzoneRegex.ymd.value

                case "ydm":
                    dateRegex = OzoneRegex.ydm.value

                case "Mdy":
                    dateRegex = OzoneRegex.Mdy.value

        return f"{dateRegex} {timeRegex}"