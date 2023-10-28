company = "Apple Inc"

flag  = company.startswith("Apl") # True
print(flag)
flag = company.endswith("inc") # True
print(flag)


companies = ["royal pvt.ltd","reliance pub.ltd","tata pvt.ltd","apple inc","google inc","microsoft inc"]
filterCompanies =[]

for i in companies:
    if i.endswith("pvt.ltd"):
        filterCompanies.append(i)

print(filterCompanies)        