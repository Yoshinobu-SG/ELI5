fast_min = 0.0

fast_sec = 0.0

slow_min = 0.0

slow_sec = 0.0

ave_min = 0.0

ave_sec = 0.0

fastest_time = 1000.0

slowest_time = 0.0

total = 0.0



laps = int(input("Enter no of laps: "))

for i in range(laps):

  print("Lap", i + 1)

  tmin = int(input("Enter minutes: "))

  tsec = int(input("Enter seconds: "))

  total += (tmin * 60) + tsec

  t = (tmin * 60) + tsec



  if t < fastest_time:

    fastest_time = t

    fast_min = tmin

    fast_sec = tsec



  if t > slowest_time:

    slowest_time = t

    slow_min = tmin

    slow_sec = tsec



average_time = total / laps

ave_min = average_time // 60

ave_sec = average_time % 60

print("Fastest lap time = {} min {} sec".format(fast_min, fast_sec))

print("Slowest lap time = {} min {} sec".format(slow_min, slow_sec))

print("Average lap time = {} min {} sec".format(ave_min, ave_sec))###for and in
