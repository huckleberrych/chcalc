from math import exp, log, ceil, floor

siya = 1
curAtman = '0'
tp = 0
ascendZone = 147

"""
test = int(floor(2.832*log(siya) - 1.416*log(alpha) - 1.416*log(4.0/3-exp(-0.013*max(int(curAtman), 1)))-6.613))
"""

#optAtman = int(floor(       2.832*log(siya)   -   1.416*log(alpha)  -     1.416*log(4.0/3-exp(-0.013*int(curAtman)))     -6.613)   )

#alpha = 1.4067 * log(1 + tp * 1) / log(ceil(ascendZone / 500.0) * 0.005 + 1.14)
alpha = log(1+tp)


print alpha