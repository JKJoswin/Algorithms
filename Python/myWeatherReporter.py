import datetime
import calendar

city = input("Enter your city name:")
temp = float(input("Enter today's temperature:"))

print(f"Temperature at {city} is {temp}°C")
if temp >= 40:
    print("It is a very sunny day.")
elif temp >= 25:
    print("It is moderate day.")
elif temp >= 10:
    print("It is cold and cloudy.")
else:
    print("It is too cold.")

current = datetime.datetime.now()
print("The exact instant is ",current)
print("The Calendar for ",current.year)
print(calendar.calendar(current.year))