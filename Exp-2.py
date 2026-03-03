import csv

# Load CSV data
def load_data(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        data = list(reader)
    header = data[0]
    return header, data[1:]

# Check if hypothesis is consistent with example
def is_consistent(hypothesis, example):
    for i in range(len(hypothesis)):
        if hypothesis[i] != '?' and hypothesis[i] != example[i]:
            return False
    return True

# Get minimum generalizations for S
def generalize_S(s, example):
    for i in range(len(s)):
        if s[i] == 'Ø':
            s[i] = example[i]
        elif s[i] != example[i]:
            s[i] = '?'
    return s

# Specialize G for negative example
def specialize_G(g, s, example, domains):
    specializations = []
    for i in range(len(g)):
        if g[i] == '?':
            for value in domains[i]:
                if value != example[i]:
                    new_h = g.copy()
                    new_h[i] = value
                    if s[i] == '?' or s[i] == new_h[i]:
                        specializations.append(new_h)
    return specializations

# Candidate-Elimination Algorithm
def candidate_elimination(filename):
    header, data = load_data(filename)
    num_attr = len(data[0]) - 1

    # Get domains of attributes
    domains = [set() for _ in range(num_attr)]
    for row in data:
        for i in range(num_attr):
            domains[i].add(row[i])

    # Initialize S and G
    S = ['Ø'] * num_attr
    G = [['?'] * num_attr]

    print("\nInitial S:", S)
    print("Initial G:", G)

    for example in data:
        attributes = example[:-1]
        label = example[-1]

        if label == 'Yes':  # Positive example
            # Remove inconsistent hypotheses from G
            G = [g for g in G if is_consistent(g, attributes)]

            # Generalize S
            S = generalize_S(S, attributes)

        else:  # Negative example
            new_G = []
            for g in G:
                if is_consistent(g, attributes):
                    specializations = specialize_G(g, S, attributes, domains)
                    new_G.extend(specializations)
                else:
                    new_G.append(g)
            G = new_G

        print("\nAfter example:", example)
        print("S:", S)
        print("G:", G)

    print("\nFinal Version Space:")
    print("S boundary:", S)
    print("G boundary:", G)


# Run the algorithm
candidate_elimination("training_data.csv")
