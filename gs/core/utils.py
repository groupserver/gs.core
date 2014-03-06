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
from datetime import datetime
from pytz import utc as UTC


def to_ascii(obj):
    u = to_unicode_or_bust(obj)
    retval = u.encode('ascii', 'ignore')
    return retval


def to_unicode_or_bust(obj, encoding='utf-8'):
    'http://farmdev.com/talks/unicode/'
    if isinstance(obj, basestring):
        if not isinstance(obj, unicode):
            obj = unicode(obj, encoding)
    return obj


def curr_time():
    retval = datetime.now(UTC)
    return retval


def comma_comma_and(l, conj='and'):
    '''Join a list of strings joined with commas and a conjunction
       (either "and" or "or", defaulting to "and").

      Turn a list (or tuple) of strings into a single string, with all
      the items joined by ", " except for the last two, which are joined
      by either " and " or " or ". If there is only one item in the list,
      it is returned.
    '''
    if type(l) not in [list, tuple]:
        m = '%s, not a list or tuple' % type(l)
        raise TypeError(m)
    if len(l) == 0:
        retval = ''
    elif len(l) == 1:
        retval = l[0]
    else:
        base = ', {0} '.format(conj)
        retval = base.join((', '.join(l[:-1]), l[-1]))
    return retval
