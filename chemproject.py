import chemparse
from aweights import getatomicmass
avogadro = 6.022 * (10)**23

nummol = []
fmass = []
numfirst = []

def getanswer(formula, mass):
    thismass = 0
    firstnum = 0
    formdict = chemparse.parse_formula(formula)
    first = True
    print(formdict)
    for i in formdict.keys():
        thismass += getatomicmass(i) * formdict[i]
    nummolecules = avogadro * (mass / thismass)
    fmass.append(thismass)
    nummol.append((mass / thismass))
    nfirst = nummolecules * formdict[getfirstelement(formula)]
    numfirst.append(nfirst)
    return nfirst
def getfirstelement(cformula):
    formula = cformula.replace("(", "")
    z = formula[:2]
    if z[-1].isnumeric() or z[-1].isupper():
        return z[0]
    else:
        return z
def getmass(formula):
    thismass = 0
    firstnum = 0
    formdict = chemparse.parse_formula(formula)
    first = True
    print(formdict)
    for i in formdict.keys():
        thismass += getatomicmass(i) * formdict[i]   
    return thismass 
