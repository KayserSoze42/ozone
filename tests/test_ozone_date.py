from datetime import datetime
import random

import pytz

from Ozone.OzoneDate import OzoneDate



# Generate valid data for testing
validTimezones = [zone for zone in pytz.all_timezones]
validDates = []

# Get time stamp for current time, rounded is good enough imho
currentTimeStampRounded = round(datetime.now().timestamp())

# Generate 100 valid sets of date elements
for i in range(1, 101):

    # Get a random date between 1st of January 1970 and now (rounded)
    randomDate = datetime.fromtimestamp(random.randint(1, currentTimeStampRounded))

    # Get random time zone
    randomTimeZone = validTimezones[random.randint(0, len(validTimezones)-1)]

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


def test_ozone_date_set_attributes() -> None:

    # Iterate over the list of valid date elements
    for day, month, year, hour, minute, timezone, ampm in validDates:

        # Construct an OzoneDate object with generated data
        randomOzoneDate = OzoneDate(
            day,
            month,
            year,
            hour,
            minute,
            timezone,
            ampm
        )

        # Test the initialization of the OzoneDate and confirm the attributes values
        assert randomOzoneDate.day == int(day)
        assert randomOzoneDate.month == int(month)
        assert randomOzoneDate.year == int(year)

        # Set up the time
        if ampm == "pm":
            hour = 12 if int(hour) == 12 else int(hour) + 12
        elif ampm == "am":
            if int(hour) == 12:
                hour = 0

        # Test for the time set
        assert randomOzoneDate.hours == int(hour)

        # Test for the rest
        assert randomOzoneDate.minutes == int(minute)
        assert randomOzoneDate.timezone == pytz.timezone(timezone)
        assert randomOzoneDate.ampm == ampm

        # Build the string from the current data
        currentString = f"{day:02}.{month:02}.{year:04} {hour:02}:{minute:02} ({ampm}) {timezone}"

        # Test for the __str__ method
        assert str(randomOzoneDate) == currentString