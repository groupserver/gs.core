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
from md5 import new as md5_new
from string import printable
from time import asctime
from .utils import to_unicode_or_bust


def convert_int2b(num, alphabet, converted=[]):
    mod = num % len(alphabet)
    rem = num / len(alphabet)
    converted.append(alphabet[mod])
    if rem:
        retval = convert_int2b(rem, alphabet, converted)
    else:
        converted.reverse()
        retval = ''.join(converted)
    return retval


def convert_int2b62(num):
    alphabet = printable[:62]
    retval = convert_int2b(num, alphabet, [])
    return retval


def to_id(s):
    if not s:
        m = 'Nothing to convert to an ID'
        raise ValueError(m)
    md5n = md5_new(asctime() + to_unicode_or_bust(s))
    vNum = long(md5n.hexdigest(), 16)
    retval = str(convert_int2b62(vNum))
    return retval
