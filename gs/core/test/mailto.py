# -*- coding: utf-8 -*-
#############################################################################
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
##############################################################################
from __future__ import absolute_import, unicode_literals
from unittest import TestCase
from gs.core.mailto import mailto, quote


class TestMailto(TestCase):
    '''Test the mailto function of gs.core.utils'''

    def test_ascii(self):
        'Ensure that plain-ascii works fine'
        to = 'support@example.com'
        subject = 'Help'
        body = 'Hello, I need "help"'

        r = mailto(to, subject, body)

        self.assertEqual('mailto:', r[:7], 'Does not start with "mailto:"')
        self.assertNotIn(' ', r, 'URI contains spaces')
        self.assertNotIn('"', r, 'URI contains quote marks')
        self.assertIn(to, r)
        self.assertIn('subject=', r)
        self.assertIn('body=', r)

    def test_unocode(self):
        'Ensure that Unicode works fine'
        to = 'support@example.com'
        subject = 'Happy Halloween \U0001f383'
        body = 'Boo! \U0001F47B'

        r = mailto(to, subject, body)

        expected = 'mailto:support@example.com?subject=Happy%20Halloween%20%F0%9F%8E%83&'\
                   'body=Boo%21%20%F0%9F%91%BB'
        self.assertEqual(expected, r)


class TestQuote(TestCase):
    '''Test the core function that quotes the parameters of the mailto'''
    def test_quote_ascii(self):
        'Test the identity-quoting'
        e = 'support'
        r = quote(e)
        self.assertEqual(e, r)

    def test_quote_at(self):
        # --=mpj17=-- This is really just testing urllib.parse. Also, we do not do this with the
        # actual to-address, it is more for the body.
        to = 'support@example.com'
        r = quote(to)
        self.assertEqual('support%40example.com', r)

    def test_quote_unicode(self):
        'Ensure we convert Unicode to UTF-8 and encode it'
        subject = 'Happy Halloween \U0001f383'
        r = quote(subject)
        self.assertEqual('Happy%20Halloween%20%F0%9F%8E%83', r)
