import re
import string

import pytz
import random

from Ozone.Ozone import Constants
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
        randomDate.strftime("%d/%m/%Y"),
        randomDate.strftime("%H"),
        randomTimeZoneInput,
        randomTimeZoneOutput,
        "$24"
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


def test_regex_valid_string_contents() -> None:

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

def test_regex_invalid_string_contents() -> None:

    # Iterate over the list of random invalid strings
    for invalidString in randomInvalidStrings:

        # Test for the format to be None, since nothing is found
        assert re.search(Constants.format.value, invalidString) is None

        # Test for the input time zone to be None, since nothing is found, no need for stripping
        assert re.search(Constants.timezones.value, invalidString) is None

        # Test for the output time zone to be None, since nothing is found
        assert re.search(Constants.timezones.value, invalidString) is None


