from datetime import date, timedelta
import calendar

def years_days(year):
    start = date(year, 1, 1).toordinal()
    end = 0
    if calendar.isleap(year):
        end = start + 366
    else:
        end = start + 365
    res = (date.fromordinal(i) for i in range(start, end))
    return res

dates = years_days(2022)

print(next(dates))
print(next(dates))
print(next(dates))
print(next(dates))

dates = years_days(2077)

print(*dates)