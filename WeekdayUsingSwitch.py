def weekday(day_name):
    switch_day = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }
    return switch_day.get(day_name, "Invalid day")


day = int(input("Enter the number of day : "))
day_name = weekday(day)
print(f"Day {day} is {day_name}")
