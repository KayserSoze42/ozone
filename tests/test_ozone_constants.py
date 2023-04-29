import re
import string

import pytz
import random

from Ozone.Ozone import Ozone, Constants
from datetime import datetime

# Generate valid data for testing
validTimezones = [zone for zone in pytz.all_timezones]
validStrings = []

# Get time stamp for current time, rounded is good enough imho
currentTimeStampRounded = round(datetime.now().timestamp())

# Generate 100 valid sets of string elements
for i in range(1, 101):

    # Get a random date between 1st of January 1970 and now (rounded)
    randomDate = datetime.fromtimestamp(random.randint(1, currentTimeStampRounded))

    # Get random time zones for input and output
    randomTimeZoneInput = validTimezones[random.randint(0, len(validTimezones)-1)]
    randomTimeZoneOutput = validTimezones[random.randint(0, len(validTimezones) - 1)]

    # Append "20.04.2020 4:20 PM ETC GMT $12" type string elements to valid string list
    validStrings.append([
        randomDate.strftime("%d.%m.%Y"),
        randomDate.strftime("%I:%M %p"),
        randomTimeZoneInput,
        randomTimeZoneOutput,
        "$12"
    ])

    # Append "20/04/2020 16:00 ETC GMT $24" type string elements to valid string list
    validStrings.append([
        randomDate.strftime("%d/%m/%Y"),
        randomDate.strftime("%H:%M"),
        randomTimeZoneInput,
        randomTimeZoneOutput,
        "$24"
    ])

    # Append "20.04.2020 16 ETC GMT $24" type string elements to valid string list
    validStrings.append([
        randomDate.strftime("%d.%m.%Y"),
        randomDate.strftime("%H"),
        randomTimeZoneInput,
        randomTimeZoneOutput,
        "$24"
    ])

    # Append "04/20/2020 16 ETC GMT $24$mdy" type string elements to valid string list
    validStrings.append([
        randomDate.strftime("%m/%d/%Y"),
        randomDate.strftime("%H"),
        randomTimeZoneInput,
        randomTimeZoneOutput,
        "$24$mdy"
    ])

    # Append "2020-20-04 4-5 ETC GMT $12$ydm" type string elements to valid string list
    validStrings.append([
        randomDate.strftime("%y-%d-%m"),
        randomDate.strftime("%H"),
        randomTimeZoneInput,
        randomTimeZoneOutput,
        "$12$ydm"
    ])

    # Append "04/20/2020 16 ETC GMT $24$mdy" type string elements to valid string list
    validStrings.append([
        randomDate.strftime("%m/%d/%Y"),
        randomDate.strftime("%H"),
        randomTimeZoneInput,
        randomTimeZoneOutput,
        "$24$mdy"
    ])

# Generate invalid data for testing
randomInvalidStrings = []

# Generate 100 invalid sets of strings
for i in range(1, 101):

    # Generate random string using letters only, length of 25-34 characters
    randomInvalidStrings.append(
        ''.join(random.choice(string.ascii_letters) for _ in range(random.randint(25,35)))
    )

    # Generate random string using lowercase letters only, length of 25-34 characters
    randomInvalidStrings.append(
        ''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(25, 35)))
    )

    # Generate random string using uppercase letters only, length of 25-34 characters
    randomInvalidStrings.append(
        ''.join(random.choice(string.ascii_uppercase) for _ in range(random.randint(25, 35)))
    )

    # Generate random string using digits only, length of 25-34 characters(digits?)
    randomInvalidStrings.append(
        ''.join(random.choice(string.digits) for _ in range(random.randint(25, 35)))
    )


def test_regex_flow_with_valid_string_data() -> None:

    # Iterate over the list of valid string elements
    for genDate, genTime, genTimeZoneInput, genTimeZoneOutput, genFormat in validStrings:

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


def test_regex_separated_logic_with_valid_string_data() -> None:

    # Iterate over the list of random valid string elements
    for genDate, genTime, genTimeZoneInput, genTimeZoneOutput, genFormat in validStrings:

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




def test_regex_flow_with_invalid_string_data() -> None:

    # Iterate over the list of random invalid strings
    for invalidString in randomInvalidStrings:

        # Test for the format to be None, since nothing is found
        assert re.search(Constants.format.value, invalidString) is None

        # Test for the input time zone to be None, since nothing is found, no need for stripping
        assert re.search(Constants.timezones.value, invalidString) is None

        # Test for the output time zone to be None, since nothing is found
        assert re.search(Constants.timezones.value, invalidString) is None


