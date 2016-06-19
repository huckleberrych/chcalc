import savedecoder
from math import log, floor, ceil, exp, log10

class Current(dict):

    def __init__(self, input, curArgaiv=0, curAtman=0, curBubos=0,
                 curChronos=0, curDogcog=0, curDora=0, curFortuna=0,
                 curKuma=0, curLibertas=0, curMammon=0, curMimzee=0,
                 curMorg=0, curSiya=0, curSolomon=0):
        self.input = input
        self.curArgaiv = curArgaiv
        self.curAtman = curAtman
        self.curBubos = curBubos
        self.curChronos = curChronos
        self.curDogcog = curDogcog
        self.curDora = curDora
        self.curFortuna = curFortuna
        self.curKuma = curKuma
        self.curLibertas = curLibertas
        self.curMammon = curMammon
        self.curMimzee = curMimzee
        self.curMorg = curMorg
        self.curSiya = curSiya
        self.curSolomon = curSolomon

    def getCurrentAncientLvls(self):
        if self.input.get('ancients').get('ancients').get('28'):
            self.curArgaiv = float(
                 self.input['ancients']['ancients']['28']['level'])
        if self.input.get('ancients').get('ancients').get('13'):
            self.curAtman = float(
                self.input['ancients']['ancients']['13']['level'])
        if self.input.get('ancients').get('ancients').get('18'):
            self.curBubos = float(
                self.input['ancients']['ancients']['18']['level'])
        if self.input.get('ancients').get('ancients').get('17'):
            self.curChronos = float(
                self.input['ancients']['ancients']['17']['level'])
        if self.input.get('ancients').get('ancients').get('11'):
            self.curDogcog = float(
                self.input['ancients']['ancients']['11']['level'])
        if self.input.get('ancients').get('ancients').get('14'):
            self.curDora = float(
                self.input['ancients']['ancients']['14']['level'])
        if self.input.get('ancients').get('ancients').get('12'):
            self.curFortuna = float(
                self.input['ancients']['ancients']['12']['level'])
        if self.input.get('ancients').get('ancients').get('21'):
            self.curKuma = float(
                self.input['ancients']['ancients']['21']['level'])
        if self.input.get('ancients').get('ancients').get('4'):
            self.curLibertas = float(
                self.input['ancients']['ancients']['4']['level'])
        if self.input.get('ancients').get('ancients').get('8'):
            self.curMammon = float(
                self.input['ancients']['ancients']['8']['level'])
        if self.input.get('ancients').get('ancients').get('9'):
            self.curMimzee = float(
                self.input['ancients']['ancients']['9']['level'])
        if self.input.get('ancients').get('ancients').get('16'):
            self.curMorg = float(
                self.input['ancients']['ancients']['16']['level'])
        if self.input.get('ancients').get('ancients').get('5'):
            self.curSiya = float(
                self.input['ancients']['ancients']['5']['level'])
        if self.input.get('ancients').get('ancients').get('3'):
            self.curSolomon = float(
                self.input['ancients']['ancients']['3']['level'])

