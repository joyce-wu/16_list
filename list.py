def union(a, b):
    ans = []
    [ans.append(x) for x in a if x not in ans]
    [ans.append(x) for x in b if x not in ans]
    return ans

#print(union([1, 2, 3], [2, 3, 4]))
#print(union([2, 2, 2, 3, 1], [1, 0, 2]))

def intersection(a, b):
    ans = []
    [ans.append(x) for x in a if x in b and x not in ans]
    return ans

#print(intersection([1, 1, 2, 4], [4, 1]))
#print(intersection([1, 2, 3], [2, 3, 4]))

def set_difference(u, a):
    ans = []
    c=u+a
    [ans.append(x) for x in c if x not in intersection(u,a)]
    return ans

#print(set_difference((1, 2, 3), (2, 3, 4)))

def sym_diff(a, b):
    return set_difference(union(a,b), intersection(a, b))

print(sym_diff([1, 2, 3], [2, 3, 4]))

def cartesian_prod(a, b):
    return [(x,y) for x in a for y in b]

