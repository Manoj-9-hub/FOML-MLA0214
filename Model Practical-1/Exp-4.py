data = [
    ["Short","High","Many","Yes"],
    ["Medium","Medium","Few","No"],
    ["Long","Low","None","No"],
    ["Short","Medium","Many","Yes"]
]

def accuracy(y_true, y_pred):
    correct = sum(1 for i in range(len(y_true)) if y_true[i]==y_pred[i])
    return correct/len(y_true)

def confusion(y_true, y_pred):
    labels = list(set(y_true))
    matrix = {l:{k:0 for k in labels} for l in labels}
    for i in range(len(y_true)):
        matrix[y_true[i]][y_pred[i]] += 1
    return matrix

y_true = [r[-1] for r in data]
y_pred = y_true[:]

print("Accuracy:", accuracy(y_true, y_pred))
print("Confusion Matrix:", confusion(y_true, y_pred))
