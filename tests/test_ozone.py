import re
from typing import Tuple

import pytest
import pytz

from Ozone.OzoneDate import OzoneDate
from Ozone.Ozone import Ozone


def generate_mock_ozone_start_time_only(mockDate, mockTime, mockTimeZoneInput, mockTimeZoneOutput, mockFormat) -> str:
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

def test_ozonize_mock_logic_and_valid_string_dates_dmy_12(valid_string_dates_dmy_12) -> None:
    # Iterate over the list of valid string elements
    for testDate, testTime, testTimeZoneInput, testTimeZoneOutput, testFormat in valid_string_dates_dmy_12:
        # Build the string
        testString = f"{testDate} {testTime} {testTimeZoneInput} {testTimeZoneOutput} {testFormat}"

        expectedString = generate_mock_ozone_start_time_only(
            testDate,
            testTime,
            testTimeZoneInput,
            testTimeZoneOutput,
            testFormat
        )

        assert Ozone.ozonize(testString)[0] == expectedString


def test_ozonize_mock_logic_and_valid_string_dates_dmy_24(valid_string_dates_dmy_24) -> None:
    # Iterate over the list of valid string elements
    for testDate, testTime, testTimeZoneInput, testTimeZoneOutput, testFormat in valid_string_dates_dmy_24:
        # Build the string
        testString = f"{testDate} {testTime} {testTimeZoneInput} {testTimeZoneOutput} {testFormat}"

        expectedString = generate_mock_ozone_start_time_only(
            testDate,
            testTime,
            testTimeZoneInput,
            testTimeZoneOutput,
            testFormat
        )

        assert Ozone.ozonize(testString)[0] == expectedString


def test_ozonize_mock_logic_and_valid_string_dates_mdy_12(valid_string_dates_mdy_12) -> None:
    # Iterate over the list of valid string elements
    for testDate, testTime, testTimeZoneInput, testTimeZoneOutput, testFormat in valid_string_dates_mdy_12:
        # Build the string
        testString = f"{testDate} {testTime} {testTimeZoneInput} {testTimeZoneOutput} {testFormat}"

        expectedString = generate_mock_ozone_start_time_only(
            testDate,
            testTime,
            testTimeZoneInput,
            testTimeZoneOutput,
            testFormat
        )

        assert Ozone.ozonize(testString)[0] == expectedString


def test_ozonize_mock_logic_and_valid_string_dates_mdy_24(valid_string_dates_mdy_24) -> None:
    # Iterate over the list of valid string elements
    for testDate, testTime, testTimeZoneInput, testTimeZoneOutput, testFormat in valid_string_dates_mdy_24:
        # Build the string
        testString = f"{testDate} {testTime} {testTimeZoneInput} {testTimeZoneOutput} {testFormat}"

        expectedString = generate_mock_ozone_start_time_only(
            testDate,
            testTime,
            testTimeZoneInput,
            testTimeZoneOutput,
            testFormat
        )

        assert Ozone.ozonize(testString)[0] == expectedString


def test_ozonize_mock_logic_and_valid_string_dates_ydm_12(valid_string_dates_ydm_12) -> None:
    # Iterate over the list of valid string elements
    for testDate, testTime, testTimeZoneInput, testTimeZoneOutput, testFormat in valid_string_dates_ydm_12:
        # Build the string
        testString = f"{testDate} {testTime} {testTimeZoneInput} {testTimeZoneOutput} {testFormat}"

        expectedString = generate_mock_ozone_start_time_only(
            testDate,
            testTime,
            testTimeZoneInput,
            testTimeZoneOutput,
            testFormat
        )

        assert Ozone.ozonize(testString)[0] == expectedString


def test_ozonize_mock_logic_and_valid_string_dates_ydm_24(valid_string_dates_ydm_24) -> None:
    # Iterate over the list of valid string elements
    for testDate, testTime, testTimeZoneInput, testTimeZoneOutput, testFormat in valid_string_dates_ydm_24:
        # Build the string
        testString = f"{testDate} {testTime} {testTimeZoneInput} {testTimeZoneOutput} {testFormat}"

        expectedString = generate_mock_ozone_start_time_only(
            testDate,
            testTime,
            testTimeZoneInput,
            testTimeZoneOutput,
            testFormat
        )

        assert Ozone.ozonize(testString)[0] == expectedString


def test_ozonize_mock_logic_and_valid_string_dates_ymd_12(valid_string_dates_ymd_12) -> None:
    # Iterate over the list of valid string elements
    for testDate, testTime, testTimeZoneInput, testTimeZoneOutput, testFormat in valid_string_dates_ymd_12:
        # Build the string
        testString = f"{testDate} {testTime} {testTimeZoneInput} {testTimeZoneOutput} {testFormat}"

        expectedString = generate_mock_ozone_start_time_only(
            testDate,
            testTime,
            testTimeZoneInput,
            testTimeZoneOutput,
            testFormat
        )

        assert Ozone.ozonize(testString)[0] == expectedString


def test_ozonize_mock_logic_and_valid_string_dates_ymd_24(valid_string_dates_ymd_24) -> None:
    # Iterate over the list of valid string elements
    for testDate, testTime, testTimeZoneInput, testTimeZoneOutput, testFormat in valid_string_dates_ymd_24:
        # Build the string
        testString = f"{testDate} {testTime} {testTimeZoneInput} {testTimeZoneOutput} {testFormat}"

        expectedString = generate_mock_ozone_start_time_only(
            testDate,
            testTime,
            testTimeZoneInput,
            testTimeZoneOutput,
            testFormat
        )

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

