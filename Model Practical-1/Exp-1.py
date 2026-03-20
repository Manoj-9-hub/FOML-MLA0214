import math

data = [
    ["Short","High","Many","Yes"],
    ["Medium","Medium","Few","No"],
    ["Long","Low","None","No"],
    ["Short","Medium","Many","Yes"]
]

def entropy(rows):
    total = len(rows)
    counts = {}
    for r in rows:
        label = r[-1]
        counts[label] = counts.get(label, 0) + 1
    ent = 0
    for c in counts.values():
        p = c/total
        ent -= p * math.log2(p)
    return ent

def split(rows, col):
    result = {}
    for r in rows:
        key = r[col]
        result.setdefault(key, []).append(r)
    return result

def info_gain(rows, col):
    total_entropy = entropy(rows)
    subsets = split(rows, col)
    total = len(rows)
    subset_entropy = 0
    for subset in subsets.values():
        subset_entropy += (len(subset)/total) * entropy(subset)
    return total_entropy - subset_entropy

def build_tree(rows, features):
    labels = [r[-1] for r in rows]
    if labels.count(labels[0]) == len(labels):
        return labels[0]
    if not features:
        return max(set(labels), key=labels.count)
    gains = [(info_gain(rows, f), f) for f in features]
    best = max(gains)[1]
    tree = {best:{}}
    subsets = split(rows, best)
    for val, subset in subsets.items():
        new_features = features[:]
        new_features.remove(best)
        tree[best][val] = build_tree(subset, new_features)
    return tree

tree = build_tree(data, [0,1,2])
print(tree)
