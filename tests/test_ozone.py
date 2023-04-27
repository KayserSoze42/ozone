import re
import string
import random
import pytz

from datetime import datetime

from Ozone.OzoneDate import OzoneDate

from Ozone.Ozone import Ozone

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

    # Append "2020-20-04 4 ETC GMT $12$ydm" type string elements to valid string list
    validStrings.append([
        randomDate.strftime("%y-%d-%m"),
        randomDate.strftime("%I %p"),
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


def test_ozonize_with_valid_string_data_and_mock_logic() -> None:

    # Iterate over the list of valid string elements
    for genDate, genTime, genTimeZoneInput, genTimeZoneOutput, genFormat in validStrings:
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
        ).asTimeZone(genTimeZoneOutput)

        expectedString = testDateTime.strftime("%d.%m.%Y %H:%M ") + f" {genTimeZoneOutput}"

        assert expectedString == Ozone.ozonize(testString)






def test_ozonize_returns_empty() -> None:

    # Iterate over the list of random invalid strings
    for invalidString in randomInvalidStrings:

        # Test for the Ozone.ozonize to return ('','') since nothing is found (nothing was** written as well)
        assert Ozone.ozonize(invalidString) == ('', '')

