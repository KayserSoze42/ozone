import re
from datetime import datetime
from enum import Enum
from typing import Tuple, List

from Ozone.OzoneDate import OzoneDate


class Constants(Enum):
    # REGEX
    format = r'(\$.*)\s*$'

    timezones = r'\s*(\D\S*) (\D\S*)$'

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
        regex = Ozone.getRegex(formatList)

        # Extract date and time elements from the text using the regex
        userDate, userTimeStart, userTimeEnd = Ozone.extractDateTimeData(strippedText, regex)

        # Set up the date and time data received
        userDay = userDate[0]
        userMonth = userDate[1]
        userYear = userDate[2]

        userHoursStart = userTimeStart[0]
        userMinutesStart = userTimeStart[1]
        userAmPmStart = userTimeStart[2] if userTimeStart[2] is not None else ""

        userHoursEnd = userTimeEnd[0] if userTimeEnd[0] is not None else ""
        userMinutesEnd = userTimeEnd[1] if userTimeEnd[1] is not None else ""
        userAmPmEnd = userTimeEnd[2] if userTimeEnd[2] is not None else ""

        try:
            userInputDateTimeStart = OzoneDate(
                userDay,
                userMonth,
                userYear,
                userHoursStart,
                userMinutesStart,
                userInputZone,
                ampm=userAmPmStart
            ).asTimeZone(userOutputZone)

            outputStart = userInputDateTimeStart.strftime("%d.%m.%Y %H:%M ") + f"{userOutputZone}"

            if userHoursEnd != "":

                userInputDateTimeEnd = OzoneDate(
                    userDay,
                    userMonth,
                    userYear,
                    userHoursEnd,
                    userMinutesEnd,
                    userInputZone,
                    ampm=userAmPmEnd
                ).asTimeZone(userOutputZone)

                outputEnd = userInputDateTimeEnd.strftime("%d.%m.%Y %H:%M ") + f"{userOutputZone}"

        except:
            raise ValueError(f"Unable to set start date from text: {text}")

        return outputStart, outputEnd

    @staticmethod
    def extractDateTimeData(text: str, regex: re.Pattern):
        date = []
        timeStart = []
        timeEnd = []

        dateTimeMatchBox = re.match(regex, text)

        try:
            inputDay = dateTimeMatchBox.group('date_day')
            inputMonth = dateTimeMatchBox.group('date_month')
            inputYear = dateTimeMatchBox.group('date_year')

            inputHoursStart = dateTimeMatchBox.group('hours_start')
            inputMinutesStart = dateTimeMatchBox.group('minutes_start')

            date.append(inputDay)
            date.append(inputMonth)
            date.append(inputYear)

            timeStart.append(inputHoursStart)
            timeStart.append(inputMinutesStart)

        except Exception as e:
            raise ValueError(f"Unable to extract date and time values from text: {text}")

        try:
            inputAmPmStart = dateTimeMatchBox.group('ampm_start')
            timeStart.append(inputAmPmStart)
        except:
            timeStart.append("")

        try:
            inputHoursEnd = dateTimeMatchBox.group('hours_end')
            inputMinutesEnd = dateTimeMatchBox.group('minutes_end')

            timeEnd.append(inputHoursEnd)
            timeEnd.append(inputMinutesEnd)
        except:
            timeEnd.append("")
            timeEnd.append("")

        try:
            inputAmPmEnd = dateTimeMatchBox.group('ampm_end')

            timeEnd.append(inputAmPmEnd)
        except:
            timeEnd.append("")

        return date, timeStart, timeEnd

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
            strippedText = re.sub(Constants.timezones.value, "", text).strip()


            return strippedText, inputZone, outputZone

        except Exception as e:
            raise KeyError(f"Unable to extract time zones from passed text: {text}")

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

