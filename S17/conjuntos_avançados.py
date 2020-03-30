#Conjuntos/Sets avançados => veja da forma igual conjuntos matématicos que a gente vê na escola

s = set()
s.add(1)
s.add(2)
print(s)
s.clear()
print(s)
sc = ()
sc = s.copy()
sc.add(4)
print(sc)

s1 = {1,2,3}
s2 = {1,4,5}
print(s1.difference_update(s2))
print(s1) 

