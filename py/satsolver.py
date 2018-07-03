import itertools as itertools
variables = ['A', 'B', 'C']
# n = UND; v = ODER; ~ = NOT
# reihenfolge => NOT,
fullformula = 'A$n(B$nC$n~C)'
quantifier = [['A', '$A'], ['B', '$E'], ['C', '$A']]
class SATInstance(object):
    def parse_init(self, formula, vars):
        self.variables = vars
        self.formula = formula
        self.truth_table = list(itertools.product([1, 0], repeat=len(vars)))
        print(self.truth_table)
    def solve(self, qbfquants):
        print(self.variables)
        print(self.formula)
        sats = []
        for belegung in self.truth_table:
            singleformula = self.formula
            for i in range(0, len(self.variables)):
                singleformula = singleformula.replace(self.variables[i], str(belegung[i]))
            savedfomula = singleformula
            while len(singleformula) > 1:
                singleformula = singleformula.replace('~1', '0')
                singleformula = singleformula.replace('~0', '1')
                while '$n' in singleformula:
                    singleformula = singleformula.replace('1$n1', '1')
                    singleformula = singleformula.replace('0$n1', '0')
                    singleformula = singleformula.replace('1$n0', '0')
                    singleformula = singleformula.replace('0$n0', '0')
                    if '$n(' in singleformula or ')$n' in singleformula:
                        break
                while '$v' in singleformula:
                    singleformula = singleformula.replace('1$v1', '1')
                    singleformula = singleformula.replace('0$v1', '1')
                    singleformula = singleformula.replace('1$v0', '1')
                    singleformula = singleformula.replace('0$v0', '0')
                    if '$v(' in singleformula or ')$v' in singleformula:
                        break
                singleformula = singleformula.replace('(1)', '1')
                singleformula = singleformula.replace('(0)', '0')
                if singleformula == '1':
                    print(str(belegung) + ' solved it')
                    sats.append(belegung)
                    # quantifier check
                    # print(savedfomula)
        if qbfquants:
            qbfsolved = qbfquants
            for sat in sats:
                for quant in qbfquants:
                    if '$A' in quant:
                        # print('forAll')
                        if sat[variables.index(quant[0])] not in quant:
                            quant.append(sat[variables.index(quant[0])])
                        if 1 in quant and 0 in quant:
                            qbfsolved.remove(quant)
                    if '$E' in quant:
                        # print('Exists')
                        qbfsolved.remove(quant)
                if len(qbfsolved) == 0:
                    print('quantifiers are fulfilled')
                    return
            print('quantifiers are not fulfilled')
        # print(allFormulas)
    # def solve_as_qbf(self, quantifiers):
    def __init__(self):
        self.variables = []
        self.truth_table = []
        self.formula = ''

s = SATInstance()
s.parse_init(fullformula, variables)
s.solve(quantifier)