class Optimal(dict):
    def __init__(self, current, siya, alpha, optArgaiv=0, optAtman=0,
                 optBubos=0, optChronos=0, optDogcog=0, optDora=0,
                 optFortuna=0, optKuma=0, optLibertas=0, optMammon=0,
                 optMimzee=0, optMorg=0, optSiya=0, optSolomon=0):
        self.current = current
        self.siya = siya
        self.alpha = alpha
        self.optArgaiv = optArgaiv
        self.optAtman = optAtman
        self.optBubos = optBubos
        self.optChronos = optChronos
        self.optDogcog = optDogcog
        self.optDora = optDora
        self.optFortuna = optFortuna
        self.optKuma = optKuma
        self.optLibertas = optLibertas
        self.optMammon = optMammon
        self.optMimzee = optMimzee
        self.optMorg = optMorg
        self.optSiya = int(siya)
        self.optSolomon = optSolomon

    def calcOptimalAncientLvls(self):
        self.optArgaiv = int(self.siya)
        if self.alpha != 0:
            self.optAtman = int(
                floor(2.832*log(self.siya)
                - 1.416*log(self.alpha)
                - 1.416*log(4.0/3-exp(-0.013*int(self.current.curAtman)))
                -6.613)
                )
            self.optBubos = int(
                floor(2.8*log(self.siya)
                - 1.4*log(1+exp(-0.02*int(self.current.curBubos)))
                - 5.94)
                )
            self.optChronos = int(
                floor(2.75*log(self.siya)
                - 1.375*log(2-exp(-0.034*int(self.current.curChronos)))
                - 5.1)
                )
            self.optDogcog = int(
                floor(2.844*log(self.siya)
                - 1.422*log(1.0/99 + exp((-0.01)*int(self.current.curDogcog)))
                - 7.232)
                )
            self.optDora = int(
                floor(2.877*log(self.siya)
                - 1.4365*log(100.0/99-exp(-0.002*int(self.current.curDora)))
                - 9.63)
                )
            self.optFortuna = int(
                floor(2.875*log(self.siya)
                - 1.4375*log(10.0/9-exp(-0.0025*int(self.current.curFortuna)))
                - 9.3)
                )
            self.optKuma = int(
                floor(2.844*log(self.siya)
                - 1.422*log(self.alpha)
                - 1.422*log(0.25 + exp(-0.01*int(self.current.curKuma)))
                - 7.014)
                )
            self.optLibertas = int(floor(0.926*self.siya))
            self.optMammon = int(floor(0.926*self.siya))
            self.optMimzee = int(floor(0.926*self.siya))
            self.optMorg = int(float(self.siya ** 2))
            self.optSolomon = int(floor(self.siya**(0.8)/self.alpha**0.4))

    def addCommas(self):
        self.optArgaiv = "{:,}".format(self.optArgaiv)
        self.optAtman = "{:,}".format(self.optAtman)
        self.optBubos = "{:,}".format(self.optBubos)
        self.optChronos = "{:,}".format(self.optChronos)
        self.optDogcog = "{:,}".format(self.optDogcog)
        self.optDora = "{:,}".format(self.optDora)
        self.optFortuna = "{:,}".format(self.optFortuna)
        self.optKuma = "{:,}".format(self.optKuma)
        self.optLibertas = "{:,}".format(self.optLibertas)
        self.optMammon = "{:,}".format(self.optMammon)
        self.optMimzee = "{:,}".format(self.optMimzee)
        self.optMorg = "{:,}".format(self.optMorg)
        self.optSiya = "{:,}".format(self.optSiya)
        self.optSolomon = "{:,}".format(self.optSolomon)
        self.current.curArgaiv = "{:,}".format(int(self.current.curArgaiv))
        self.current.curAtman = "{:,}".format(int(self.current.curAtman))
        self.current.curBubos = "{:,}".format(int(self.current.curBubos))
        self.current.curChronos = "{:,}".format(int(self.current.curChronos))
        self.current.curDogcog = "{:,}".format(int(self.current.curDogcog))
        self.current.curDora = "{:,}".format(int(self.current.curDora))
        self.current.curFortuna = "{:,}".format(int(self.current.curFortuna))
        self.current.curKuma = "{:,}".format(int(self.current.curKuma))
        self.current.curLibertas = "{:,}".format(int(self.current.curLibertas))
        self.current.curMammon = "{:,}".format(int(self.current.curMammon))
        self.current.curMimzee = "{:,}".format(int(self.current.curMimzee))
        self.current.curMorg = "{:,}".format(int(self.current.curMorg))
        self.current.curSiya = "{:,}".format(int(self.current.curSiya))
        self.current.curSolomon = "{:,}".format(int(self.current.curSolomon))
        

