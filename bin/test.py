from math import log, ceil, exp

maxTPreward = 41900000000000000
AS = 87 #
phan = 7 #
#tp = .0177
tp = ((50 - 49 * (exp(-AS/10000.0))) + .05 * int(phan))/100
curSolomon = 195232
ponyboy = 19
soloMultiplier = 1+(2.8+((curSolomon-80)*0.01))*(ponyboy+1)


maxTPzone=int(    ceil(   (log(maxTPreward/(20*soloMultiplier)))   /      (log(1+tp))   )         *5)+100

print maxTPzone
print tp