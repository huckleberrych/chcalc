import savedecoder
from math import log, floor, ceil, exp, log10, sqrt

MODE = 'idle'

class Current(dict):

    def __init__(self, input):
        self.input = input
        self.curArgaiv = 0
        self.curAtman = 0
        self.curBhaal = 0
        self.curBubos = 0
        self.curChronos = 0
        self.curDogcog = 0
        self.curDora = 0
        self.curFrags = 0
        self.curFortuna = 0
        self.curJugs = 0
        self.curKuma = 0
        self.curLibertas = 0
        self.curMammon = 0
        self.curMimzee = 0
        self.curMorg = 0
        self.curSiya = 0
        self.curSolomon = 0

    def getCurrentAncientLvls(self):
        if self.input.get('ancients').get('ancients').get('28'):
            self.curArgaiv = float(
                 self.input['ancients']['ancients']['28']['level'])
        if self.input.get('ancients').get('ancients').get('13'):
            self.curAtman = float(
                self.input['ancients']['ancients']['13']['level'])
        if self.input.get('ancients').get('ancients').get('15'):
            self.curBhaal = float(
                self.input['ancients']['ancients']['15']['level'])
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
        if self.input.get('ancients').get('ancients').get('19'):
            self.curFrags = float(
                self.input['ancients']['ancients']['19']['level'])
        if self.input.get('ancients').get('ancients').get('12'):
            self.curFortuna = float(
                self.input['ancients']['ancients']['12']['level'])
        if self.input.get('ancients').get('ancients').get('29'):
            self.curJugs = float(
                self.input['ancients']['ancients']['29']['level'])
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
    def __init__(self, current, siya, calcs):
        self.current = current
        self.siya = siya
        self.alpha = calcs.alpha
        self.hybridMultiplier = calcs.hybridMultiplier
        self.optArgaiv = 0
        self.optAtman = 0
        self.optBhaal = 0
        self.optBubos = 0
        self.optChronos = 0
        self.optDogcog = 0
        self.optDora = 0
        self.optFrags = 0
        self.optFortuna = 0
        self.optJugs = 0
        self.optKuma = 0
        self.optLibertas = 0
        self.optMammon = 0
        self.optMimzee = 0
        self.optMorg = 0
        self.optSiya = int(siya)
        self.optSolomon = 0

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
        if MODE == 'hybrid':
            self.optBhaal = int(floor(self.siya * self.hybridMultiplier))
            self.optFrags = int(floor(self.siya * self.hybridMultiplier))
            self.optJugs = int(floor(self.optFrags ** 0.8))

    def addCommas(self):
        if self.optArgaiv > 1e9:
            self.optArgaiv = "{:.3E}".format(self.optArgaiv)
        else:
            self.optArgaiv = "{:,}".format(self.optArgaiv)
        if self.optAtman > 1e9:
            self.optAtman = "{:.3E}".format(self.optAtman)
        else:
            self.optAtman = "{:,}".format(self.optAtman)
        if self.optBhaal > 1e9:
            self.optBhaal = "{:.3E}".format(self.optBhaal)
        else:
            self.optBhaal = "{:,}".format(self.optBhaal)
        if self.optBubos > 1e9:
            self.optBubos = "{:.3E}".format(self.optBubos)
        else:
            self.optBubos = "{:,}".format(self.optBubos)
        if self.optChronos > 1e9:
            self.optChronos = "{:.3E}".format(self.optChronos)
        else:
            self.optChronos = "{:,}".format(self.optChronos)
        if self.optDogcog > 1e9:
            self.optDogcog = "{:.3E}".format(self.optDogcog)
        else:
            self.optDogcog = "{:,}".format(self.optDogcog)
        if self.optDora > 1e9:
            self.optDora = "{:.3E}".format(self.optDora)
        else:
            self.optDora = "{:,}".format(self.optDora)
        if self.optFrags > 1e9:
            self.optFrags = "{:.3E}".format(self.optFrags)
        else:
            self.optFrags = "{:,}".format(self.optFrags)
        if self.optFortuna > 1e9:
            self.optFortuna = "{:.3E}".format(self.optFortuna)
        else:
            self.optFortuna = "{:,}".format(self.optFortuna)
        if self.optJugs > 1e9:
            self.optJugs = "{:.3E}".format(self.optJugs)
        else:
            self.optJugs = "{:,}".format(self.optJugs)
        if self.optKuma > 1e9:
            self.optKuma = "{:.3E}".format(self.optKuma)
        else:
            self.optKuma = "{:,}".format(self.optKuma)
        if self.optLibertas > 1e9:
            self.optLibertas = "{:.3E}".format(self.optLibertas)
        else:
            self.optLibertas = "{:,}".format(self.optLibertas)
        if self.optMammon > 1e9:
            self.optMammon = "{:.3E}".format(self.optMammon)
        else:
            self.optMammon = "{:,}".format(self.optMammon)
        if self.optMimzee > 1e9:
            self.optMimzee = "{:.3E}".format(self.optMimzee)
        else:
            self.optMimzee = "{:,}".format(self.optMimzee)
        if self.optMorg > 1e9:
            self.optMorg = "{:.3E}".format(self.optMorg)
        else:
            self.optMorg = "{:,}".format(self.optMorg)
        if self.optSiya > 1e9:
            self.optSiya = "{:.3E}".format(self.optSiya)
        else:
            self.optSiya = "{:,}".format(self.optSiya)
        if self.optSolomon > 1e9:
            self.optSolomon = "{:.3E}".format(self.optSolomon)
        else:
            self.optSolomon = "{:,}".format(self.optSolomon)
        
        if self.current.curArgaiv > 1e9:
            self.current.curArgaiv = "{:.3E}".format(self.current.curArgaiv)
        else:
            self.current.curArgaiv = "{:,}".format(int(self.current.curArgaiv))
        if self.current.curAtman > 1e9:
            self.current.curAtman = "{:.3E}".format(self.current.curAtman)
        else:
            self.current.curAtman = "{:,}".format(int(self.current.curAtman))
        if self.current.curBhaal > 1e9:
            self.current.curBhaal = "{:.3E}".format(self.current.curBhaal)
        else:
            self.current.curBhaal = "{:,}".format(int(self.current.curBhaal))
        if self.current.curBubos > 1e9:
            self.current.curBubos = "{:.3E}".format(self.current.curBubos)
        else:
            self.current.curBubos = "{:,}".format(int(self.current.curBubos))
        if self.current.curChronos > 1e9:
            self.current.curChronos = "{:.3E}".format(self.current.curChronos)
        else:
            self.current.curChronos = "{:,}".format(int(self.current.curChronos))
        if self.current.curDogcog > 1e9:
            self.current.curDogcog = "{:.3E}".format(self.current.curDogcog)
        else:
            self.current.curDogcog = "{:,}".format(int(self.current.curDogcog))
        if self.current.curDora > 1e9:
            self.current.curDora = "{:.3E}".format(self.current.curDora)
        else:
            self.current.curDora = "{:,}".format(int(self.current.curDora))
        if self.current.curFrags > 1e9:
            self.current.curFrags = "{:.3E}".format(self.current.curFrags)
        else:
            self.current.curFrags = "{:,}".format(int(self.current.curFrags))
        if self.current.curFortuna > 1e9:
            self.current.curFortuna = "{:.3E}".format(self.current.curFortuna)
        else:
            self.current.curFortuna = "{:,}".format(int(self.current.curFortuna))
        if self.current.curJugs > 1e9:
            self.current.curJugs = "{:.3E}".format(self.current.curJugs)
        else:
            self.current.curJugs = "{:,}".format(int(self.current.curJugs))
        if self.current.curKuma > 1e9:
            self.current.curKuma = "{:.3E}".format(self.current.curKuma)
        else:
            self.current.curKuma = "{:,}".format(int(self.current.curKuma))
        if self.current.curLibertas > 1e9:
            self.current.curLibertas = "{:.3E}".format(self.current.curLibertas)
        else:
            self.current.curLibertas = "{:,}".format(int(self.current.curLibertas))
        if self.current.curMammon > 1e9:
            self.current.curMammon = "{:.3E}".format(self.current.curMammon)
        else:
            self.current.curMammon = "{:,}".format(int(self.current.curMammon))
        if self.current.curMimzee > 1e9:
            self.current.curMimzee = "{:.3E}".format(self.current.curMimzee)
        else:
            self.current.curMimzee = "{:,}".format(int(self.current.curMimzee))
        if self.current.curMorg > 1e9:
            self.current.curMorg = "{:.3E}".format(self.current.curMorg)
        else:
            self.current.curMorg = "{:,}".format(int(self.current.curMorg))
        if self.current.curSiya > 1e9:
            self.current.curSiya = "{:.3E}".format(self.current.curSiya)
        else:
            self.current.curSiya = "{:,}".format(int(self.current.curSiya))
        if self.current.curSolomon > 1e9:
            self.current.curSolomon = "{:.3E}".format(self.current.curSolomon)
        else:
            self.current.curSolomon = "{:,}".format(int(self.current.curSolomon))

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
        
    def doTheMath(self, curSolomon, useAscendSouls):
        if self.savedata.get("ancientSoulsTotal"):
            self.AS = self.savedata["ancientSoulsTotal"]
        if self.savedata.get('outsiders'):
            self.xyl = self.savedata['outsiders']['outsiders']['1']['level']
            self.chor = self.savedata['outsiders']['outsiders']['2']['level']
            self.phan = self.savedata['outsiders']['outsiders']['3']['level']
            self.borb = self.savedata['outsiders']['outsiders']['4']['level']
            self.pony = self.savedata['outsiders']['outsiders']['5']['level']
            self.tp = 1 - 0.49 * exp(-self.AS/10000.0) - 0.5 * exp(-self.phan/1000.0)
            self.soloMultiplier = calcSoloMultiplier(curSolomon, self.pony)
        self.ascendZone = self.savedata["highestFinishedZonePersist"]
        self.alpha = 1.4067 * log(1 + self.tp * 1) / log(ceil(self.ascendZone / 500.0) * 0.005 + 1.14)
        self.totalSoulsAvail = float(self.savedata["heroSouls"])
        if useAscendSouls == 'on':
            self.totalSoulsAvail += float(self.savedata["primalSouls"])
        if self.savedata.get('outsiders'):
            self.chorDiscount = 1 - 0.95 ** self.chor
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

