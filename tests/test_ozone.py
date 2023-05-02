import re
import pytest
import pytz

from Ozone.OzoneDate import OzoneDate
from Ozone.Ozone import Ozone


def test_ozonize_with_valid_string_data_and_mock_logic(valid_string_dates) -> None:

    # Iterate over the list of valid string elements
    for genDate, genTime, genTimeZoneInput, genTimeZoneOutput, genFormat in valid_string_dates:
        # Build the string
        testString = f"{genDate} {genTime} {genTimeZoneInput} {genTimeZoneOutput} {genFormat}"

        dateTimeRegex = Ozone.getRegex(genFormat.split('$')[1::])

        testData = re.match(dateTimeRegex, f"{genDate} {genTime}")

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
            genTimeZoneInput,
            ampm=testAmPm
        )

        expectedString = testDateTime\
                             .asTimeZone(genTimeZoneOutput)\
                             .strftime("%d.%m.%Y %H:%M") + f" {genTimeZoneOutput}"

        assert Ozone.ozonize(testString)[0] == expectedString


def test_ozonize_mock_logic_and_valid_string_dates_dmy_24(valid_string_dates_dmy_24) -> None:
    # Iterate over the list of valid string elements
    for genDate, genTime, genTimeZoneInput, genTimeZoneOutput, genFormat in valid_string_dates_dmy_24:
        # Build the string
        testString = f"{genDate} {genTime} {genTimeZoneInput} {genTimeZoneOutput} {genFormat}"

        dateTimeRegex = Ozone.getRegex(genFormat.split('$')[1::])

        testData = re.match(dateTimeRegex, f"{genDate} {genTime}")

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
            genTimeZoneInput,
            ampm=testAmPm
        )

        expectedString = testDateTime \
                             .asTimeZone(genTimeZoneOutput) \
                             .strftime("%d.%m.%Y %H:%M") + f" {genTimeZoneOutput}"

        assert Ozone.ozonize(testString)[0] == expectedString

def test_extract_methods_with_valid_string_data(valid_string_dates) -> None:
    for genDate, genTime, genTimeZoneInput, genTimeZoneOutput, genFormat in valid_string_dates:

        assert ("", genFormat) == Ozone.extractFormat(genFormat)

        timeZonesString = f"{genTimeZoneInput} {genTimeZoneOutput}"
        assert ("", genTimeZoneInput, genTimeZoneOutput) == Ozone.extractTimeZones(timeZonesString)

        dateTimeString = f"{genDate} {genTime}"
        dateTimeRegex = Ozone.getRegex(genFormat.split("$")[1::])


def test_ozonize_returns_empty(invalid_string_dates) -> None:

    # Iterate over the list of random invalid strings
    for invalidString in invalid_string_dates:

        with pytest.raises(Exception) as exception:

            # Test for the Ozone.ozonize to raise KeyError(?) since no valid data was found
            Ozone.ozonize(invalidString)

