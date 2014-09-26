import math
import re
import sys

print "This program finds the intersections of two equations"
eq_1 = raw_input("Equation 1: y=")
eq_2 = raw_input("Equation 2: y=")

p = re.compile("(-?)\s*(\d*.?\d*)x\^(-?\d*/?\d*\.?\d*)|"\
               "(-?)\s*(\d*\.?\d*)x(?!\^)|"\
               "(?<!\^)(-?)\s*(\d*\.?\d+)(?![x\.])")

polys = (re.findall(p, eq_1), re.findall(p, eq_2))
for poly in polys:
    for term in range(len(poly)):
        if "." in poly[term][2] or "/" in poly[term][2]:
            print "THIS PROGRAM WON'T WORK ON FRACTIONAL POWERS"
            sys.exit()

        if poly[term][2] != "" and int(poly[term][2]) < 0:
            print "THIS PROGRAM WON'T WORK ON NEGATIVE POWERS"
            sys.exit()


orders = [0, 1]
for eq in (eq_1, eq_2):
    orders.extend(map(int, re.findall("x\^(-?\d+)", eq)))

orders = sorted(set(orders), reverse=True)

terms = {}
for order in orders:
    term = 0
    for eq in (eq_1, eq_2):
        co = 0
        split = []
        if order != 0:
            if order == 1:
                expr = re.compile(r"(-?)\s*(\d*\.?\d*)x(?!\^)")
            else:
                expr = re.compile(r"(-?)\s*(\d*\.?\d*)x\^{}".format(order))
            for pair in re.findall(expr, eq):
                split.extend(list(pair))
            for element in split:
                if split.index(element) % 2 == 0 and element == '':
                    split[split.index(element)] = "+"
                elif element == '':
                    split[split.index(element)] = 1

        elif order == 0:
            expr = re.compile(r"(?<!\^)(-?)\s*(\d*\.?\d+)(?![x\.])")
            for pair in re.findall(expr, eq):
                split.extend(list(pair))
            for element in split:
                if element == '':
                    split[split.index(element)] = "+"

        for element in split:
            if element == '+':
                co += float(split[split.index(element) + 1])
                split[split.index(element)] = " "
            elif element == '-':
                co -= float(split[split.index(element) + 1])
                split[split.index(element)] = " "
        
        if eq is eq_1:
            term += co
        else:
            term -= co
        
        terms[order] = term

orders = sorted(terms, reverse=True)

if max(orders) > 2:
    print "A polynomial above order 2 is NOT MY CUP OF TEA."

elif max(orders) > 1:
    a = terms[2]
    b = terms[1]
    c = terms[0]
    if a == 0:
        try:
            print -terms[0] / terms[1]
        except ZeroDivisionError:
            print "These two lines run parallel. They will never intersect."
    elif 4 * a * c > b ** 2:
        print "These two equations will never intersect."
    else:
        x_1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
        x_2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
        y_1 = 0
        if round(x_1, 4) != round(x_2, 4):
            print "Two solutions:"
        for term in range(len(poly)):
            if (poly[term][0] == "" and poly[term][1] == "" and
                poly[term][2] == "" and poly[term][4] == "" and
                poly[term][5] == "" and poly[term][6] == ""):
                if poly[term][3] == "":
                    y_1 += x_1
                else:
                    y_1 -= x_1
            if poly[term][2] != "" and poly[term][1] != "":
                value = x_1 * x_1 * float(poly[term][1])
                if poly[term][0] == "":
                    y_1 += value
                else:
                    y_1 -= value
            if poly[term][2] != "" and poly[term][1] == "":
                value = x_1 * x_1
                if poly[term][0] == "":
                    y_1 += value
                else:
                    y_1 -= value
            if poly[term][4] != "":
                value = x_1 * float(poly[term][4])
                if poly[term][3] == "":
                    y_1 += value
                else:
                    y_1 -= value
            if poly[term][6] != "":
                value = float(poly[term][6])
                if poly[term][5] == "":
                    y_1 += value
                else:
                    y_1 -= value
        print "({}, {})".format(float(x_1), float(y_1))
        if round(x_1, 4) != round(x_2, 4):
            y_2 = 0
            for term in range(len(poly)):
                if (poly[term][0] == "" and poly[term][1] == "" and
                    poly[term][2] == "" and poly[term][4] == "" and
                    poly[term][5] == "" and poly[term][6] == ""):
                    if poly[term][3] == "":
                        y_2 += x_2
                    else:
                        y_2 -= x_2
                if poly[term][2] != "" and poly[term][1] != "":
                    value = x_2 * x_2 * float(poly[term][1])
                    if poly[term][0] == "":
                        y_2 += value
                    else:
                        y_2 -= value
                if poly[term][2] != "" and poly[term][1] == "":
                    value = x_2 * x_2
                    if poly[term][0] == "":
                        y_2 += value
                    else:
                        y_2 -= value
                if poly[term][4] != "":
                    value = x_2 * float(poly[term][4])
                    if poly[term][3] == "":
                        y_2 += value
                    else:
                        y_2 -= value
                if poly[term][6] != "":
                    value = float(poly[term][6])
                    if poly[term][5] == "":
                        y_2 += value
                    else:
                        y_2 -= value
            print "({}, {})".format(float(x_2), float(y_2))
            
elif max(orders) > 0:
    try:
        x = -terms[0] / terms[1]
    except ZeroDivisionError:
        print "These two lines run parallel. They will never intersect."
    y = 0
    for term in range(len(poly)):
        if poly[term][4] != "":
            value = x * float(poly[term][4])
            if poly[term][3] == "":
                y += value
            else:
                y -= value
        if poly[term][6] != "":
            value = float(poly[term][6])
            if poly[term][5] == "":
                y += value
            else:
                y -= value
    print "({}, {})".format(float(x), float(y))