def calcOptCost(curAncients, optAncients, chorDiscount):
    #optCost = 0
    optCost = {'Argaiv':0, 'Atman':0, 'Bhaal': 0, 'Bubos':0,
               'Chronos':0, 'Dogcog':0, 'Dora':0, 'Frags': 0,
               'Fortuna':0, 'Jugs':0, 'Kuma':0, 'Libertas':0,
               'Mammon':0, 'Mimzee':0, 'Morg':0, 'Siya':0,
               'Solomon':0}
    if optAncients.optArgaiv > curAncients.curArgaiv:
        optCost['Argaiv'] = int(ceil((1 - chorDiscount)*(0.5*(optAncients.optArgaiv)*(optAncients.optArgaiv+2)-0.5*curAncients.curArgaiv*(curAncients.curArgaiv+2))))
    if optAncients.optAtman > curAncients.curAtman:
        optCost['Atman'] = int(ceil(((1-chorDiscount)*((2**(optAncients.optAtman+1)-1)-(2**(curAncients.curAtman+1)-1)))))
    if optAncients.optBhaal > curAncients.curBhaal:
        optCost['Bhaal'] = int(ceil((1 - chorDiscount)*(0.5*(optAncients.optBhaal)*(optAncients.optBhaal+2)-0.5*curAncients.curBhaal*(curAncients.curBhaal+2))))
    if optAncients.optBubos > curAncients.curBubos:
        optCost['Bubos'] = int(ceil(((1-chorDiscount)*((2**(optAncients.optBubos+1)-1)-(2**(curAncients.curBubos+1)-1)))))
    if optAncients.optChronos > curAncients.curChronos:
        optCost['Chronos'] = int(ceil(((1-chorDiscount)*((2**(optAncients.optChronos+1)-1)-(2**(curAncients.curChronos+1)-1)))))
    if optAncients.optDogcog > curAncients.curDogcog:
        optCost['Dogcog'] = int(ceil(((1-chorDiscount)*((2**(optAncients.optDogcog+1)-1)-(2**(curAncients.curDogcog+1)-1)))))
    if optAncients.optDora > curAncients.curDora:
        optCost['Dora'] = int(ceil(((1-chorDiscount)*((2**(optAncients.optDora+1)-1)-(2**(curAncients.curDora+1)-1)))))
    if optAncients.optFrags > curAncients.curFrags:
        optCost['Frags'] = int(ceil((1 - chorDiscount)*(0.5*(optAncients.optFrags)*(optAncients.optFrags+2)-0.5*curAncients.curFrags*(curAncients.curFrags+2))))
    if optAncients.optFortuna > curAncients.curFortuna:
        optCost['Fortuna'] = int(ceil(((1-chorDiscount)*((2**(optAncients.optFortuna+1)-1)-(2**(curAncients.curFortuna+1)-1)))))
    if optAncients.optJugs > curAncients.curJugs:
        optCost['Jugs'] = int(ceil((1-chorDiscount)*(ceil((0.4*optAncients.optJugs**2.5)-(0.4*curAncients.curJugs**2.5)))))
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
    for k in optCost:
        if k != 'Total' and optCost[k] > 1e9:
            optCost[k] = "{:.3E}".format(optCost[k])
        elif k != 'Total':
            optCost[k] = "{:,}".format(optCost[k])
    return optCost

