import savedecoder
from math import log, floor, ceil, exp, log10, sqrt

MODE = 'idle'
HIGHWEP = 'off'

def getCurrentAncientLvls(input):
    fromsave = input['ancients']['ancients']
    ancientIDs = {'28':'Argaiv', '13':'Atman', '15':'Bhaal',
                  '18':'Bubos', '17':'Chronos', '11':'Dogcog',
                  '14':'Dora', '12':'Fortuna', '19':'Frags',
                  '29':'Jugs', '21':'Kuma', '4':'Libertas',
                  '8':'Mammon', '9':'Mimzee', '16':'Morg',
                  '5':'Siya', '3':'Solomon'}
    curAncients = {}
    for k, v in ancientIDs.iteritems():
        try:
            curAncients[v] = float(fromsave[k]['level'])
        except:
            curAncients[v] = 0
    return curAncients

def calcOptimalAncientLvls(curAncients, siya, calcs):
    optAncients = {'Argaiv':0,
                   'Atman':0,
                   'Bhaal':0,
                   'Bubos':0,
                   'Chronos':0,
                   'Dogcog':0,
                   'Dora':0,
                   'Frags':0,
                   'Fortuna':0,
                   'Jugs':0,
                   'Kuma':0,
                   'Libertas':0,
                   'Mammon':0,
                   'Mimzee':0,
                   'Morg':0,
                   'Siya':siya,
                   'Solomon':0}
    if HIGHWEP == 'on':
        goldratio = 0.905
    else:
        goldratio = 0.926
    if MODE == 'hybrid':
        optAncients['Frags'] = round(siya * calcs.hybridMultiplier)
        optAncients['Bhaal'] = optAncients['Frags']
        optAncients['Jugs'] = round(optAncients['Frags'] ** 0.8)
    base = max(optAncients['Frags'], optAncients['Siya'])
    optAncients['Argaiv'] = base
    if calcs.alpha != 0:
        optAncients['Atman'] = ceil(
            2.832*log(base)
            - 1.416*log(calcs.alpha)
            - 1.416*log(4.0/3-exp(-0.013*curAncients['Atman']))
            -6.613)
        optAncients['Bubos'] = ceil(
            2.8*log(base)
            - 1.4*log(1+exp(-0.02*curAncients['Bubos']))
            - 5.94)
        optAncients['Chronos'] = ceil(
            2.75*log(base)
            - 1.375*log(2-exp(-0.034*curAncients['Chronos']))
            - 5.1)
        optAncients['Dogcog'] = ceil(
            2.844*log(base)
            - 1.422*log(1.0/99 + exp((-0.01)*curAncients['Dogcog']))
            - 7.232)
        optAncients['Dora'] = ceil(
            2.877*log(base)
            - 1.4365*log(100.0/99-exp(-0.002*curAncients['Dora']))
            - 9.63)
        optAncients['Fortuna'] = ceil(
            2.875*log(base)
            - 1.4375*log(10.0/9-exp(-0.0025*curAncients['Fortuna']))
            - 9.3)
        optAncients['Kuma'] = ceil(
            2.844*log(base)
            - 1.422*log(calcs.alpha)
            - 1.422*log(0.25 + exp(-0.01*curAncients['Kuma']))
            - 7.014)
        optAncients['Libertas'] = ceil(goldratio*siya)
        optAncients['Mammon'] = ceil(goldratio*base)
        optAncients['Mimzee'] = ceil(goldratio*base)
        optAncients['Morg'] = (base ** 2)
        optAncients['Solomon'] = ceil(base**(0.8)/calcs.alpha**0.4)

    return optAncients

def prepForOutput(input):
    for k in input:
        input[k] = int(input[k])
        if input[k] > 1e9:
            input[k] = "{:.3E}".format(input[k])
        else:
            input[k] = "{:,}".format(input[k])
    return input

