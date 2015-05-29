#!/usr/bin/python
#
##
# Copyright (C) 2015 by Thomas Hemmingby Espe <thomas.espe@gmail.com>
#

import re


def convertsizes(st, to='mb', strip=True):
    """
    Converts from unit of bytes to another.
    Base is currently resticted to 1024

    :param str st: The value to convert from (eg. 5GB)
    :param str to: The unit to convert to
    :param strip: Whether to leave out (default) or append unit in return value
    :type strip: bool
    :return: A float or string (depending on whether strip is True or False)
    :rtype: float or str
    """
    legends = {'b': 0, 'kb': 1, 'mb': 2, 'gb': 3, 'tb': 4, 'pd': 5}
    res = 0

    st = st.lower()
    to = to.lower()

    # extract the digits
    n = float(re.findall('\d+\.?\d*', st)[0])
    # extract the denomination
    lt = ''.join([l for l in st if l.isalpha()])
    diff = legends[to] - legends[lt]

    if diff < 0:
        res = n * (1024**abs(diff))
    elif diff > 0:
        res = n / (1024**diff)
    else:
        # diff is 0, no conversion needed
        res = n

    if strip:
        return res
    else:
        return str(res).join(to)
