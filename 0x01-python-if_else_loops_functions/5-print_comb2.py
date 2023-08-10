#!/usr/bin/python3
for nb in range(0, 100):
    if nb == 99:
        print("{}".format(nb))
    else:
        print("{:02}".format(nb), end=", ")
