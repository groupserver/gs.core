# -*- coding: utf-8 -*-
##############################################################################
#
# Copyright © 2014 OnlineGroups.net and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
from __future__ import unicode_literals
import sys
if (sys.version_info < (3, )):
    longint = long
else:
    longint = int
from hashlib import md5
from string import printable
from time import asctime
from .utils import to_unicode_or_bust


def convert_int2b(num, alphabet, converted=[]):
    '''Convert n integer to a string using the alphabet as the base'''
    mod = num % len(alphabet)
    rem = num // len(alphabet)
    converted.append(alphabet[mod])
    if rem:
        retval = convert_int2b(rem, alphabet, converted)
    else:
        converted.reverse()
        retval = ''.join(converted)
    return retval


def convert_int2b62(num):
    '''Convert an integer to a base-62 encoded string.

:param int num: The number to convert.
:returns: A base-62 encoded string.
:rtype: str
'''
    alphabet = printable[:62]
    retval = convert_int2b(num, alphabet, [])
    return retval


def to_id(s):
    '''  Create a random identifier, using a string as a seed.

:param str s: The string to be used as a seed.
:return: A base-62 encoded string, 22 characters long.
:rtype: str

Many things require unique identifiers, such as users, posts, topics,
password-reset links, and email-verification links. The ``to_id`` function
takes a string and converts it to a fixed-length base-62 encoded string
that can be used as an ID.


Example:

    Create a verification identifier for an email address::

        email = emailUser.get_delivery_addresses()[0]
        verificationId = to_id(email)
'''
    if not s:
        m = 'Nothing to convert to an ID'
        raise ValueError(m)
    st = to_unicode_or_bust(asctime()) + to_unicode_or_bust(s)
    md5n = md5()
    md5n.update(st.encode('utf-8', 'ignore'))
    vNum = longint(md5n.hexdigest(), 16)
    retval = str(convert_int2b62(vNum))
    return retval