def findOptSiya(curAncients, calcs):
    
    ##check if they can afford to optimize
    optAncients = Optimal(curAncients, curAncients.curSiya, calcs)
    optAncients.calcOptimalAncientLvls()
    optcost = calcOptCost(curAncients, optAncients, calcs.chorDiscount)
    if optcost['Total'] > calcs.totalSoulsAvail:
        return 'broke'  ###can't afford to optimize
    
    ##check if they can afford +1 siya
    optAncients = Optimal(curAncients, curAncients.curSiya + 1, calcs)
    optAncients.calcOptimalAncientLvls()
    optcost = calcOptCost(curAncients, optAncients, calcs.chorDiscount)
    if optcost['Total'] > calcs.totalSoulsAvail:
        return 'optimize'  ###can't afford +1 but can afford optimize

    maxSiya = int(floor(-1/2 + sqrt(2*((1-calcs.chorDiscount)*calcs.totalSoulsAvail) + curAncients.curSiya**2 + curAncients.curSiya + 1/4)))  #thanks Holrik, graceoflives, Sugima for help in Discord chat
    minSiya = int(curAncients.curSiya)
    newsiya = int((maxSiya - minSiya) / 2 + minSiya)
    found = False
    while not found:
        optAncients = Optimal(curAncients, newsiya, calcs)
        optAncients.calcOptimalAncientLvls()
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
    diff['Argaiv'] = max(int(optAncients.optArgaiv - curAncients.curArgaiv), 0)
    diff['Atman'] = max(int(optAncients.optAtman - curAncients.curAtman), 0)
    diff['Bhaal'] = max(int(optAncients.optBhaal - curAncients.curBhaal), 0)
    diff['Bubos'] = max(int(optAncients.optBubos - curAncients.curBubos), 0)
    diff['Chronos'] = max(int(optAncients.optChronos - curAncients.curChronos), 0)
    diff['Dogcog'] = max(int(optAncients.optDogcog - curAncients.curDogcog), 0)
    diff['Dora'] = max(int(optAncients.optDora - curAncients.curDora), 0)
    diff['Frags'] = max(int(optAncients.optFrags - curAncients.curFrags), 0)
    diff['Fortuna'] = max(int(optAncients.optFortuna - curAncients.curFortuna), 0)
    diff['Jugs'] = max(int(optAncients.optJugs - curAncients.curJugs), 0)
    diff['Kuma'] = max(int(optAncients.optKuma - curAncients.curKuma), 0)
    diff['Libertas'] = max(int(optAncients.optLibertas - curAncients.curLibertas), 0)
    diff['Mammon'] = max(int(optAncients.optMammon - curAncients.curMammon), 0)
    diff['Mimzee'] = max(int(optAncients.optMimzee - curAncients.curMimzee), 0)
    diff['Morg'] = max(int(optAncients.optMorg - curAncients.curMorg), 0)
    diff['Siya'] = max(int(optAncients.optSiya - curAncients.curSiya), 0)
    diff['Solomon'] = max(int(optAncients.optSolomon - curAncients.curSolomon), 0)
    for k in diff:
        if diff[k] > 1e9:
            diff[k] = "{:.3E}".format(diff[k])
        else:
            diff[k] = "{:,}".format(diff[k])
    return diff

