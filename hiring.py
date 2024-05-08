import random 

candidates = [0,1,2,3,4,5,6,7,8,9,10]
print(f"CANDIDATES: {candidates}")
interviewed = []
hired = []

for i in range(len(candidates)):
    temp  = random.choice(candidates)
    interviewed.append(temp)
    candidates.remove(temp)

max = -1
for i in interviewed:
    if max<i:
        hired.append(i)
        max = i

print(f"RANDOMISED INTERVIEW ORDER OF CANDIDATES: {interviewed}")
print(f"CANDIDATES HIRED: {hired}")
print(f"HIRING COST: {len(hired)}")
print(f"FIRING COST: {len(hired)-1}")