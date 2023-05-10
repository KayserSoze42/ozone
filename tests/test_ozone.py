import pytest

from Ozone.Ozone import Ozone
from Ozone.testing_tools import OzoneTT

def test_ozonize_mock_logic_and_valid_string_dates_dmy_12(valid_string_dates_dmy_12) -> None:
    # Iterate over the list of valid string elements
    for testDate, testTime, testTimeZoneInput, testTimeZoneOutput, testFormat in valid_string_dates_dmy_12:
        # Build the string
        testString = f"{testDate} {testTime} {testTimeZoneInput} {testTimeZoneOutput} {testFormat}"

        expectedString = OzoneTT.generate_mock_ozone_start_time_only(
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

        expectedString = OzoneTT.generate_mock_ozone_start_time_only(
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

        expectedString = OzoneTT.generate_mock_ozone_start_time_only(
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

        expectedString = OzoneTT.generate_mock_ozone_start_time_only(
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

        expectedString = OzoneTT.generate_mock_ozone_start_time_only(
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

        expectedString = OzoneTT.generate_mock_ozone_start_time_only(
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

        expectedString = OzoneTT.generate_mock_ozone_start_time_only(
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

        expectedString = OzoneTT.generate_mock_ozone_start_time_only(
            testDate,
            testTime,
            testTimeZoneInput,
            testTimeZoneOutput,
            testFormat
        )

        assert Ozone.ozonize(testString)[0] == expectedString

def test_ozonize_mock_logic_and_valid_string_dates_Mdy_12(valid_string_dates_Mdy_12) -> None:
    # Iterate over the list of valid string elements
    for testDate, testTime, testTimeZoneInput, testTimeZoneOutput, testFormat in valid_string_dates_Mdy_12:
        # Build the string
        testString = f"{testDate} {testTime} {testTimeZoneInput} {testTimeZoneOutput} {testFormat}"

        expectedString = OzoneTT.generate_mock_ozone_start_time_only(
            testDate,
            testTime,
            testTimeZoneInput,
            testTimeZoneOutput,
            testFormat
        )

        assert Ozone.ozonize(testString)[0] == expectedString


def test_ozonize_mock_logic_and_valid_string_dates_dmy_12_timeframe(valid_string_dates_dmy_12_timeframe) -> None:

    for testDate, testTimeStart, testTimeEnd, testTimeZoneInput, testTimeZoneOutput, testFormat in valid_string_dates_dmy_12_timeframe:

        testString = f"{testDate} {testTimeStart} - {testTimeEnd} {testTimeZoneInput} {testTimeZoneOutput} {testFormat}"

        expectedStrings = OzoneTT.generate_mock_ozone_timeframe(
            testDate,
            testTimeStart,
            testTimeEnd,
            testTimeZoneInput,
            testTimeZoneOutput,
            testFormat
        )

        assert Ozone.ozonize(testString) == expectedStrings


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