class Calculations(dict):
    
    def __init__(self, savedata, hybridMultiplier):
        self.savedata = savedata
        self.xyl = 0
        self.chor = 0
        self.phan = 0
        self.borb = 0
        self.pony = 0
        self.AS = 0
        self.tp = 0
        self.ascendZone = 0
        self.alpha = 0
        self.totalSoulsAvail = 0
        self.chorDiscount = 0
        self.maxTPreward = 0
        self.soloMultiplier = 1
        self.maxTPzone = 0
        self.newTPzone = 0
        self.newSoloMultiplier = 1
        self.hybridMultiplier = hybridMultiplier
        
    def doTheMath(self, Solomon, useAscendSouls):
        if self.savedata.get("ancientSoulsTotal"):
            self.AS = self.savedata["ancientSoulsTotal"]
        if self.savedata.get('outsiders'):
            self.xyl = self.savedata['outsiders']['outsiders']['1']['level']
            self.chor = self.savedata['outsiders']['outsiders']['2']['level']
            self.phan = self.savedata['outsiders']['outsiders']['3']['level']
            self.borb = self.savedata['outsiders']['outsiders']['4']['level']
            self.pony = self.savedata['outsiders']['outsiders']['5']['level']
            self.tp = 1 - 0.49 * exp(-self.AS/10000.0) - 0.5 * exp(-self.phan/1000.0)
            self.soloMultiplier = calcSoloMultiplier(Solomon, self.pony)
            self.chorDiscount = 1 - 0.95 ** self.chor
        self.ascendZone = self.savedata["highestFinishedZonePersist"]
        
        if HIGHWEP == 'on':
            self.alpha = 1.1085 * log(1 + self.tp) / log(ceil(self.ascendZone / 500.0) * 0.005 + 1.14)
        else:
            self.alpha = 1.4067 * log(1 + self.tp) / log(ceil(self.ascendZone / 500.0) * 0.005 + 1.14)
        self.totalSoulsAvail = float(self.savedata["heroSouls"])
        if useAscendSouls == 'on':
            self.totalSoulsAvail += float(self.savedata["primalSouls"])
        
        if self.savedata.get("heroSoulsSacrificed"):
            self.maxTPreward = float(self.savedata["heroSoulsSacrificed"]) * (0.05 + (self.borb * 0.005))
        if self.maxTPreward != 0:
            self.maxTPzone = int((ceil((log(self.maxTPreward / (20 * self.soloMultiplier))) / (log(1 + self.tp))) * 5) + 100)
            
    def findNewTPzone(self, optSolomon, curSolomon):
        #ancient levels have decimals, must check vs our opt (always x.0) so if opt = +0 then maxTPzone = newTPzone
        if floor(optSolomon) != floor(curSolomon) and ceil(optSolomon) != ceil(curSolomon):
            if self.savedata.get('outsiders'):
                self.newSoloMultiplier = calcSoloMultiplier(optSolomon, self.pony)
            if self.maxTPreward != 0:
                self.newTPzone = int((ceil((log(self.maxTPreward / (20 * self.newSoloMultiplier))) / (log(1 + self.tp))) * 5) + 100)
        else:
            self.newTPzone = self.maxTPzone
            
def costFunc1(chorDiscount, opt, cur):
    return max(ceil((1-chorDiscount)*(ceil((0.4*opt**2.5)-(0.4*cur**2.5)))), 0)
    
def costFunc2(chorDiscount, opt, cur):
    return max(ceil(((1-chorDiscount)*((2**(opt+1)-1)-(2**(cur+1)-1)))), 0)
    
def costFunc3(chorDiscount, opt, cur):
    return max(ceil((1 - chorDiscount)*(0.5*(opt)*(opt+2)-0.5*cur*(cur+2))), 0)

def costFunc4(chorDiscount, opt, cur):
    return max(ceil((1-chorDiscount)*(opt-cur)), 0)

def calcOptCost(curAncients, optAncients, chorDiscount):
    optCost = {}
    optCost['Argaiv'] = costFunc3(chorDiscount, optAncients['Argaiv'], curAncients['Argaiv'])
    optCost['Atman'] = costFunc2(chorDiscount, optAncients['Atman'], curAncients['Atman'])
    optCost['Bhaal'] = costFunc3(chorDiscount, optAncients['Bhaal'], curAncients['Bhaal'])
    optCost['Bubos'] = costFunc2(chorDiscount, optAncients['Bubos'], curAncients['Bubos'])
    optCost['Chronos'] = costFunc2(chorDiscount, optAncients['Chronos'], curAncients['Chronos'])
    optCost['Dogcog'] = costFunc2(chorDiscount, optAncients['Dogcog'], curAncients['Dogcog'])
    optCost['Dora'] = costFunc2(chorDiscount, optAncients['Dora'], curAncients['Dora'])
    optCost['Fortuna'] = costFunc2(chorDiscount, optAncients['Fortuna'], curAncients['Fortuna'])
    optCost['Frags'] = costFunc3(chorDiscount, optAncients['Frags'], curAncients['Frags'])
    optCost['Jugs'] = costFunc1(chorDiscount, optAncients['Jugs'], curAncients['Jugs'])
    optCost['Kuma'] = costFunc2(chorDiscount, optAncients['Kuma'], curAncients['Kuma'])
    optCost['Libertas'] = costFunc3(chorDiscount, optAncients['Libertas'], curAncients['Libertas'])
    optCost['Mammon'] = costFunc3(chorDiscount, optAncients['Mammon'], curAncients['Mammon'])
    optCost['Mimzee'] = costFunc3(chorDiscount, optAncients['Mimzee'], curAncients['Mimzee'])
    optCost['Morg'] = costFunc4(chorDiscount, optAncients['Morg'], curAncients['Morg'])
    optCost['Siya'] = costFunc3(chorDiscount, optAncients['Siya'], curAncients['Siya'])
    optCost['Solomon'] = costFunc1(chorDiscount, optAncients['Solomon'], curAncients['Solomon'])

    optCost['Total'] = sum(optCost.itervalues())
    return optCost

