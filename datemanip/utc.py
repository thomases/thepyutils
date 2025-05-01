#!/usr/bin/env python3

from datetime import datetime
from datetime import parser
import pytz



def convert_to_utc(fromtzone: str, fromdate: str, pr : bool = False) -> datetime.datetime:
    """
    Convert time and date from a timezone into UTC

    :param fromtzone: timezone to convert from
    :param fromdate: date/time to convert from
    :param pr: wether to print the result in addition to returning it
    :returns: datetime object with time/date in UTC
    """
    dt = parser.parse(fromdate)
    tzone = pytz.timezone(fromtzone)

    local_dt = tzone.localize(dt)
    utc_dt = local_dt.astimezone(pytz.utc)

    print(utc_dt.isoformat()) if pr

    return utc_dt


