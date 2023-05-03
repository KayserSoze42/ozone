import random
import string
import pytest
import pytz

from datetime import datetime


validTimezones = [zone for zone in pytz.all_timezones]

@pytest.fixture
def valid_dates():
    # Generate valid data for testing
    validDates = []

    # Get time stamp for current time, rounded is good enough imho
    currentTimeStampRounded = round(datetime.now().timestamp())

    # Generate 100 valid sets of date elements
    for i in range(1, 101):
        # Get a random date between 1st of January 1970 and now (rounded)
        randomDate = datetime.fromtimestamp(random.randint(1, currentTimeStampRounded))

        # Get random time zone
        randomTimeZone = validTimezones[random.randint(0, len(validTimezones) - 1)]

        # Append "20.04.2020 04:20 PM CET" type date elements to valid date list
        validDates.append([
            randomDate.strftime("%d"),
            randomDate.strftime("%m"),
            randomDate.strftime("%Y"),
            randomDate.strftime("%I"),
            randomDate.strftime("%M"),
            randomTimeZone,
            randomDate.strftime("%p").lower()
        ])

    return validDates


@pytest.fixture
def valid_string_dates_dmy_12():
    # Re/set valid data for testing
    validStrings = []

    # Get time stamp for current time, rounded is good enough imho
    currentTimeStampRounded = round(datetime.now().timestamp())

    # Generate 100 valid sets of $dmy$24 string elements
    for i in range(1, 101):
        # Get a random date between 1st of January 1970 and now (rounded)
        randomDate = datetime.fromtimestamp(random.randint(1, currentTimeStampRounded))

        # Get random time zones for input and output
        randomTimeZoneInput = validTimezones[random.randint(0, len(validTimezones) - 1)]
        randomTimeZoneOutput = validTimezones[random.randint(0, len(validTimezones) - 1)]

        # Append "20.04.2020 4:20 PM ETC GMT $12" type string elements to valid string list
        validStrings.append([
            randomDate.strftime("%d.%m.%Y"),
            randomDate.strftime("%I:%M %p"),
            randomTimeZoneInput,
            randomTimeZoneOutput,
            "$12"
        ])

    return validStrings


@pytest.fixture
def valid_string_dates_dmy_24():
    # Re/set valid data for testing
    validStrings = []

    # Get time stamp for current time, rounded is good enough imho
    currentTimeStampRounded = round(datetime.now().timestamp())

    # Generate 100 valid sets of $dmy$24 string elements
    for i in range(1, 101):
        # Get a random date between 1st of January 1970 and now (rounded)
        randomDate = datetime.fromtimestamp(random.randint(1, currentTimeStampRounded))

        # Get random time zones for input and output
        randomTimeZoneInput = validTimezones[random.randint(0, len(validTimezones) - 1)]
        randomTimeZoneOutput = validTimezones[random.randint(0, len(validTimezones) - 1)]

        # Append "20.04.2020 16:20 ETC GMT $24" type string elements to valid string list
        validStrings.append([
            randomDate.strftime("%d.%m.%Y"),
            randomDate.strftime("%H:%M"),
            randomTimeZoneInput,
            randomTimeZoneOutput,
            "$24"
        ])

    return validStrings

@pytest.fixture
def valid_string_dates_mdy_12():
    # Re/set valid data for testing
    validStrings = []

    # Get time stamp for current time, rounded is good enough imho
    currentTimeStampRounded = round(datetime.now().timestamp())

    # Generate 100 valid sets of $dmy$24 string elements
    for i in range(1, 101):
        # Get a random date between 1st of January 1970 and now (rounded)
        randomDate = datetime.fromtimestamp(random.randint(1, currentTimeStampRounded))

        # Get random time zones for input and output
        randomTimeZoneInput = validTimezones[random.randint(0, len(validTimezones) - 1)]
        randomTimeZoneOutput = validTimezones[random.randint(0, len(validTimezones) - 1)]

        # Append "04.20.2020 4:20 PM ETC GMT $mdy$12" type string elements to valid string list
        validStrings.append([
            randomDate.strftime("%m.%d.%Y"),
            randomDate.strftime("%I:%M %p"),
            randomTimeZoneInput,
            randomTimeZoneOutput,
            "$mdy$12"
        ])

    return validStrings


@pytest.fixture
def valid_string_dates_mdy_24():
    # Re/set valid data for testing
    validStrings = []

    # Get time stamp for current time, rounded is good enough imho
    currentTimeStampRounded = round(datetime.now().timestamp())

    # Generate 100 valid sets of $dmy$24 string elements
    for i in range(1, 101):
        # Get a random date between 1st of January 1970 and now (rounded)
        randomDate = datetime.fromtimestamp(random.randint(1, currentTimeStampRounded))

        # Get random time zones for input and output
        randomTimeZoneInput = validTimezones[random.randint(0, len(validTimezones) - 1)]
        randomTimeZoneOutput = validTimezones[random.randint(0, len(validTimezones) - 1)]

        # Append "04.20.2020 16:20 ETC GMT $mdy$24" type string elements to valid string list
        validStrings.append([
            randomDate.strftime("%m.%d.%Y"),
            randomDate.strftime("%H:%M"),
            randomTimeZoneInput,
            randomTimeZoneOutput,
            "$mdy$24"
        ])

    return validStrings