class Calculations(dict):
    
    def __init__(self, savedata, AS=0, tp=0, ascendZone=0, alpha=0,
                 totalSoulsAvail=0, chorDiscount=0, maxTPreward=0,
                 soloMultiplier=1, maxTPzone=0, newTPzone=0,
                 newSoloMultiplier=1):
        self.savedata = savedata
        self.AS = AS
        self.tp = tp
        self.ascendZone = ascendZone
        self.alpha = alpha
        self.totalSoulsAvail = totalSoulsAvail
        self.chorDiscount = chorDiscount
        self.maxTPreward = maxTPreward
        self.soloMultiplier = soloMultiplier
        self.maxTPzone = maxTPzone
        self.newTPzone = newTPzone
        self.newSoloMultiplier = newSoloMultiplier
        
    def doTheMath(self, curSolomon, useAscendSouls):
        if self.savedata.get("ancientSoulsTotal"):
            self.AS = self.savedata["ancientSoulsTotal"]
        if self.savedata.get('outsiders'):
            self.tp = (50 - 49 * (exp(-self.AS/10000.0))) / 100 + .0005 * int(self.savedata['outsiders']['outsiders']['3']['level'])
        self.ascendZone = self.savedata["highestFinishedZonePersist"]
        self.alpha = 1.4067 * log(1 + self.tp * 1) / log(ceil(self.ascendZone / 500.0) * 0.005 + 1.14)
        self.totalSoulsAvail = float(self.savedata["heroSouls"])
        if useAscendSouls == 'on':
            self.totalSoulsAvail += float(self.savedata["primalSouls"])
        if self.savedata.get('outsiders'):
            self.chorDiscount = 1 - 0.95 ** int(self.savedata['outsiders']['outsiders']['2']['level'])
        if self.savedata.get("heroSoulsSacrificed"):
            self.maxTPreward = float(self.savedata["heroSoulsSacrificed"]) * (0.05 + (int(self.savedata['outsiders']['outsiders']['4']['level']) * 0.005))
        if self.savedata.get('outsiders'):
            self.soloMultiplier = calcSoloMultiplier(curSolomon, self.savedata['outsiders']['outsiders']['5']['level'])
        if self.maxTPreward != 0:
            self.maxTPzone = int((ceil((log(self.maxTPreward / (20 * self.soloMultiplier))) / (log(1 + self.tp))) * 5) + 100)
            
    def findNewTPzone(self, optSolomon, curSolomon):
        #ancient levels have decimals, must check vs our opt (always x.0) so if opt = +0 then maxTPzone = newTPzone
        if floor(optSolomon) != floor(curSolomon) and ceil(optSolomon) != ceil(curSolomon):
            if self.savedata.get('outsiders'):
                self.newSoloMultiplier = calcSoloMultiplier(optSolomon, self.savedata['outsiders']['outsiders']['5']['level'])
            if self.maxTPreward != 0:
                self.newTPzone = int((ceil((log(self.maxTPreward / (20 * self.newSoloMultiplier))) / (log(1 + self.tp))) * 5) + 100)
        else:
            self.newTPzone = self.maxTPzone

