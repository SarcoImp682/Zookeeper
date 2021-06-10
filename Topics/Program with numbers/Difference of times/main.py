# put your python code here

# start time
hour_start = int(input())
minutes_start = int(input())
seconds_start = int(input())

# stop time
hour_stop = int(input())
minutes_stop = int(input())
seconds_stop = int(input())

# conversion
start = hour_start * 3600 + minutes_start * 60 + seconds_start
stop = hour_stop * 3600 + minutes_stop * 60 + seconds_stop

# result
print(abs(start - stop))