@pytest.fixture
def valid_string_dates_ydm_12():
    # Re/set valid data for testing
    validStrings = []

    # Get time stamp for current time, rounded is good enough imho
    currentTimeStampRounded = round(datetime.now().timestamp())

    # Generate 100 valid sets of $dmy$24 string elements
    for i in range(1, 101):
        # Get a random date between 1st of January 1970 and now (rounded)
        randomDate = datetime.fromtimestamp(random.randint(1, currentTimeStampRounded))

        # Get random time zones for input and output
        randomTimeZoneInput = validTimezones[random.randint(0, len(validTimezones) - 1)]
        randomTimeZoneOutput = validTimezones[random.randint(0, len(validTimezones) - 1)]

        # Append "2020.20.04 4:20 PM ETC GMT $ydm$12" type string elements to valid string list
        validStrings.append([
            randomDate.strftime("%Y.%d.%m"),
            randomDate.strftime("%I:%M %p"),
            randomTimeZoneInput,
            randomTimeZoneOutput,
            "$ydm$12"
        ])

    return validStrings


@pytest.fixture
def valid_string_dates_ydm_24():
    # Re/set valid data for testing
    validStrings = []

    # Get time stamp for current time, rounded is good enough imho
    currentTimeStampRounded = round(datetime.now().timestamp())

    # Generate 100 valid sets of $dmy$24 string elements
    for i in range(1, 101):
        # Get a random date between 1st of January 1970 and now (rounded)
        randomDate = datetime.fromtimestamp(random.randint(1, currentTimeStampRounded))

        # Get random time zones for input and output
        randomTimeZoneInput = validTimezones[random.randint(0, len(validTimezones) - 1)]
        randomTimeZoneOutput = validTimezones[random.randint(0, len(validTimezones) - 1)]

        # Append "2020.20.04 16:20 ETC GMT $ydm$24" type string elements to valid string list
        validStrings.append([
            randomDate.strftime("%Y.%d.%m"),
            randomDate.strftime("%H:%M"),
            randomTimeZoneInput,
            randomTimeZoneOutput,
            "$ydm$24"
        ])

    return validStrings

@pytest.fixture
def valid_string_dates_ymd_12():
    # Re/set valid data for testing
    validStrings = []

    # Get time stamp for current time, rounded is good enough imho
    currentTimeStampRounded = round(datetime.now().timestamp())

    # Generate 100 valid sets of $dmy$24 string elements
    for i in range(1, 101):
        # Get a random date between 1st of January 1970 and now (rounded)
        randomDate = datetime.fromtimestamp(random.randint(1, currentTimeStampRounded))

        # Get random time zones for input and output
        randomTimeZoneInput = validTimezones[random.randint(0, len(validTimezones) - 1)]
        randomTimeZoneOutput = validTimezones[random.randint(0, len(validTimezones) - 1)]

        # Append "2020.04.20 4:20 PM ETC GMT $ymd$12" type string elements to valid string list
        validStrings.append([
            randomDate.strftime("%Y.%m.%d"),
            randomDate.strftime("%I:%M %p"),
            randomTimeZoneInput,
            randomTimeZoneOutput,
            "$ymd$12"
        ])

    return validStrings


@pytest.fixture
def valid_string_dates_ymd_24():
    # Re/set valid data for testing
    validStrings = []

    # Get time stamp for current time, rounded is good enough imho
    currentTimeStampRounded = round(datetime.now().timestamp())

    # Generate 100 valid sets of $dmy$24 string elements
    for i in range(1, 101):
        # Get a random date between 1st of January 1970 and now (rounded)
        randomDate = datetime.fromtimestamp(random.randint(1, currentTimeStampRounded))

        # Get random time zones for input and output
        randomTimeZoneInput = validTimezones[random.randint(0, len(validTimezones) - 1)]
        randomTimeZoneOutput = validTimezones[random.randint(0, len(validTimezones) - 1)]

        # Append "2020.04.20 16:20 ETC GMT $ymd$24" type string elements to valid string list
        validStrings.append([
            randomDate.strftime("%Y.%m.%d"),
            randomDate.strftime("%H:%M"),
            randomTimeZoneInput,
            randomTimeZoneOutput,
            "$ymd$24"
        ])

    return validStrings


@pytest.fixture
def valid_string_dates():

    # Generate valid data for testing
    validStrings = []

    # Get time stamp for current time, rounded is good enough imho
    currentTimeStampRounded = round(datetime.now().timestamp())

    # Generate 100 valid sets of string elements
    for i in range(1, 101):
        # Get a random date between 1st of January 1970 and now (rounded)
        randomDate = datetime.fromtimestamp(random.randint(1, currentTimeStampRounded))

        # Get random time zones for input and output
        randomTimeZoneInput = validTimezones[random.randint(0, len(validTimezones) - 1)]
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

    return validStrings

@pytest.fixture
def invalid_string_dates():
    # Generate invalid data for testing
    randomInvalidStrings = []

    # Generate 200 invalid sets of strings
    for i in range(1, 201):
        # Generate random string using letters only, length of 25-34 characters
        randomInvalidStrings.append(
            ''.join(random.choice(string.ascii_letters) for _ in range(random.randint(25, 35)))
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

    return randomInvalidStrings