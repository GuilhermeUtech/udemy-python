#aula sobre Namedtuple
"""t = (12,13,14)
print(t[1])
"""

from collections import namedtuple

Dog = namedtuple('Dog', 'age breed name')
sam = Dog(age = 18, breed = 'cocker', name = 'shake')
print(sam)
print(sam.age)
print(sam.breed)
print(sam.name)
print(sam[2])

