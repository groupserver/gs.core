# -*- coding: utf-8 -*-
#############################################################################
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
from __future__ import absolute_import, unicode_literals
from unittest import TestCase, main as unittest_main
from gs.core import to_ascii, to_unicode_or_bust, comma_comma_and


class TestToUnicode(TestCase):
    '''Test the to_unicode_or_bust function of gs.core.utils'''

    def test_unicode_to_unicode(self):
        testText = 'Word association football \u26BD'
        r = to_unicode_or_bust(testText)
        self.assertEqual(type(testText), type(r))

    def test_ascii_to_unicode(self):
        testText = b'Word association football'
        r = to_unicode_or_bust(testText)
        self.assertEqual('Word association football', r)

    def test_utf8_to_unicode(self):
        testText = b'Word association football \342\232\275'
        r = to_unicode_or_bust(testText)
        self.assertEqual('Word association football \u26BD', r)


class TestToAscii(TestCase):
    '''Test the to_unicode_or_bust function of gs.core.utils'''

    def test_ascii_to_ascii(self):
        testText = b'Word association football'
        r = to_ascii(testText)
        self.assertEqual(type(testText), type(r))

    def test_unicode_to_ascii(self):
        testText = 'Word association football \u26BD'
        r = to_ascii(testText)
        self.assertEqual(b'Word association football ', r)

    def test_utf8_to_ascii(self):
        testText = b'Word association football \342\232\275'
        r = to_ascii(testText)
        self.assertEqual(b'Word association football ', r)


class TestCommaCommaAnd(TestCase):
    def test_err(self):
        testText = 'Dirk'
        self.assertRaises(TypeError, comma_comma_and, testText)

    def test_double(self):
        testText = ['Dirk', 'Dinsdale']
        r = comma_comma_and(testText)
        self.assertEqual('Dirk, and Dinsdale', r)

    def test_three(self):
        testText = ['Dirk', 'Dinsdale', 'the local constable for the area']
        r = comma_comma_and(testText)
        expected = 'Dirk, Dinsdale, and the local constable for the area'
        self.assertEqual(expected, r)


if __name__ == '__main__':
    unittest_main()
