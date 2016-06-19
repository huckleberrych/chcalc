from math import ceil, floor

curTesty = 4.2397
optTesty = 5

if floor(optTesty) != floor(curTesty) and ceil(optTesty) != ceil(curTesty):
    print 'calc a new zone'
else:
    print 'don\'t calc a new zone'