def calcOptCost(curAncients, optAncients, chorDiscount):
    #optCost = 0
    optCost = {'Argaiv':0, 'Atman':0, 'Bubos':0, 'Chronos':0,
               'Dogcog':0, 'Dora':0, 'Fortuna':0, 'Kuma':0,
               'Libertas':0, 'Mammon':0, 'Mimzee':0, 'Morg':0,
               'Siya':0, 'Solomon':0}
    if optAncients.optArgaiv > curAncients.curArgaiv:
        optCost['Argaiv'] = int(ceil((1 - chorDiscount)*(0.5*(optAncients.optArgaiv)*(optAncients.optArgaiv+2)-0.5*curAncients.curArgaiv*(curAncients.curArgaiv+2))))
    if optAncients.optAtman > curAncients.curAtman:
        optCost['Atman'] = int(ceil(((1-chorDiscount)*((2**(optAncients.optAtman+1)-1)-(2**(curAncients.curAtman+1)-1)))))
    if optAncients.optBubos > curAncients.curBubos:
        optCost['Bubos'] = int(ceil(((1-chorDiscount)*((2**(optAncients.optBubos+1)-1)-(2**(curAncients.curBubos+1)-1)))))
    if optAncients.optChronos > curAncients.curChronos:
        optCost['Chronos'] = int(ceil(((1-chorDiscount)*((2**(optAncients.optChronos+1)-1)-(2**(curAncients.curChronos+1)-1)))))
    if optAncients.optDogcog > curAncients.curDogcog:
        optCost['Dogcog'] = int(ceil(((1-chorDiscount)*((2**(optAncients.optDogcog+1)-1)-(2**(curAncients.curDogcog+1)-1)))))
    if optAncients.optDora > curAncients.curDora:
        optCost['Dora'] = int(ceil(((1-chorDiscount)*((2**(optAncients.optDora+1)-1)-(2**(curAncients.curDora+1)-1)))))
    if optAncients.optFortuna > curAncients.curFortuna:
        optCost['Fortuna'] = int(ceil(((1-chorDiscount)*((2**(optAncients.optFortuna+1)-1)-(2**(curAncients.curFortuna+1)-1)))))
    if optAncients.optKuma > curAncients.curKuma:
        optCost['Kuma'] = int(ceil(((1-chorDiscount)*((2**(optAncients.optKuma+1)-1)-(2**(curAncients.curKuma+1)-1)))))
    if optAncients.optLibertas > curAncients.curLibertas:
        optCost['Libertas'] = int(ceil((1-chorDiscount)*(0.5*(optAncients.optLibertas)*(optAncients.optLibertas+2)-0.5*curAncients.curLibertas*(curAncients.curLibertas+2))))
    if optAncients.optMammon > curAncients.curMammon:
        optCost['Mammon'] = int(ceil((1-chorDiscount)*(0.5*(optAncients.optMammon)*(optAncients.optMammon+2)-0.5*curAncients.curMammon*(curAncients.curMammon+2))))
    if optAncients.optMimzee > curAncients.curMimzee:
        optCost['Mimzee'] = int(ceil((1-chorDiscount)*(0.5*(optAncients.optMimzee)*(optAncients.optMimzee+2)-0.5*curAncients.curMimzee*(curAncients.curMimzee+2))))
    if optAncients.optMorg > curAncients.curMorg:
        optCost['Morg'] = int(ceil((1-chorDiscount)*(optAncients.optMorg-curAncients.curMorg)))
    if optAncients.optSiya > curAncients.curSiya:
        optCost['Siya'] = int(ceil((1-chorDiscount)*(0.5*(optAncients.optSiya)*(optAncients.optSiya+2)-0.5*curAncients.curSiya*(curAncients.curSiya+2))))
    if optAncients.optSolomon > curAncients.curSolomon:
        optCost['Solomon'] = int(ceil((1-chorDiscount)*(ceil((0.4*optAncients.optSolomon**2.5)-(0.4*curAncients.curSolomon**2.5)))))
    optCost['Total'] = sum(optCost.itervalues())
    optCost['Argaiv'] = "{:,}".format(optCost['Argaiv'])
    optCost['Atman'] = "{:,}".format(optCost['Atman'])
    optCost['Bubos'] = "{:,}".format(optCost['Bubos'])
    optCost['Chronos'] = "{:,}".format(optCost['Chronos'])
    optCost['Dogcog'] = "{:,}".format(optCost['Dogcog'])
    optCost['Dora'] = "{:,}".format(optCost['Dora'])
    optCost['Fortuna'] = "{:,}".format(optCost['Fortuna'])
    optCost['Kuma'] = "{:,}".format(optCost['Kuma'])
    optCost['Libertas'] = "{:,}".format(optCost['Libertas'])
    optCost['Mammon'] = "{:,}".format(optCost['Mammon'])
    optCost['Mimzee'] = "{:,}".format(optCost['Mimzee'])
    optCost['Morg'] = "{:,}".format(optCost['Morg'])
    optCost['Siya'] = "{:,}".format(optCost['Siya'])
    optCost['Solomon'] = "{:,}".format(optCost['Solomon'])
    return optCost

def findOptSiya(curAncients, calcs):
    
    ##check if they can afford to optimize
    optAncients = Optimal(curAncients, curAncients.curSiya, calcs.alpha)
    optAncients.calcOptimalAncientLvls()
    optcost = calcOptCost(curAncients, optAncients, calcs.chorDiscount)
    if optcost['Total'] > calcs.totalSoulsAvail:
        return 'broke'  ###can't afford to optimize
    
    ##check if they can afford +1 siya
    optAncients = Optimal(curAncients, curAncients.curSiya + 1, calcs.alpha)
    optAncients.calcOptimalAncientLvls()
    optcost = calcOptCost(curAncients, optAncients, calcs.chorDiscount)
    if optcost['Total'] > calcs.totalSoulsAvail:
        return 'optimize'  ###can't afford +1 but can afford optimize
    
    ##
    newsiya = curAncients.curSiya
    while optcost['Total'] <= calcs.totalSoulsAvail:
        newsiya += 1
        optAncients = Optimal(curAncients, newsiya, calcs.alpha)
        optAncients.calcOptimalAncientLvls()
        optcost = calcOptCost(curAncients, optAncients, calcs.chorDiscount)
    return max(newsiya - 1, 1) #if they don't have siya, this will return negative and break program. result must be >= 1
    
