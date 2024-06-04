def union(set1, set2):
    set_union = []
    [set_union.append(value) for value in set1 if value not in set_union]
    [set_union.append(value) for value in set2 if value not in set_union]
    return set_union

def intersection(set1, set2):
    return [set for set in set1 if set in set2]


def symmetric_difference(set1, set2):
    set3 = []
    [set3.append(value) for value in set1 if value not in set2 and value not in set3]
    [set3.append(value) for value in set2 if value not in set1 and value not in set3] 
    return set3




print(union(['a','b','c'],['d','e','f']))
print(intersection([1,2,3],[3,4,5]))
print(symmetric_difference([1,2,3,3],[3,4,5]))