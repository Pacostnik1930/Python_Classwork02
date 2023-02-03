#  Множества. В множестве содержатся только уникальные значения.

#colors = {'red','green','blue'}
#print(colors)
#colors.add('red')
#print(colors)
#colors.add('gray')
#print(colors)
#colors.remove('red')
#print(colors)
#colors.remove('red')
#print(colors)
#colors.discard('red')
#print(colors)
#colors.clear()
#print(colors)
#q = set()


# Операции со множествами в Python

a = {1,2,3,5,8}
b = {2,5,8,13,21}
c = a.copy          #  c = {1,2,3,5,8}
u = a.union(b)      #  u = {1,2,3,5,8,13,21}
i = a.intersection(b)  # i = {2,5,8}
d1 = a.difference(b)    # d1 = {1,3}
d2 = b.difference(a)    # d2 = {13,21}
q = a.union(b).difference(a.intersection(b))  # {1,3,13,21}

# Замороженное множество 

a = {1,8,6}
b = frozenset(a)
print(b)
