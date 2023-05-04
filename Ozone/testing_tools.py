import re
from typing import Tuple

from Ozone.Ozone import Ozone
from Ozone.OzoneDate import OzoneDate


class OzoneTT:

    @staticmethod
    def generate_mock_ozone_start_time_only(mockDate, mockTime, mockTimeZoneInput, mockTimeZoneOutput,
                                            mockFormat) -> str:
        dateTimeRegex = Ozone.getRegex(mockFormat.split('$')[1::])

        testData = re.match(dateTimeRegex, f"{mockDate} {mockTime}")

        testAmPm = ""
        try:
            testAmPm = testData.group('ampm_start')
        except:
            pass

        testDateTime = OzoneDate(
            testData.group('date_day'),
            testData.group('date_month'),
            testData.group('date_year'),
            testData.group('hours_start'),
            testData.group('minutes_start'),
            mockTimeZoneInput,
            ampm=testAmPm
        )

        output = testDateTime \
                     .asTimeZone(mockTimeZoneOutput) \
                     .strftime("%d.%m.%Y %H:%M") + f" {mockTimeZoneOutput}"

        return output

    @staticmethod
    def generate_mock_ozone_timeframe(mockDate, mockTimeStart, mockTimeEnd, mockTimeZoneInput, mockTimeZoneOutput,
                                            mockFormat) -> Tuple[str, str]:

        outputStart = ""
        outputEnd = ""

        dateTimeRegex = Ozone.getRegex(mockFormat.split('$')[1::])

        testData = re.match(dateTimeRegex, f"{mockDate} {mockTimeStart} - {mockTimeEnd}")

        testAmPmStart = ""
        testAmPmEnd = ""
        try:
            testAmPmStart = testData.group('ampm_start')
            testAmPmEnd = testData.group('ampm_end')
        except:
            pass

        testDateTimeStart = OzoneDate(
            testData.group('date_day'),
            testData.group('date_month'),
            testData.group('date_year'),
            testData.group('hours_start'),
            testData.group('minutes_start'),
            mockTimeZoneInput,
            ampm=testAmPmStart
        )

        testDateTimeEnd = OzoneDate(
            testData.group('date_day'),
            testData.group('date_month'),
            testData.group('date_year'),
            testData.group('hours_end'),
            testData.group('minutes_end'),
            mockTimeZoneInput,
            ampm=testAmPmEnd
        )

        outputStart = testDateTimeStart \
                     .asTimeZone(mockTimeZoneOutput) \
                     .strftime("%d.%m.%Y %H:%M") + f" {mockTimeZoneOutput}"

        outputEnd = testDateTimeEnd \
                          .asTimeZone(mockTimeZoneOutput) \
                          .strftime("%d.%m.%Y %H:%M") + f" {mockTimeZoneOutput}"

        return outputStart, outputEnd
