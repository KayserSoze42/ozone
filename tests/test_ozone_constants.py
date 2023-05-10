import re

from Ozone.Ozone import Ozone, Constants
from Ozone.testing_tools import OzoneTT


def test_regex_flow_with_valid_string_data(valid_string_dates) -> None:

    # Iterate over the list of valid string elements
    for genDate, genTime, genTimeZoneInput, genTimeZoneOutput, genFormat in valid_string_dates:

        # Build the string
        text = f"{genDate} {genTime} {genTimeZoneInput} {genTimeZoneOutput} {genFormat}"

        # Test for the content of the format passed in
        assert re.search(Constants.format.value, text)[0] == genFormat

        # Do necessary stripping
        strippedText = text.replace(genFormat, "").strip()

        timezones = re.findall(Constants.timezones.value, strippedText)[0]

        # Test for the content of the input time zone passed in
        assert timezones[0] == genTimeZoneInput

        # Test for the content of the output time zone passed in
        assert timezones[1] == genTimeZoneOutput

        # Strip some more
        strippedText = strippedText.replace(timezones[0], "")
        strippedText = strippedText.replace(timezones[1], "")
        strippedText = strippedText.strip()

        # Get the date and time regex for the current format
        genRegex = re.compile(Ozone.getRegex(genFormat.split("$")[1::]))

        # Test for the regex pattern to match passed date and time(the whole, remainder of the strippedText)
        assert strippedText == re.match(genRegex, strippedText)[0]


def test_regex_separated_logic_with_valid_string_data(valid_string_dates) -> None:

    # Iterate over the list of random valid string elements
    for genDate, genTime, genTimeZoneInput, genTimeZoneOutput, genFormat in valid_string_dates:

        # Test for the date and time regex to match for the passed date and time
        # Since this part is tricky, and it mostly depends on the format user passed, call Ozone.getRegex to help
        # Tl;dr I didn't want to create new lists for each of the formats
        genCommands = genFormat.split('$')[1::]
        dateTimeRegex = Ozone.getRegex(genCommands)
        dateTimeMatch = re.search(dateTimeRegex, f"{genDate} {genTime}")
        assert f"{genDate} {genTime}" == dateTimeMatch[0]

        # Test for the time zone regex to match the passed time zones
        # Oy bother, another trouble
        # Build string, since again, logic requires two zones to be passed at once
        timeZoneString = f" {genTimeZoneInput} {genTimeZoneOutput}"
        genTimeZones = re.findall(Constants.timezones.value, timeZoneString)[0]
        assert genTimeZoneInput == genTimeZones[0]
        assert genTimeZoneOutput == genTimeZones[1]

        # Test for the format regex to match the passed format
        assert genFormat == re.search(Constants.format.value, genFormat)[0]

def test_Mdy_regex_with_valid_string_data(valid_string_elements_Mdy_12_dmy_12) -> None:

    # Test that, basically, after finding the month using regex, it returns the same value as dmy formatted date
    for genMdyDate, gendmyDate in valid_string_elements_Mdy_12_dmy_12:

        testData = re.match(Constants.Mdy.value, genMdyDate)
        testDate = OzoneTT.getDateSTRP(gendmyDate, "%d.%m.%Y")

        testMonthValue = OzoneTT.getMonth(testData.group("date_month"))
        assert testDate.month == testMonthValue



def test_regex_flow_with_invalid_string_data(invalid_string_dates) -> None:

    # Iterate over the list of random invalid strings
    for invalidString in invalid_string_dates:

        # Test for the format to be None, since nothing is found
        assert re.search(Constants.format.value, invalidString) is None

        # Test for the input time zone to be None, since nothing is found, no need for stripping
        assert re.search(Constants.timezones.value, invalidString) is None

        # Test for the output time zone to be None, since nothing is found
        assert re.search(Constants.timezones.value, invalidString) is None