def findOptSiya(curAncients, calcs):

    ##check if they can afford to optimize
    optAncients = calcOptimalAncientLvls(curAncients, curAncients['Siya'], calcs)
    optcost = calcOptCost(curAncients, optAncients, calcs.chorDiscount)
    if optcost['Total'] > calcs.totalSoulsAvail:
        return 'broke'  ###can't afford to optimize
    
    ##check if they can afford +1 siya
    optAncients = calcOptimalAncientLvls(curAncients, curAncients['Siya'] + 1, calcs)
    optcost = calcOptCost(curAncients, optAncients, calcs.chorDiscount)
    if optcost['Total'] > calcs.totalSoulsAvail:
        return 'optimize'  ###can't afford +1 but can afford optimize

    maxSiya = int(floor(-1/2 + sqrt(2*((1-calcs.chorDiscount)*calcs.totalSoulsAvail) + curAncients['Siya']**2 + curAncients['Siya'] + 1/4)))  #thanks Holrik, graceoflives, Sugima for help in Discord chat
    minSiya = int(curAncients['Siya'])
    newsiya = int((maxSiya - minSiya) / 2 + minSiya)
    found = False
    while not found:
        optAncients = calcOptimalAncientLvls(curAncients, newsiya, calcs)
        optcost = calcOptCost(curAncients, optAncients, calcs.chorDiscount)
        if optcost['Total'] < calcs.totalSoulsAvail:
            minSiya = newsiya
            newsiya = int((maxSiya - minSiya) / 2 + minSiya)
        elif optcost['Total'] > calcs.totalSoulsAvail:
            maxSiya = newsiya
            newsiya = int((maxSiya - minSiya) / 2 + minSiya)
        elif optcost['Total'] == calcs.totalSoulsAvail:
            found = True
        if maxSiya == minSiya+1 or maxSiya == minSiya:
            newsiya = minSiya
            found = True
    return max(newsiya, 1)

def calcSoloMultiplier(Solomon, ponyboy):
    if Solomon < 21:
        soloMultiplier = 1 + (ponyboy + 1) * (Solomon * 0.05)
    elif Solomon < 41:
        soloMultiplier = 1 + (ponyboy + 1) * (1 + ((Solomon - 20) * 0.04))
    elif Solomon < 61:
        soloMultiplier = 1 + (ponyboy + 1) * (1.8 + ((Solomon - 40) * 0.03))
    elif Solomon < 81:
        soloMultiplier = 1 + (ponyboy + 1) * (2.4 + ((Solomon - 60) * 0.02))
    else:
        soloMultiplier = 1 + (ponyboy + 1) * (2.8 + ((Solomon - 80) * 0.01))
    return soloMultiplier

def getAncientLvlDifferences(curAncients, optAncients):
    diff = {}
    for k in curAncients.keys():
        diff[k] = max(int(optAncients[k] - curAncients[k]), 0)
        if diff[k] > 1e9:
            diff[k] = "{:.3E}".format(diff[k])
        else:
            diff[k] = "{:,}".format(diff[k])
    return diff

def theMonsterMath(input, useAscendSouls, mode, hybridMultiplier, highwep):
    global MODE, HIGHWEP
    MODE = mode
    HIGHWEP = highwep
    savedata = savedecoder.decryptSave(input)
    if savedata in ('Invalid Save File', 'Invalid Save File - bad hash'):
        return (0, 0, 0, 0, 0, savedata)
    curAncients = getCurrentAncientLvls(savedata)
    
    if curAncients['Siya'] == 0:
        return (0, 0, 0, 0, 0, 'You need to buy Siyalatas!')
    
    calcs = Calculations(savedata, hybridMultiplier)
    calcs.doTheMath(curAncients['Solomon'], useAscendSouls)
    
    optsiya = findOptSiya(curAncients, calcs)
    if optsiya == 'broke':
        optAncients = calcOptimalAncientLvls(curAncients, int(curAncients['Siya']), calcs)
        optcost = calcOptCost(curAncients, optAncients, calcs.chorDiscount)
        diff = getAncientLvlDifferences(curAncients, optAncients)
        calcs.findNewTPzone(optAncients['Solomon'], curAncients['Solomon'])
        return (prepForOutput(curAncients), prepForOutput(optAncients), diff, calcs, prepForOutput(optcost), "<h2>You can't afford to optimize your ancients right now<br>but here are the optimal levels:</h2>")
    if optsiya == 'optimize':
        optsiya = curAncients['Siya']
    
    optAncients = calcOptimalAncientLvls(curAncients, optsiya, calcs)
    optcost = calcOptCost(curAncients, optAncients, calcs.chorDiscount)
    diff = getAncientLvlDifferences(curAncients, optAncients)
    calcs.findNewTPzone(optAncients['Solomon'], curAncients['Solomon'])
    return (prepForOutput(curAncients), prepForOutput(optAncients), diff, calcs, prepForOutput(optcost), '<h2>These are the highest optimal ancient levels you can afford:</h2>')