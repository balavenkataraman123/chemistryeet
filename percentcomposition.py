import chemparse
from aweights import getatomicmass
avogadro = 6.022 * (10)**23

def getanswer(formula):
    thismass = 0
    firstnum = 0
    formdict = chemparse.parse_formula(formula)
    fdk = list(formdict.keys())
    fdv = list(formdict.values())
    totalmass = sum([fdv[i] * getatomicmass(fdk[i]) for i in range(len(fdk))])
    pcdict = {}
    for i in formdict.keys():
        pcdict[i] = (getatomicmass(i)*formdict[i] * 100) / totalmass
    
    return pcdict
    
for i in range(len(formulas)):
    print(names[i])
    print(getanswer(formulas[i]))
    print("\n\n")