def theMonsterMath(input, useAscendSouls, mode, hybridMultiplier):
    global MODE
    MODE = mode
    savedata = savedecoder.decryptSave(input)
    if savedata in ('Invalid Save File', 'Invalid Save File - bad hash'):
        return (0, 0, 0, 0, savedata)
    curAncients = Current(savedata)
    curAncients.getCurrentAncientLvls()
    
    if curAncients.curSiya == 0:
        return (0, 0, 0, 0, 'You need to buy Siyalatas!')
    
    calcs = Calculations(savedata, hybridMultiplier)
    calcs.doTheMath(curAncients.curSolomon, useAscendSouls)
    
    optsiya = findOptSiya(curAncients, calcs)
    if optsiya == 'broke':
        optAncients = Optimal(curAncients, int(curAncients.curSiya), calcs)
        optAncients.calcOptimalAncientLvls()
        optcost = calcOptCost(curAncients, optAncients, calcs.chorDiscount)
        if optcost['Total'] > 1e9:
            optcost['Total'] = "{:.3E}".format(optcost['Total'])
        else:
            optcost['Total'] = "{:,}".format(optcost['Total'])
        diff = getAncientLvlDifferences(curAncients, optAncients)
        calcs.findNewTPzone(optAncients.optSolomon, curAncients.curSolomon)
        optAncients.addCommas()
        return (optAncients, diff, calcs, optcost, "<h2>You can't afford to optimize your ancients right now<br>but here are the optimal levels:</h2>")
    if optsiya == 'optimize':
        optsiya = curAncients.curSiya
    
    optAncients = Optimal(curAncients, optsiya, calcs)
    optAncients.calcOptimalAncientLvls()
    optcost = calcOptCost(curAncients, optAncients, calcs.chorDiscount)
    if optcost['Total'] > 1e9:
        optcost['Total'] = "{:.3E}".format(optcost['Total'])
    else:
        optcost['Total'] = "{:,}".format(optcost['Total'])
    diff = getAncientLvlDifferences(curAncients, optAncients)
    calcs.findNewTPzone(optAncients.optSolomon, curAncients.curSolomon)
    optAncients.addCommas()
    return (optAncients, diff, calcs, optcost, '<h2>These are the highest optimal ancient levels you can afford:</h2>')