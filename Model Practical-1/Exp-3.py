data = [
    ["Short","High","Many","Yes"],
    ["Medium","Medium","Few","No"],
    ["Long","Low","None","No"],
    ["Short","Medium","Many","Yes"]
]

def prob(attr_index, value, label):
    count = 0
    total = 0
    for r in data:
        if r[-1] == label:
            total += 1
            if r[attr_index] == value:
                count += 1
    return (count+1)/(total+3)

def prior(label):
    total = len(data)
    count = sum(1 for r in data if r[-1]==label)
    return count/total

test = ["Short","High","Many"]

p_yes = prior("Yes")
p_no = prior("No")

for i in range(3):
    p_yes *= prob(i, test[i], "Yes")
    p_no *= prob(i, test[i], "No")

print("Yes" if p_yes > p_no else "No")
