def element(x):
    return x[0]

def sort_list(t):
    return sorted(t, key = element)

print(sort_list([(2,5), (1,2), (4,4), (2,3), (2,1)]))
