def convert_to_24_hour_format(hour, minute, period):
    # Adjust the hour based on the period ("am" or "pm")
    if period == "pm" and hour != 12:
        hour += 12
    elif period == "am" and hour == 12:
        hour = 0
    
    # Format the time in 24-hour format as a four-digit string
    time_24_hour = f"{hour:02d}{minute:02d}"
    
    return time_24_hour
hour = 12
minute = 30
period = "am"
result = convert_to_24_hour_format(hour, minute, period)
print(result)
