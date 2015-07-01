#!/usr/bin/python
#
##
# Copyright (C) 2015 by Thomas Hemmingby Espe <thomas.espe@gmail.com>
#


def all_but_last(s, sep=' '):
    """Returns all but the last element of a string after split on sep"""
    return sep.join(s.split(sep)[0:-1])
