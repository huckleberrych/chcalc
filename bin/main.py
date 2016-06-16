import savedecoder
from math import log, floor, ceil, exp, log10

class Current(dict):

    def __init__(self, input, curArgaiv=0, curAtman=0, curBubos=0, curChronos=0,
                 curDogcog=0, curDora=0, curFortuna=0, curKuma=0,
                 curLibertas=0, curMammon=0, curMimzee=0, curMorg=0,
                 curSiya=0, curSolomon=0):
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
        self.curArgaiv = float(self.input['ancients']['ancients']['28']['level'])
        self.curAtman = float(self.input['ancients']['ancients']['13']['level'])
        self.curBubos = float(self.input['ancients']['ancients']['18']['level'])
        self.curChronos = float(self.input['ancients']['ancients']['17']['level'])
        self.curDogcog = float(self.input['ancients']['ancients']['11']['level'])
        self.curDora = float(self.input['ancients']['ancients']['14']['level'])
        self.curFortuna = float(self.input['ancients']['ancients']['12']['level'])
        self.curKuma = float(self.input['ancients']['ancients']['21']['level'])
        self.curLibertas = float(self.input['ancients']['ancients']['4']['level'])
        self.curMammon = float(self.input['ancients']['ancients']['8']['level'])
        self.curMimzee = float(self.input['ancients']['ancients']['9']['level'])
        self.curMorg = float(self.input['ancients']['ancients']['16']['level'])
        self.curSiya = float(self.input['ancients']['ancients']['5']['level'])
        self.curSolomon = float(self.input['ancients']['ancients']['3']['level'])

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
        self.optSiya = siya
        self.optSolomon = optSolomon

    def calcOptimalAncientLvls(self):
        self.optArgaiv = int(self.siya)
        self.optAtman = int(floor(2.832*log(self.siya) - 1.416*log(self.alpha) - 1.416*log(4.0/3-exp(-0.013*int(self.current.curAtman))) -6.613))
        self.optBubos = int(floor(2.8*log(self.siya) - 1.4*log(1+exp(-0.02*int(self.current.curBubos))) - 5.94))
        self.optChronos = int(floor(2.75*log(self.siya) - 1.375*log(2-exp(-0.034*int(self.current.curChronos))) - 5.1))
        self.optDogcog = int(floor(2.844*log(self.siya) - 1.422*log(1.0/99 + exp((-0.01)*int(self.current.curDogcog))) - 7.232))
        self.optDora = int(floor(2.877*log(self.siya) - 1.4365*log(100.0/99-exp(-0.002*int(self.current.curDora))) - 9.63))
        self.optFortuna = int(floor(2.875*log(self.siya) - 1.4375*log(10.0/9-exp(-0.0025*int(self.current.curFortuna))) - 9.3))
        self.optKuma = int(floor(2.88*log(self.siya) - 1.44*log(self.alpha) - 1.44*log(0.25+exp(-0.001*int(self.current.curKuma))) - 10.42))
        self.optLibertas = int(floor(0.926*self.siya))
        self.optMammon = int(floor(0.926*self.siya))
        self.optMimzee = int(floor(0.926*self.siya))
        self.optMorg = int(float(self.siya ** 2))
        self.optSolomon = int(floor(self.siya**(0.8)/self.alpha**0.4))

class Calculations(dict):
    
    def __init__(self, savedata, AS=0, tp=0, ascendZone=0, alpha=0, totalSoulsAvail=0, chorDiscount=0):
        self.savedata = savedata
        self.AS = AS
        self.tp = tp
        self.ascendZone = ascendZone
        self.alpha = alpha
        self.totalSoulsAvail = totalSoulsAvail
        self.chorDiscount = chorDiscount
        
    def doTheMath(self):
        self.AS = floor(5 * log10(float(self.savedata["heroSoulsSacrificed"])))  #or self.AS = self.savedata["ancientSoulsTotal"]
        self.tp = (50-49*(exp(-self.AS/10000.0))) * (1 + .05*int(self.savedata['outsiders']['outsiders']['4']['level']))/100
        self.ascendZone = self.savedata["highestFinishedZonePersist"]
        self.alpha = 1.4067*log(1+self.tp*1)/log(ceil(self.ascendZone/500.0)*0.005+1.14)
        self.totalSoulsAvail = float(self.savedata["heroSouls"]) + float(self.savedata["primalSouls"])
        self.chorDiscount = 1-0.95**int(self.savedata['outsiders']['outsiders']['2']['level'])

