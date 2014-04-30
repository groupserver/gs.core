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
import sys
from pytz import utc as UTC


def to_ascii(stringOrUnicode):
    '''Convert a string to ASCII, with a reasonable chance of success.

:param stringOrUnicode: The instance to convert.
:return: The object converted to a string
:rtype: ``str``

The ``to_ascii`` function, ultimately, calls
``unicode.encode('ascii', 'ignore')``, but it has a couple of advantages.

#. It takes up less space when writing code.
#. If passed a string then the string will be decoded as UTF-8, before
   being re-encoded as ASCII.

The second point may seem to be redundant, but it avoids the dreaded
**Unicode Decode Error** from occurring.

Example:
    Ensure the filename with the group identifier is ascii::

        filename = to_ascii('{0}-members.csv'.format(self.groupInfo.id))
'''
    u = to_unicode_or_bust(stringOrUnicode)
    retval = u.encode('ascii', 'ignore')
    return retval


def p2_to_unicode_or_bust(obj, encoding='utf-8'):
    'http://farmdev.com/talks/unicode/'
    if isinstance(obj, basestring):
        if not isinstance(obj, unicode):
            obj = unicode(obj, encoding)
    return obj


def p3_to_unicode_or_bust(obj, encoding='utf-8'):
    if hasattr(obj, 'decode'):
        obj = obj.decode(encoding)
    return obj

# Figure out if we should be using the Python 2 or the Python 3 version of
# to_unicode_or_bust
if (sys.version_info < (3, )):
    p23 = p2_to_unicode_or_bust
else:
    p23 = p3_to_unicode_or_bust


def to_unicode_or_bust(stringOrUnicode, encoding='utf-8'):
    '''Convert an object to a Unicode instance, with reasonable chance of
success.

:param stringOrUnicode: The instance to convert to a unicode.
:param encoding: The encoding for the object. Defaults to ``utf-8``.
:return: The object converted to a Unicode.
:rtype: ``unicode`` (or ``str`` in Python 3)

Sometimes text-input has… uncertain… origins, and it is hard to know
encoding it is. The ``to_unicode_or_bust`` has a good stab at converting
the input to a Unicode instance.

Example:
    Convert some input into Unicode::

        filename = gs.core.to_unicode_or_bust(someInput)

Acknowledgements:
    Taken from an excellent presentation on `Unicode in Python by Kumar
    McMillan <http://farmdev.com/talks/unicode/>`_.
'''
    return p23(stringOrUnicode, encoding)


def curr_time():
    '''Get the current time, in UTC, as a :class:`datetime.datetime`.

:return: The current time, as a class:`datetime.datetime` instance, with the
         timezone set to ``UTC``.
:rtype: :class:`datetime.datetime`

This function returns the current time, with a timezone, as a standard
Python :class:`datetime.datetime` instance. It saves quite a few
imports!
'''
    retval = datetime.now(UTC)
    return retval


def comma_comma_and(l, conj='and'):
    '''Turn a list of strings into a single string, with commas.

:param sequence l: The strings to convert.
:param str conj: The conjunctive to use.
:return: Either

  * An empty string if the list ``l`` is empty,
  * The one item from ``l`` if ``l`` is a single item long, or
  * A single string that contains all the items from ``l`` separated by
    commas (``,``), except for the last two items that are separated by a
    comma and the conjunctive (``conj``).

:rtype: ``str``

This utility turns a list (such as ``['this', 'that', 'the other thing']``)
into a single string (``this, that, and the other thing``). It is useful
when reporting back from forms.
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
