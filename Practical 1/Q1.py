def compare(a, b):
    chef1 = 0
    chef2 = 0
    
    for i in range(3):
        if a[i] > b[i]:
            chef1 += 1
        elif a[i] < b[i]:
            chef2 += 1
    
    return chef1, chef2

a = []
b = []

print("Enter the scores for Chef 1:")
for i in range(3):
    score = int(input(f"Score {i+1}: "))
    a.append(score)

print("Enter the scores for Chef 2:")
for i in range(3):
    score = int(input(f"Score {i+1}: "))
    b.append(score)

result = compare(a, b)
print(result)
