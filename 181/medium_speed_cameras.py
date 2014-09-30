import re

expr = re.compile("(\d+\.\d+)\s(mph|km\/h)")
inp = raw_input()

m_obj = re.search(expr, inp)

if m_obj.group(2) == "mph":
    speed_limit = float(m_obj.group(1)) * 1.60934
    unit = "mph"
else:
    speed_limit = float(m_obj.group(1))
    unit = "km/h"

distances = {}
expr = re.compile("(\d)\D*(\d+)")
while True:
    inp = raw_input()

    m_obj = re.search(expr, inp)

    if m_obj:
        distances[int(m_obj.group(1)) - 1] = float(m_obj.group(2)) / 1000.
    else:
        break

times = {}
expr = re.compile("e (.*) p.*at (\d{2}):(\d{2}):(\d{2})\.")
while True:
    inp = raw_input()

    m_obj = re.search(expr, inp)

    if m_obj:
        hours = (float(m_obj.group(2)) + 
                 float(m_obj.group(3)) / 60 + 
                 float(m_obj.group(4)) / 3600)
        times[m_obj.group(1)] = [hours]
    else:
        break

while inp != '':
    while True:
        inp = raw_input()

        m_obj = re.search(expr, inp)

        if m_obj:
            hours = (float(m_obj.group(2)) + 
                     float(m_obj.group(3)) / 60 + 
                     float(m_obj.group(4)) / 3600)
            times[m_obj.group(1)].append(hours)
        else:
            break

if unit == "mph":
    speed_limit /= 1.60934

max_speed = {}
for car in times:
    for i in range(len(distances)):
        for j in range(i + 1, len(distances)):
            speed = ((float(distances[j]) - float(distances[i])) /
                     (float(times[car][j]) - float(times[car][i])))
            if unit == "mph":
                speed /= 1.60934
            if car in max_speed:
                if speed > max_speed[car]:
                    max_speed[car] = speed
            else:
                max_speed[car] = speed
for car in sorted(max_speed, key=max_speed.get):
    if max_speed[car] > speed_limit:
        print "Vehicle {} sped by {:.1f} {}".format(car, 
                                             max_speed[car] - speed_limit,
                                             unit)