def calcSoloMultiplier(curSolomon, ponyboy):                                        ##success!
    if curSolomon < 21:
        soloMultiplier = 1 + (ponyboy + 1) * (curSolomon * 0.05)
    elif curSolomon < 41:
        soloMultiplier = 1 + (ponyboy + 1) * (1 + ((curSolomon - 20) * 0.04))
    elif curSolomon < 61:
        soloMultiplier = 1 + (ponyboy + 1) * (1.8 + ((curSolomon - 40) * 0.03))
    elif curSolomon < 81:
        soloMultiplier = 1 + (ponyboy + 1) * (2.4 + ((curSolomon - 60) * 0.02))
    else:
        soloMultiplier = 1 + (2.8 + ((curSolomon - 80) * 0.01)) * (ponyboy + 1)
    return soloMultiplier

def getAncientLvlDifferences(curAncients, optAncients):
    diff = {}
    diff['Argaiv'] = "{:,}".format(max(int(optAncients.optArgaiv - curAncients.curArgaiv), 0))
    diff['Atman'] = "{:,}".format(max(int(optAncients.optAtman - curAncients.curAtman), 0))
    diff['Bubos'] = "{:,}".format(max(int(optAncients.optBubos - curAncients.curBubos), 0))
    diff['Chronos'] = "{:,}".format(max(int(optAncients.optChronos - curAncients.curChronos), 0))
    diff['Dogcog'] = "{:,}".format(max(int(optAncients.optDogcog - curAncients.curDogcog), 0))
    diff['Dora'] = "{:,}".format(max(int(optAncients.optDora - curAncients.curDora), 0))
    diff['Fortuna'] = "{:,}".format(max(int(optAncients.optFortuna - curAncients.curFortuna), 0))
    diff['Kuma'] = "{:,}".format(max(int(optAncients.optKuma - curAncients.curKuma), 0))
    diff['Libertas'] = "{:,}".format(max(int(optAncients.optLibertas - curAncients.curLibertas), 0))
    diff['Mammon'] = "{:,}".format(max(int(optAncients.optMammon - curAncients.curMammon), 0))
    diff['Mimzee'] = "{:,}".format(max(int(optAncients.optMimzee - curAncients.curMimzee), 0))
    diff['Morg'] = "{:,}".format(max(int(optAncients.optMorg - curAncients.curMorg), 0))
    diff['Siya'] = "{:,}".format(max(int(optAncients.optSiya - curAncients.curSiya), 0))
    diff['Solomon'] = "{:,}".format(max(int(optAncients.optSolomon - curAncients.curSolomon), 0))
    return diff

def theMonsterMath(input, useAscendSouls):
    savedata = savedecoder.decryptSave(input)
    if savedata in ('Invalid Save File', 'Invalid Save File - bad hash'):
        return (0, 0, 0, 0, savedata)
    curAncients = Current(savedata)
    curAncients.getCurrentAncientLvls()
    
    if curAncients.curSiya == 0:
        return (0, 0, 0, 0, 'You need to buy Siyalatas!')
    
    calcs = Calculations(savedata)
    calcs.doTheMath(curAncients.curSolomon, useAscendSouls)
    
    optsiya = findOptSiya(curAncients, calcs)
    if optsiya == 'broke':
        optAncients = Optimal(curAncients, int(curAncients.curSiya), calcs.alpha)
        optAncients.calcOptimalAncientLvls()
        optcost = calcOptCost(curAncients, optAncients, calcs.chorDiscount)
        diff = getAncientLvlDifferences(curAncients, optAncients)
        calcs.findNewTPzone(optAncients.optSolomon, curAncients.curSolomon)
        optAncients.addCommas()
        return (optAncients, diff, calcs, optcost, "<h2>You can't afford to optimize your ancients right now<br>but here are the optimal levels:</h2>")
    if optsiya == 'optimize':
        optsiya = curAncients.curSiya
    
    optAncients = Optimal(curAncients, optsiya, calcs.alpha)
    optAncients.calcOptimalAncientLvls()
    optcost = calcOptCost(curAncients, optAncients, calcs.chorDiscount)
    optcost['Total'] = "{:,}".format(optcost['Total'])
    diff = getAncientLvlDifferences(curAncients, optAncients)
    calcs.findNewTPzone(optAncients.optSolomon, curAncients.curSolomon)
    optAncients.addCommas()
    return (optAncients, diff, calcs, optcost, '<h2>These are the highest optimal ancient levels you can afford:</h2>')