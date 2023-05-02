from datetime import datetime
import pytz

from Ozone.OzoneDate import OzoneDate


def test_ozone_date_set_attributes(valid_dates) -> None:

    # Iterate over the list of valid date elements
    for day, month, year, hour, minute, timezone, ampm in valid_dates:

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

        # Construct an datetime object with generated data
        randomDateTime = datetime(
            randomOzoneDate.year,
            randomOzoneDate.month,
            randomOzoneDate.day,
            randomOzoneDate.hours,
            randomOzoneDate.minutes
        )

        # Test the initialization of the OzoneDate and confirm the attributes values

        # Test for the date to match value and type
        assert randomOzoneDate.day == int(day)
        assert randomOzoneDate.month == int(month)
        assert randomOzoneDate.year == int(year)

        # Set up the time
        if ampm == "pm":
            hour = 12 if int(hour) == 12 else int(hour) + 12
        elif ampm == "am":
            if int(hour) == 12:
                hour = 0

        # Test for the time to match value and type
        assert randomOzoneDate.hours == int(hour)
        assert randomOzoneDate.minutes == int(minute)
        assert randomOzoneDate.ampm == ampm

        # Set current time zone
        genTimeZone = pytz.timezone(timezone)

        # Test the time zone to match
        assert randomOzoneDate.timezone == genTimeZone

        # Build the string from the current data
        currentString = f"{day:02}.{month:02}.{year:04} {hour:02}:{minute:02} ({ampm}) {timezone}"

        # Test for the __str__ method
        assert str(randomOzoneDate) == currentString

        # Test for the datetime.astimezone to return the same as OzoneDate.asTimeZone
        assert genTimeZone.localize(randomDateTime) == randomOzoneDate.asTimeZone(timezone)



