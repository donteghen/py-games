"""Calendar Maker, by Donald Teghen donaldteghen@gmail.com
Create monthly calendars, saved to a text file and fit for printing.
This code is available at https://learnwithdonny.com/mini-games/calender-maker
Tags: short"""

import datetime, os, glob

# Set up the constants:
DAYS = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')
MONTHS = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')
 
print('Calendar Maker, by Donald Teghen donaldteghen@gmail.com')
 
while True:  # Loop to get a year from the user.
    print('Enter the year for the calendar:')
    response = input('> ')
 
    if response.isdecimal() and int(response) > 0:
        year = int(response)
        break
 
    print('Please enter a numeric year, like 2023.')
    continue
 
while True:  # Loop to get a month from the user.
    print('Enter the month for the calendar, 1-12:')
    response = input('> ')
 
    if not response.isdecimal():
        print('Please enter a numeric month, like 3 for March.')
        continue
 
    month = int(response)
    if 1 <= month <= 12:
        break
 
    print('Please enter a number from 1 to 12.')
 
 
def getCalendarFor(year, month):
    calText = ''  # calText will contain the string of our calendar.

    # Put the month and year at the top of the calendar:
    calText += (' ' * 34) + MONTHS[month - 1] + ' ' + str(year) + '\n'

    # Add the days of the week labels to the calendar:
    # (!) Try changing this to abbreviations: SUN, MON, TUE, etc.
    for day in DAYS:
        if len(day) <= 6:
            calText += '...{}..'.format(day)
        else:
            calText += '..{}.'.format(day)    
        #calText += '...Sunday.....Monday....Tuesday...Wednesday...Thursday....Friday....Saturday..\n'
    calText += '.\n'
    
    # The horizontal line string that separate weeks:
    weekSeparator = (('+' + '-' * 10) * 7) + '+\n'

    # The blank rows have ten spaces in between the | day separators:
    blankRow = (('|' + (' ' * 10)) * 7) + '|\n'

    # Get the first date in the month. (The datetime module handles all
    # the complicated calendar stuff for us here.)
    currentDate = datetime.date(year, month, 1)
    print(str(currentDate), currentDate.weekday())
    # Roll back currentDate until it is Sunday. (weekday() returns 6
    # for Sunday, not 0.)
    while currentDate.weekday() != 6:
      currentDate -= datetime.timedelta(days=1)
 
    while True:  # Loop over each week in the month.
        calText += weekSeparator

        # dayNumberRow is the row with the day number labels:
        dayNumberRow = ''
        for i in range(7):
            dayNumberLabel = str(currentDate.day).rjust(2)
            dayNumberRow += '|' + dayNumberLabel + (' ' * 8)
            currentDate += datetime.timedelta(days=1) # Go to next day.
        dayNumberRow += '|\n'  # Add the vertical line after Saturday.

        # Add the day number row and 3 blank rows to the calendar text.
        calText += dayNumberRow
        for i in range(3):  # (!) Try changing the 4 to a 5 or 10.
            calText += blankRow

      # Check if we're done with the month:
        if currentDate.month != month:
            break

    # Add the horizontal line at the very bottom of the calendar.
    calText += weekSeparator
    return calText
  
calText = getCalendarFor(year, month)
print(calText)  # Display the calendar.
 
# Save the calendar to a text file:
calendarFilename = os.getcwd() + '/' + 'calender-maker/' + 'calendar_{}_{}.txt'.format(year, month)
with open(calendarFilename, 'w') as fileObj:
    fileObj.write(calText)

print('Saved to ' + calendarFilename)

# Uncomment this snippet to clear the folder of all previously created .txt files
# pathern = os.getcwd() + '/calender-maker/*.txt'
# files = glob.glob(pathern)
# for file in files:
#     os.remove(file)

