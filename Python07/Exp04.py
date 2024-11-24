# Print a Calendar for a Particular Month

import calendar

year = int(input("Enter the year: "))
month = int(input("Enter the month (1-12): "))

print(f"\nCalendar for {month}/{year}:\n")
print(calendar.month(year, month))
