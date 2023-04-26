import re
from datetime import datetime
from enum import Enum
from typing import Tuple, List

from Ozone.OzoneDate import OzoneDate


class Constants(Enum):
    # REGEX
    format = r'(\$.*)\s*$'

    timezones = r'\s+(\D\S*) (\D\S*)$'

    dmy = r''

    mdy = r''

    ydm = r''

    ymd = r''

    Mdy = r''

    h12 = r'\s+(?P<hours_start>\d{1,2})\s?:?\s?(?P<minutes_start>\d{0,2})\s?(?P<ampm_start>[AaPp]?\.?[Mm]?)\s?[->]?\s?' \
          r'(?P<hours_end>\d{1,2})\s?:?\s?(?P<minutes_end>\d{0,2})\s?(?P<ampm_end>[AaPp]?\.?[Mm]?)\s*'

    h24 = r''

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
            userFormat = re.search(Constants.format.value, text)[0]
            strippedText = text.replace(userFormat, "").strip()

        except Exception as e:
            userFormat = "$dmy$24"
            strippedText = text.strip()

        formatList = userFormat.split("$")[1::]

        # Check for the timezones, else set default and shorten the user input text
        try:
            zones = re.findall(Constants.timezones.value, strippedText)

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

            userInputHoursStart = dateTimeMatchBox.group('hours_start')
            userInputMinutesStart = dateTimeMatchBox.group('minutes_start')
            userInputAmPmStart = dateTimeMatchBox.group('ampm_start')

            userInputHoursEnd = dateTimeMatchBox.group('hours_end')
            userInputMinutesEnd = dateTimeMatchBox.group('minutes_end')
            userInputAmPmEnd = dateTimeMatchBox.group('ampm_end')

        except Exception as e:
            return '', ''

        try:
            userInputDateTimeStart = OzoneDate(
                userInputDay,
                userInputMonth,
                userInputYear,
                userInputHoursStart,
                userInputMinutesStart,
                userInputAmPmStart,
                userInputZone
            )

            outputStart = str(userInputDateTimeStart)

            if userInputHoursEnd is not None:

                userInputDateTimeEnd = OzoneDate(
                    userInputDay,
                    userInputMonth,
                    userInputYear,
                    userInputHoursEnd,
                    userInputMinutesEnd,
                    userInputAmPmEnd,
                    userInputZone
                )

                outputEnd = str(userInputDateTimeEnd)

        except:
            pass

        return outputStart, outputEnd


    @staticmethod
    def getRegex(formatList: List[str]) -> str:

        dateRegex = ""
        timeRegex = ""

        for format in formatList:

            match format:

                case "12":
                    timeRegex = Constants.h12.value

                case "24":
                    timeRegex = Constants.h24.value

                case "dmy":
                    dateRegex = Constants.dmy.value

                case "mdy":
                    dateRegex = Constants.mdy.value

                case "ymd":
                    dateRegex = Constants.ymd.value

                case "ydm":
                    dateRegex = Constants.ydm.value

                case "Mdy":
                    dateRegex = Constants.Mdy.value

        return f"{dateRegex} {timeRegex}"


testOzone = Ozone.ozonize("04.20.2020 04:00 PM CET GMT $12")