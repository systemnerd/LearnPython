from collections import defaultdict

coworkers = [('rolf', 'MIT'), ('james', 'Stanford'), ('rolf', 'columbia')
             ,('jen', 'oxford'), ('james', 'Yale')]

# alma_matters = {}

# for worker, place in coworkers:
#     if worker not in alma_matters:
#         alma_matters[worker] = []
#     alma_matters[worker].append(place)

# print(alma_matters)

alma_matters = defaultdict(list)

for worker, place in coworkers:
    alma_matters[worker].append(place)

print(alma_matters)
print(alma_matters["rolf"])
print(alma_matters["sample"])
