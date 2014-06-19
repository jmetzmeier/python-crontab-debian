#!/usr/bin/python
#
# Copyright (C) 2012 Jay Sigbrandt <jsigbrandt@slb.com>
#                    Martin Owens <doctormo@gmail.com>
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
Test crontab usage.
"""

import os
import sys

sys.path.insert(0, '../')

import unittest
from crontab import CronTab, __doc__
try:
    from test import test_support
except ImportError:
    from test import support as test_support

class DummyStdout(object):
    def write(self, text):
        pass

BASIC = '@hourly firstcommand\n\n'
USER = '\n*/4 * * * * user_command # user_comment\n\n\n'

def flush():
    pass

class UseTestCase(unittest.TestCase):
    """Test use documentation in crontab."""
    def test_01_empty(self):
        """Open system crontab"""
        cron = CronTab()
        self.assertEqual(cron.render(), "")

    def test_02_user(self):
        """Open a user's crontab"""
        cron = CronTab(user='basic')
        self.assertEqual(cron.render(), BASIC)

    def test_03_usage(self):
        """Dont modify crontab"""
        cron = CronTab(tab='')
        sys.stdout = DummyStdout()
        sys.stdout.flush = flush
        exec(__doc__)
        sys.stdout = sys.__stdout__
        self.assertEqual(cron.render(), '')

    def test_04_username(self):
        """Username is True"""
        cron = CronTab(user=True)
        self.assertNotEqual(cron.user, True)
        self.assertEqual(cron.render(), USER)

if __name__ == '__main__':
    test_support.run_unittest(
       UseTestCase,
    )
