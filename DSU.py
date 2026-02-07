n = 6
elements = [i for i in range(n)]
parents = [i for i in range(n)]

#find parent with path compression
def find_parent(x):
    if parents[x] == x:
        return x
    parents[x] = find_parent(parents[x])
    return parents[x]


def union(u,v):
    a = find_parent(u)
    b = find_parent(v)
    if a != b:
        parents[b] = a # connecting b to a
    

union(0,1)
# print(parents[0])
# print(parents[1])

union(2,3)
# print(parents[3])
# print(parents[4])

union(4,5)
union(0,2)
print(parents[2])

find_parent(3)
