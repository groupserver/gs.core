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
from gs.core import convert_int2b62


class TestInt2B62(TestCase):
    def test_convert(self):
        i = 12
        r = convert_int2b62(i)
        self.assertEqual(r, 'c')

    def test_convert_2(self):
        i = 128
        r = convert_int2b62(i)
        self.assertEqual(r, '24')


if __name__ == '__main__':
    unittest_main()
