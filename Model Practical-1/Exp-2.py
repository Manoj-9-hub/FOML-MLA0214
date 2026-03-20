import math

data = [
    ["Short","High","Many","Yes"],
    ["Medium","Medium","Few","No"],
    ["Long","Low","None","No"],
    ["Short","Medium","Many","Yes"]
]

map1 = {"Short":1,"Medium":2,"Long":3,"Low":1,"High":3,"Few":2,"Many":3,"None":1}

def encode(row):
    return [map1[row[0]], map1[row[1]], map1[row[2]]]

def distance(a,b):
    return math.sqrt(sum((x-y)**2 for x,y in zip(a,b)))

test = ["Short","High","Many"]
test_enc = encode(test)

distances = []
for r in data:
    d = distance(encode(r), test_enc)
    distances.append((d, r[-1]))

distances.sort()
k = 3
votes = [distances[i][1] for i in range(k)]
result = max(set(votes), key=votes.count)

print(result)
