#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2014 Martin Owens
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
"""
Test crontab use of UTF-8 filenames and strings
"""

import os
import sys

sys.path.insert(0, '../')

import unittest
from crontab import CronTab, PY3
try:
    from test import test_support
except ImportError:
    from test import support as test_support

if PY3:
    unicode = str


class Utf8TestCase(unittest.TestCase):
    """Test basic functionality of crontab."""
    def setUp(self):
        self.crontab = CronTab(tabfile='data/a-ůțƒ-8.tab')

    def test_01_read(self):
        """Read from utf8 Filename"""
        self.assertTrue(self.crontab)

    def test_02_write(self):
        """Write to utf8 Filename"""
        self.crontab.write("data/output-ůțƒ-8.tab")

    def test_03_presevation(self):
        """All Entries Re-Rendered Correctly"""
        self.assertEqual(
           open("data/a-ůțƒ-8.tab", "r").read(),
           open("data/output-ůțƒ-8.tab", "r").read())

    def test_04_command(self):
        """Read Command String"""
        self.assertEqual(self.crontab[0].command, u"ůțƒ_command")

    def test_05_comment(self):
        """Read Comment String"""
        self.assertEqual(self.crontab[0].comment, u'ůțƒ_comment')

    def test_06_unicode(self):
        """Write New via Unicode"""
        c = self.crontab.new(command=u"ůțƒ_command",  comment=u'ůțƒ_comment')
        self.assertEqual(c.command, u"ůțƒ_command")
        self.assertEqual(c.comment, u"ůțƒ_comment")
        self.crontab.render()

    def test_07_utf8(self):
        """Write New via UTF-8"""
        c = self.crontab.new(command='\xc5\xaf\xc8\x9b\xc6\x92_command',
                             comment='\xc5\xaf\xc8\x9b\xc6\x92_comment')
        self.crontab.render()

if __name__ == '__main__':
    test_support.run_unittest(
       Utf8TestCase,
    )
