#!/usr/bin/env python3
#
##
# Copyright (C) 2015 by Thomas Hemmingby Espe <thomas.espe@gmail.com>
#


def all_but_last(s, sep=' '):
    """
    Returns all but the last element of a string after split on sep

    :param s str: The string to operate on
    :param sep str: The separator to use for split, default ' '
    :return: A string with all but the last element of the input string
    :rtype: string
    """
    return sep.join(s.split(sep)[0:-1])
