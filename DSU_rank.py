#union by size/rank

n = 6
elements = [i for i in range(n)]
parents = [i for i in range(n)]

def find_parent(element):
    temp_element = element
    temp_parent = parents[temp_element]

    while temp_parent != temp_element:
        temp_element = temp_parent
        temp_parent = parents[element]
    parents[element] = temp_parent
    return temp_element

def union(u,v):
    u_parent = parents[u]
    v_parent = parents[v]
    if u_parent != v_parent:
        parents[v] = u
    

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
