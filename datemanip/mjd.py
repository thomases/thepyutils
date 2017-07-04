#!/usr/bin/python


import datetime
import jdcal


def mjd2000_to_date(mjd):
    """
    Convert a MJD2000 date to a datetime object
    
    :param mjd float: the MJD2000 date to convert
    :return: a datetime object
    :rtype: datetime.datetime
    """
    dat = jdcal.jd2gcal(jdcal.MJD_0 + jdcal.MJD_JD2000, mjd)
    tm = __mjd2000_fraction_to_timedelta(dat[3])
        
    return datetime.datetime(dat[0], dat[1], dat[2],
                             *__split_timedelta(tm))
                             

def mjd2000_to_ISO(mjd):
    """
    Convert a MJD2000 date into an ISO8601 string

    :param mjd float: the MJD2000 date to convert
    :return: a string in ISO8601 format
    :rtype: string
    """
    return mjd2000_to_date(mjd).isoformat()


def mjd2000_strftime(mjd, fmt):
    """
    Convert a MJD2000 date into a date string according to fmt

    :param mjd float: the MJD2000 date to convert
    :paramt fmt string: strftime() style string
    """
    return mjd2000_to_date(mjd).strftime(fmt)


def __mjd2000_fraction_to_timedelta(mjt):
    """
    Takes a fraction of a day and returns the time in a HH:MM:ss.ms format

    :param mjt int: The time to convert to a timedelta
    :return: a timedelta object
    """
    return datetime.timedelta(mjt)


def __split_timedelta(tm):
    """
    Split a timedelta into a tuple of (hours, minutes, seconds, microseconds)

    :param tm datetime.timedelta: the timedelta object to split
    :return: a tuple
    :rtype: tuple
    """
    s = tm.seconds
    hours = s // 3600

    s = s - (hours * 3600)
    minutes = s // 60

    seconds = s - (minutes * 60)
    
    return (hours, minutes, seconds, tm.microseconds)
