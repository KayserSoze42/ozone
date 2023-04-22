import re, pytz, calendar
from datetime import datetime
from typing import Tuple


class Ozone:

    def ozonize(user_input: str) -> Tuple[str, str]:
        #                                     DATE                                                                                      TIME                          TIMEZONES      FORMAT
        REGEX = r"\s*(\d{1,4}|\D{3,15})\s*[\./-]*(\d{1,2})\s*[\./\-,]*(\d{1,4}) (\d{1,2})\s?:?\s?(\d{0,2})\s*([aApP]?[mM]?)\s*[->]?\s*(\d{0,2}):?(\d{0,2})\s*([aApP]?[mM]?) (\D\S*) (\D\S*)\s*(\$?.*)\s*"

        output_start = ""
        output_end = ""

        data = re.match(REGEX, user_input)

        try:

            date_a = data[1].strip()
            date_b = data[2].strip()
            date_c = data[3].strip()

            start_time_hours = data[4]
            start_time_minutes = data[5]
            start_time_ampm = data[6]

            end_time_hours = data[7]
            end_time_minutes = data[8]
            end_time_ampm = data[9]

            input_zone = data[10]
            output_zone = data[11]

            regex_format = data[12]

        except Exception as e:
            start_time_hours = 16
            start_time_minutes = 0
            end_time_hours = -1
            end_time_minutes = ""
            input_zone = "CET"
            output_zone = "GMT"
            pass

        start_datetime_hours = start_time_hours if start_time_hours != "" else 16
        start_datetime_minutes = start_time_minutes if start_time_minutes != "" else 0

        end_datetime_hours = end_time_hours if end_time_hours != "" else -1
        end_datetime_minutes = end_time_minutes if end_time_minutes != "" else 0

        input_timezone = pytz.timezone(input_zone)
        output_timezone = pytz.timezone(output_zone)

        input_datetime_year = datetime.now().year
        input_datetime_month = datetime.now().month
        input_datetime_day = datetime.now().day

        input_datetime = None
        output_datetime = None

        try:

            if regex_format != "":

                regex_array = regex_format.split("$")[1::]

                for cmd in regex_array:

                    if cmd == "12":

                        if start_time_ampm.lower() == "pm":
                            start_datetime_hours = int(start_time_hours) + 12

                        if start_time_ampm.lower() == "am":
                            start_datetime_hours = int(start_time_hours)

                        if end_time_ampm.lower() == "pm":
                            end_datetime_hours = int(end_time_hours) + 12 if end_time_hours != "" else 16

                        if end_time_ampm.lower() == "am":
                            end_datetime_hours = int(end_time_hours) if end_time_hours != "" else 16

                    elif cmd == "24":

                        start_datetime_hours = int(start_time_hours)

                    elif cmd == "ymd":

                        input_datetime_year = date_a
                        input_datetime_month = date_b
                        input_datetime_day = date_c

                    elif cmd == "ydm":

                        input_datetime_year = date_a
                        input_datetime_month = date_c
                        input_datetime_day = date_b

                    elif cmd == "dmy":

                        input_datetime_year = date_c
                        input_datetime_month = date_b
                        input_datetime_day = date_a

                    elif cmd == "mdy":

                        input_datetime_year = date_c
                        input_datetime_month = date_a
                        input_datetime_day = date_b

                    elif cmd == "Mdy":

                        if len(date_a) == 3:
                            input_datetime_month = list(calendar.month_abbr).index(date_a)

                        else:
                            input_datetime_month = list(calendar.month_name).index(date_a)

                        input_datetime_day = date_b
                        input_datetime_year = date_c

                input_datetime = datetime(
                    int(input_datetime_year),
                    int(input_datetime_month),
                    int(input_datetime_day),
                    int(start_datetime_hours),
                    int(start_datetime_minutes),

                )

                input_localized = input_timezone.localize(input_datetime)

                output_datetime = input_localized.astimezone(output_timezone)

                output_start += output_datetime.strftime("%d.%m.%Y %H:%M ") + str(output_timezone)

                if end_datetime_hours != -1:

                    input_end_datetime = datetime(
                        int(input_datetime_year),
                        int(input_datetime_month),
                        int(input_datetime_day),
                        int(end_datetime_hours),
                        int(end_datetime_minutes)
                    )

                    input_end_localized = input_timezone.localize(input_end_datetime)

                    output_datetime_end = input_end_localized.astimezone(input_timezone)

                    output_end += output_datetime_end.strftime("%d.%m.%Y %H:%M ") + str(output_timezone)

            else:

                start_datetime_hours = start_time_hours
                end_datetime_hours = end_time_hours

                input_datetime = datetime(
                    int(date_c),
                    int(date_b),
                    int(date_a),
                    int(start_datetime_hours),
                    int(start_datetime_minutes),

                )

                input_localized = input_timezone.localize(input_datetime)

                output_datetime = input_localized.astimezone(output_timezone)

                output_start += output_datetime.strftime("%d.%m.%Y %H:%M ") + str(output_timezone)

                if end_datetime_hours != -1:

                    input_end_datetime = datetime(
                        int(date_c),
                        int(date_b),
                        int(date_a),
                        int(end_datetime_hours),
                        int(end_datetime_minutes)
                    )

                    input_end_localized = input_timezone.localize(input_end_datetime)

                    output_datetime_end = input_end_localized.astimezone(input_timezone)

                    output_end += output_datetime_end.strftime("%d.%m.%Y %H:%M ") + str(output_timezone)

        except Exception as e:
            output_start = datetime.now().strftime("%d.%m.%Y %H:%M ") + ":)"
            pass

        return output_start,  output_end
