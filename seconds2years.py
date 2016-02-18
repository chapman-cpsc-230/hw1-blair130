"""
File: <seconds2years.py>

Copyright (c) 2016 <Lucas Blair>

License: MIT

<Tells whether a baby will live to a billion seconds>
"""
year = (3600*24*365)
lifeyears = 1000000000/year
print lifeyears
if lifeyears < 100:
    print "He will live!"
else:
    print "He will not live"
