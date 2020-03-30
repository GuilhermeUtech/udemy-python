#aula sobre default dict
from collections import defaultdict
d = {}
d['one'] = 1
d2 = defaultdict(object)
d2['one'] = 1
print(d2)
d2['two'] = 1
print(d2)
#Se eu procurar algo que n tem no dicionário ele da uma resposta
#padrão que eu digo qual que é:
"""
from collections import defaultdict
ice_cream = defaultdict(lambda: 'Vanilla')
ice_cream = defaultdict(lambda: 'Vanilla')
ice_cream['Sarah'] = 'Chunky Monkey'
ice_cream['Abdul'] = 'Butter Pecan'
print ice_cream['Sarah']
Chunky Monkey
print ice_cream['Joe']
Vanilla
"""

