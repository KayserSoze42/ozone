import re
from datetime import datetime
from enum import Enum
from typing import Tuple, List

from Ozone.OzoneDate import OzoneDate


class Constants(Enum):
    # REGEX
    format = r'(\$.*)\s*$'

    timezones = r'\s+(\D\S*) (\D\S*)$'

    dmy = r'\s*(?P<date_day>\d{1,2})[\./-]?(?P<date_month>\d{1,2})[\./-](?P<date_year>\d{2,4})\s*'

    mdy = r'\s*(?P<date_month>\d{1,2})\s?[\./-]?\s?(?P<date_day>\d{1,2})\s?[\./-]?\s?(?P<date_year>\d{2,4})\s*'

    ydm = r'\s*(?P<date_year>\d{2,4})\s?[\./-]?\s?(?P<date_day>\d{1,2})\s?[\./-]?\s?(?P<date_month>\d{1,2})\s*'

    ymd = r'\s*(?P<date_year>\d{2,4})\s?[\./-]?\s?(?P<date_month>\d{1,2})\s?[\./-]?\s?(?P<date_date>\d{1,2})\s*'

    Mdy = r''

    h12 = r'\s*(?P<hours_start>\d{1,2})\s?:?\s?(?P<minutes_start>\d{0,2})\s?(?P<ampm_start>[AaPp]?\.?[Mm]?)\s?[->]?\s?' \
          r'(?P<hours_end>\d{0,2})\s?:?\s?(?P<minutes_end>\d{0,2})\s?(?P<ampm_end>[AaPp]?\.?[Mm]?)\s*'

    h24 = r'\s*(?P<hours_start>\d{1,2})\s?:?\s?(?P<minutes_start>\d{0,2})\s?[->]?\s?' \
          r'(?P<hours_end>\d{0,2})\s?:?\s?(?P<minutes_end>\d{0,2})\s*'

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
        strippedText, userFormat = Ozone.extractFormat(text)
        formatList = userFormat.split("$")[1::]

        # Check for the timezones and shorten the user input text, else raise KeyError
        strippedText, userInputZone, userOutputZone = Ozone.extractTimeZones(strippedText)

        # Get regular expression pattern for set format
        regex = re.compile(Ozone.getRegex(formatList))

        try:
            dateTimeMatchBox = re.match(regex, strippedText)

            userInputDay = dateTimeMatchBox.group('date_day')
            userInputMonth = dateTimeMatchBox.group('date_month')
            userInputYear = dateTimeMatchBox.group('date_year')

            userInputHoursStart = dateTimeMatchBox.group('hours_start')
            userInputMinutesStart = dateTimeMatchBox.group('minutes_start')

            if dateTimeMatchBox.group('ampm_start') is not None:
                userInputAmPmStart = dateTimeMatchBox.group('ampm_start')

            if dateTimeMatchBox.group('hours_end') is not None:
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
            ).asTimeZone(userOutputZone)

            outputStart = userInputDateTimeStart.strftime("%d.%m.%Y %H:%M ") + f" {userOutputZone}"

            if userInputHoursEnd is not None:

                userInputDateTimeEnd = OzoneDate(
                    userInputDay,
                    userInputMonth,
                    userInputYear,
                    userInputHoursEnd,
                    userInputMinutesEnd,
                    userInputAmPmEnd,
                    userInputZone
                ).asTimeZone(userOutputZone)

                outputEnd = userInputDateTimeEnd.strftime("%d.%m.%Y %H:%M ") + f" {userOutputZone}"

        except:
            pass

        return outputStart, outputEnd

    @staticmethod
    def extractFormat(text: str) -> Tuple[str, str]:

        try:
            userFormat = re.search(Constants.format.value, text)[0]
            strippedText = text.replace(userFormat, "").strip()

        except Exception as e:
            userFormat = "$dmy$24"
            strippedText = text.strip()

        finally:
            return strippedText, userFormat

    @staticmethod
    def extractTimeZones(text: str) -> Tuple[str, str, str]:

        try:
            zones = re.findall(Constants.timezones.value, text)

            inputZone = zones[0][0]
            outputZone = zones[0][1]

            # 3 chains?
            strippedText = text.replace(inputZone, "")
            strippedText = strippedText.replace(outputZone, "")
            strippedText = strippedText.strip()

        except Exception as e:
            raise KeyError(f"Unable to extract time zones from passed text: {text}")

        finally:
            return strippedText, inputZone, outputZone


    @staticmethod
    def getRegex(formatList: List[str]) -> re.Pattern:

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

        dateRegex = Constants.dmy.value if dateRegex == "" else dateRegex
        timeRegex = Constants.h24.value if timeRegex == "" else timeRegex

        return re.compile(f"{dateRegex} {timeRegex}")


testOzone = Ozone.ozonize("04.20.2020 04:00 PM CET GMT $12")