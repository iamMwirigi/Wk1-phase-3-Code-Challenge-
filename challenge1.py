def convert_to_24_hour_format(hour, minute, period):

    if period == "pm" and hour != 12:
        hour += 12
    elif period == "am" and hour == 12:
        hour = 0
    
    
    time_24_hour = f"{hour:02d}{minute:02d}"
    
    return time_24_hour
hour = 8
minute = 30
period = "am"
result = convert_to_24_hour_format(hour, minute, period)
print(result)
hour = 12
minute = 30
period = "pm"
result = convert_to_24_hour_format(hour, minute, period)
print(result)
