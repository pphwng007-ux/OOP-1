#1. Seconds in 42 minutes 42 seconds
minutes = 42
seconds = 42
total_seconds = (minutes * 60) + seconds
print("Total seconds in 42 minutes and 42 seconds: ", total_seconds,"s")

#2. Miles in 10 kilometers
kilometers = 10
miles = kilometers/1.61
print("Miles in 10 kilometers:", miles,"m")

#3.Average pace and average speed in miles per hour
hour = total_seconds / 3600
average_speed = kilometers / hour
print("Average speed in miles per hour:", average_speed,"km/h")

average_pace = total_seconds / miles
pace_minutes = int(average_pace // 60)
pace_seconds = int(average_pace % 60)
print("Average pace in minutes and seconds per mile:", pace_minutes, "minutes", pace_seconds, "seconds per mile")