def calcOptCost(curAncients, optAncients, chorDiscount):
    optCost = 0
    if optAncients.optArgaiv > curAncients.curArgaiv: optCost += ceil((1-chorDiscount)*(0.5*(optAncients.optArgaiv)*(optAncients.optArgaiv+2)-0.5*curAncients.curArgaiv*(curAncients.curArgaiv+2)))
    if optAncients.optAtman > curAncients.curAtman: optCost += ceil(((1-chorDiscount)*((2**(optAncients.optAtman+1)-1)-(2**(curAncients.curAtman+1)-1))))
    if optAncients.optBubos > curAncients.curBubos: optCost += ceil(((1-chorDiscount)*((2**(optAncients.optBubos+1)-1)-(2**(curAncients.curBubos+1)-1))))
    if optAncients.optChronos > curAncients.curChronos: optCost += ceil(((1-chorDiscount)*((2**(optAncients.optChronos+1)-1)-(2**(curAncients.curChronos+1)-1))))
    if optAncients.optDogcog > curAncients.curDogcog: optCost += ceil(((1-chorDiscount)*((2**(optAncients.optDogcog+1)-1)-(2**(curAncients.curDogcog+1)-1))))
    if optAncients.optDora > curAncients.curDora: optCost += ceil(((1-chorDiscount)*((2**(optAncients.optDora+1)-1)-(2**(curAncients.curDora+1)-1))))
    if optAncients.optFortuna > curAncients.curFortuna: optCost += ceil(((1-chorDiscount)*((2**(optAncients.optFortuna+1)-1)-(2**(curAncients.curFortuna+1)-1))))
    if optAncients.optKuma > curAncients.curKuma: optCost += ceil(((1-chorDiscount)*((2**(optAncients.optKuma+1)-1)-(2**(curAncients.curKuma+1)-1))))
    if optAncients.optLibertas > curAncients.curLibertas: optCost += ceil((1-chorDiscount)*(0.5*(optAncients.optLibertas)*(optAncients.optLibertas+2)-0.5*curAncients.curLibertas*(curAncients.curLibertas+2)))
    if optAncients.optMammon > curAncients.curMammon: optCost += ceil((1-chorDiscount)*(0.5*(optAncients.optMammon)*(optAncients.optMammon+2)-0.5*curAncients.curMammon*(curAncients.curMammon+2)))
    if optAncients.optMimzee > curAncients.curMimzee: optCost += ceil((1-chorDiscount)*(0.5*(optAncients.optMimzee)*(optAncients.optMimzee+2)-0.5*curAncients.curMimzee*(curAncients.curMimzee+2)))
    if optAncients.optMorg > curAncients.curMorg: optCost += ceil((1-chorDiscount)*(optAncients.optMorg-curAncients.curMorg))
    if optAncients.optSiya > curAncients.curSiya: optCost += ceil((1-chorDiscount)*(0.5*(optAncients.optSiya)*(optAncients.optSiya+2)-0.5*curAncients.curSiya*(curAncients.curSiya+2)))
    if optAncients.optSolomon > curAncients.curSolomon: optCost += ceil((1-chorDiscount)*(ceil((0.4*optAncients.optSolomon**2.5)-(0.4*curAncients.curSolomon**2.5))))
    return optCost

def findOptSiya(curAncients, calcs):
    optcost = 0
    newsiya = curAncients.curSiya
    while optcost <= calcs.totalSoulsAvail:
        newsiya += 1
        optAncients = Optimal(curAncients, newsiya, calcs.alpha)
        optAncients.calcOptimalAncientLvls()
        optcost = calcOptCost(curAncients, optAncients, calcs.chorDiscount)
    return (newsiya - 1)

def getAncientLvlDifferences(curAncients, optAncients):
    diff = {}
    diff['Argaiv'] = int(optAncients.optArgaiv - curAncients.curArgaiv)
    diff['Atman'] = int(optAncients.optAtman - curAncients.curAtman)
    diff['Bubos'] = int(optAncients.optBubos - curAncients.curBubos)
    diff['Chronos'] = int(optAncients.optChronos - curAncients.curChronos)
    diff['Dogcog'] = int(optAncients.optDogcog - curAncients.curDogcog)
    diff['Dora'] = int(optAncients.optDora - curAncients.curDora)
    diff['Fortuna'] = int(optAncients.optFortuna - curAncients.curFortuna)
    diff['Kuma'] = int(optAncients.optKuma - curAncients.curKuma)
    diff['Libertas'] = int(optAncients.optLibertas - curAncients.curLibertas)
    diff['Mammon'] = int(optAncients.optMammon - curAncients.curMammon)
    diff['Mimzee'] = int(optAncients.optMimzee - curAncients.curMimzee)
    diff['Morg'] = int(optAncients.optMorg - curAncients.curMorg)
    diff['Siya'] = int(optAncients.optSiya - curAncients.curSiya)
    diff['Solomon'] = int(optAncients.optSolomon - curAncients.curSolomon)
    return diff

def theMonsterMath(input):
    #results = []
    savedata = savedecoder.decryptSave(input)
    if savedata == 'Invalid Save File':
        return (savedata, savedata)
    curAncients = Current(savedata)
    curAncients.getCurrentAncientLvls()
    calcs = Calculations(savedata)
    calcs.doTheMath()
    optsiya = findOptSiya(curAncients, calcs)
    optAncients = Optimal(curAncients, optsiya, calcs.alpha)
    optAncients.calcOptimalAncientLvls()
    optcost = calcOptCost(curAncients, optAncients, calcs.chorDiscount)
    diff = getAncientLvlDifferences(curAncients, optAncients)
    return (optAncients, diff)