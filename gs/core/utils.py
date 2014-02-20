# -*- coding: utf-8 -*-
from __future__ import unicode_literals


def to_ascii(obj):
    u = to_unicode_or_bust(obj)
    retval = u.encode('ascii', 'ignore')
    return retval


def to_unicode_or_bust(obj, encoding='utf-8'):
    'http://farmdev.com/talks/unicode/'
    #FIXME: Move to gs.utils
    if isinstance(obj, basestring):
        if not isinstance(obj, unicode):
            obj = unicode(obj, encoding)
    return obj
