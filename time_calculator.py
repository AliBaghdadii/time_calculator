def add_time(start_time, duration_time, show_day=None):
    # write days of the week in a dictionary
    days_of_the_week = {"Saturday": 0, "Sunday": 1, "Monday": 2, "Tuesday": 3, "Wednesday": 4, "Thursday": 5, "Friday": 6}
    # getting information about start time
    time_of_start, midday_of_start_time = start_time.split()
    hour_in_start_time, minutes_in_start_time = time_of_start.split(':')
    hour_in_start_time = int(hour_in_start_time)
    minutes_in_start_time = int(minutes_in_start_time)
    # turn the hour in the 24 hour format
    if midday_of_start_time == "PM":
        hour_in_start_time += 12
    # getting information about duration time
    duration_hour, duration_minutes = duration_time.split(':')
    duration_hour = int(duration_hour)
    duration_minutes = int(duration_minutes)
    # calculating the final hour and final minutes
    total_minutes = minutes_in_start_time + duration_minutes
    remaining_minutes = total_minutes % 60
    extra_hours = total_minutes // 60
    total_hour = hour_in_start_time + duration_hour + extra_hours
    # final hours as per 12 Hour clock
    ans_hour = (total_hour % 24) % 12
    # turn ans_hour in 24 hour clock format
    if ans_hour == 0:
        ans_hour = 12
    ans_hour = str(ans_hour)
    # 1 day = 24 hour
    total_day = (total_hour // 24)
    # we should know the day is am or pm
    final_midday = ""
    if (total_hour % 24) <= 11:
        final_midday = "AM"
    else:
        final_midday = "PM"
    # if the remaining of the total minutes is single digit, we should add a '0' before it
    if remaining_minutes <= 9:
        remaining_minutes = '0' + str(remaining_minutes)
    else:
        remaining_minutes = str(remaining_minutes)
    # returning
    final_time = ans_hour + ":" + remaining_minutes + ' ' + final_midday
    if show_day == None:
        if total_day == 0:
            return final_time
        if total_day == 1:
            return final_time + ' (next day)'
        return final_time + ' (' + str(total_day) + ' days later)'
    else:
        final_day = (days_of_the_week[show_day.lower().capitalize()] + total_day) % 7
        # find the final day in the days_of_the_week dictionary
        for i, j in days_of_the_week.items():
            if j == final_day:
                final_day = i
                break
        if total_day == 0:
            return final_time + ', ' + final_day
        if total_day == 1:
            return final_time + ', ' + final_day + ' (next day)'
        return final_time + ', ' + final_day + ' (' + str(
            total_day) + ' days later)'
