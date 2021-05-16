# Time Calculator
class myDateTime:
    days = 0
    hours = 0
    minutes = 0
    dayofweek = 0
    displayStr = ""
    displayWeekDay = False

    def __init__(self, strTime="00:00 AM", dayofweek=""):
        # break Time and AM/PM seperately
        if (dayofweek != ""):
            self.displayWeekDay = True

        self.__parseInputTime(strTime, dayofweek)

    def __add__(self, datetime1):
        result = myDateTime()
        result.days = self.days + datetime1.days
        result.hours = self.hours + datetime1.hours
        result.minutes = self.minutes + datetime1.minutes
        result.dayofweek = self.dayofweek + datetime1.dayofweek
        result.displayWeekDay = self.displayWeekDay or datetime1.displayWeekDay

        return result

    def __parseInputTime(self, strTime="00:00 AM", dayofweek=""):
        # decode dayofweek
        days = ["", "sunday", "monday", "tuesday",
                "wednesday", "thursday", "friday", "saturday"]
        index = 0
        for day in days:
            if day == dayofweek.lower():
                self.dayofweek = index
            index = index + 1

        # decode time
        timeIndex = strTime.find(" ")
        if timeIndex < 0:
            timePart = strTime
        else:
            timePart = strTime[0:timeIndex]

        am_pm_index = strTime.find(" ")
        am_pm = ""
        if (am_pm_index > 0):
            am_pm = strTime[am_pm_index+1:]

        self.hours = int(timePart[:timePart.find(":")])
        self.minutes = int(timePart[timePart.find(":")+1:])
        if (am_pm == "PM"):
            self.hours = self.hours + 12

    def __str__(self):
        self.__formatResult()
        return self.displayStr

    def __formatResult(self):
        self.hours = self.hours+int(self.minutes/60)
        self.days = self.days + int(self.hours/24)
        self.dayofweek = (self.dayofweek + self.days) % 7

        self.minutes = self.minutes % 60
        self.hours = self.hours % 24
        am_pm = " AM"

        if (self.hours >= 12):
            am_pm = " PM"

        display_hrs = self.hours % 12
        if (display_hrs == 0):
            display_hrs = 12

        display_mins = str(self.minutes)
        if (len(display_mins) < 2):
            display_mins = "0"*(2-len(display_mins)) + display_mins

        display_hrs = str(display_hrs)
        days = ["", "Sunday", "Monday", "Tuesday",
                "Wednesday", "Thursday", "Friday", "Saturday"]

        display_weekday = ""
        if (self.displayWeekDay == True):
            display_weekday = ", "+days[self.dayofweek]

        if (self.days == 1):
            display_days = " (next day)"
        else:
            display_days = " ("+str(self.days)+" days later)"
        if self.days < 1:
            display_days = ""

        self.displayStr = display_hrs+":"+display_mins + \
            am_pm+display_weekday+display_days


def add_time(start_time, duration, dayofweek=""):
    dateTime1 = myDateTime(start_time, dayofweek)
    dateTime2 = myDateTime(duration)
    result = dateTime1 + dateTime2

    return str(result)


# MAIN
print(add_time("3:00 PM", "3:10"))
print(add_time("11:30 AM", "2:32", "Monday"))
print(add_time("11:43 AM", "0:20"))
print(add_time("10:10 PM", "3:30"))
print(add_time("11:43 PM", "24:20", "tueSday"))
print(add_time("6:30 PM", "205:12"))
# Test file
print(add_time("3:30 PM", "2:12"))
print(add_time("11:55 AM", "3:12"))
print(add_time("9:15 PM", "5:30"))
print(add_time("11:40 AM", "0:25"))
print(add_time("2:59 AM", "24:00"))
print(add_time("11:59 PM", "24:05"))
print(add_time("8:16 PM", "466:02"))
print(add_time("5:01 AM", "0:00"))
print(add_time("3:30 PM", "2:12", "Monday"))
print(add_time("2:59 AM", "24:00", "saturDay"))
print(add_time("11:59 PM", "24:05", "Wednesday"))
print(add_time("8:16 PM", "466:02", "tuesday"))
