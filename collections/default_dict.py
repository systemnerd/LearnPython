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

my_company = "sample_company"
coworkers = ['Jen', 'Li', 'Charlie', 'Rhys']
other_coworkers = [('rolf', 'apple'), ('anna', 'google')]

coworker_companies = defaultdict(lambda: my_company)

for person, company in other_coworkers:
    coworker_companies[person] = company

print(coworker_companies[coworkers[0]])
print(coworker_companies['rolf'])
