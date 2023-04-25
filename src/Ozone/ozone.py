import re, pytz, calendar
from datetime import datetime
from enum import Enum


class OzoneRegex(Enum):
    format = r'(\$.*)\s*$'
    timezones = r'\s+(\D\S*)\s?(\D\S*)$'

    dmy = r''
    mdy = r''
    ydm = r''
    ymd = r''
    Mdy = r''
    h12 = r'\s+(\d{1,2})\s?:?\s?(\d{0,2})\s?([AaPp]?\.?[Mm]?)\s+'
    h24 = r''


class Ozone:

    def ozonize(text: str) -> None:


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
            print(f"Input Timezone: {userInputZone}")
            print(f"Output Timezone: {userOutputZone}")

            strippedText = strippedText.replace(userInputZone, "")
            strippedText = strippedText.replace(userOutputZone, "")
            print(strippedText)

        except Exception as e:
            userInputZone = "CET"
            userOutputZone = "GMT"

        for format in formatList:

            match format:

                case "12":
                    print("12")
                    userTime = re.findall(OzoneRegex.h12.value, strippedText)
                    for time in userTime:
                        print(f"Hours: {time[0]}, minutes: {time[1]}, am/pm: {time[2]}")
                case "24":
                    print("24")
                case "dmy":
                    print("dmy")
                case "mdy":
                    print("mdy")
                case "ymd":
                    print("ymd")
                case "ydm":
                    print("ydm")
                case "Mdy":
                    print("Mdy")

        print(f"Input: {text}")
        print(f"Format: {userFormat}")








Ozone.ozonize("20 04 2020 4 PM - 5 PM CET GMT $12")