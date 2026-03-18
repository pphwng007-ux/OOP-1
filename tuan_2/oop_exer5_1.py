# current time in seconds since epoch
import time
current_time = time.time()
print("Current time in seconds since epoch:", current_time, "s")

# number of days since epoch
days_since_epoch = current_time // (24 * 3600)
print("Number of days since epoch:", days_since_epoch, "days")

# seconds remaining today
seconds_today = current_time % (24 * 3600)

# coverts to hour, minute, second 
hour = seconds_today // 3600
minute = (seconds_today % 3600) // 60
second = seconds_today % 60
print("Current time today:", hour, "hours", minute, "minutes", second, "seconds")

