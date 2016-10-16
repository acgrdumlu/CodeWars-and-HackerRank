time = raw_input()
ampm = time[-2:]
time = time[:-2]

time = [int(x) for x in time.split(':')]
if ampm == 'PM' or ampm == 'pm':
	if time[0] != 12:
		time[0] += 12
elif ampm == 'AM' or ampm == 'am':
	if time[0] == 12:
		time[0] = 0

hour = str(time[0])
if len(hour) < 2:
	hour = '0' + hour

minute = str(time[1])
if len(minute) < 2:
	minute = '0' + minute

second = str(time[2])
if len(second) < 2:
	second = '0' + second

time = [hour, minute, second]
print ':'.join(time)