# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 18:52:08 2018

@author: sajid Ullah
"""

month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
def days_in_month(year, month):
    """Return number of days in that month in that year."""

    # year 2017
    # month 2
    if not 1 <= month <= 12:
        return 'Invalid Month'

      return month_days[month]

print(days_in_month(2018, 12))
