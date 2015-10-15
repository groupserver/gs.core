# -*- coding: utf-8 -*-
############################################################################
#
# Copyright © 2015 OnlineGroups.net and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
############################################################################
from __future__ import absolute_import, division, unicode_literals, print_function
import sys
if sys.version_info >= (3, ):  # pragma: no cover
    from urllib.parse import quote as quote_for_url
else:  # Python 2
    from urllib import quote as quote_for_url
from .utils import to_unicode_or_bust

#: The format for the mailto URI, for writing email messages to support.
MAILTO = 'mailto:{to}?subject={subject}&body={body}'


def mailto(toAddress, subject, body):
    '''Create a mailto URI

:param str toAddress: The address to send the email to (the :mailheader:`To` header).
:param str subject: The subject of the new message (the :mailheader:`Subject` header).
:param str body: The body of the message
:returns: A mailto URI (``mailto:``).
:rtype: str

It is possible to create a URI that will create an email message when clicked. Such URIs start with
``mailto:`` (:rfc:`6068`). However, care must be taken to quote the parameters correctly. This
function creates a mailto URI with the correct quoting.'''
    quotedSubject = quote(subject)
    quotedBody = quote(body)
    retval = MAILTO.format(to=toAddress, subject=quotedSubject, body=quotedBody)
    return retval


def quote(val):
    '''Quote a string for embedding in a URI

:param str val: The value to quote
:returns: The value converted to UTF-8, and quoted to be put into a URL.
:rtype: str'''
    uval = to_unicode_or_bust(val)
    utf8val = uval.encode('utf-8')
    retval = quote_for_url(utf8val)
    return retval
