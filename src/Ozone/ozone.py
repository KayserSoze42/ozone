import re

from datetime import datetime
from typing import Tuple, List
from .ozone_utils import OzoneConstants, OzoneDate


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
            userFormat = re.search(OzoneConstants.format.value, text)[0]
            strippedText = text.replace(userFormat, "").strip()

        except Exception as e:
            userFormat = "$dmy$24"
            strippedText = text.strip()

        formatList = userFormat.split("$")[1::]

        # Check for the timezones, else set default and shorten the user input text
        try:
            zones = re.findall(OzoneConstants.timezones.value, strippedText)

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
                    timeRegex = OzoneConstants.h12.value

                case "24":
                    timeRegex = OzoneConstants.h24.value

                case "dmy":
                    dateRegex = OzoneConstants.dmy.value

                case "mdy":
                    dateRegex = OzoneConstants.mdy.value

                case "ymd":
                    dateRegex = OzoneConstants.ymd.value

                case "ydm":
                    dateRegex = OzoneConstants.ydm.value

                case "Mdy":
                    dateRegex = OzoneConstants.Mdy.value

        return f"{dateRegex} {timeRegex}"