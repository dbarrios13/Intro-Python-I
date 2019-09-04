"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
from datetime import datetime

user_input = input('Enter a month and/or year separated by commas: ').split(',')

current_month = datetime.now().strftime("%m")
current_year = datetime.now().strftime("%Y")

def display_calendar(m = current_month, y = current_year):
  def cal_print(year, month):
    print(calendar.TextCalendar(calendar.SUNDAY).formatmonth(int(year), int(month)))
  if user_input[0] == '':
    cal_print(y, m)
  elif int(user_input[0]) <= 12:
    if len(user_input) == 2:
      m = user_input[0]
      y = user_input[1]
    else:
      m = user_input[0]
    cal_print(y, m)
  elif len(user_input[0]) == 4:
    y = user_input[0]
    cal_print(y, m) 
  else:
    print('In order to print calendar you must submit a month and year both digits and separated by a comma, ex. 10, 2010')

display_calendar()