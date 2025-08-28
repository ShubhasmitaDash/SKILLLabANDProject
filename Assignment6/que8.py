prices={"laptop":55000, "phone":25000, "tablet":18000}
p=[]
for key in prices:
    if prices[key] not in p:
        p.append(prices[key])
p.sort()
print("Maximum is:", p[-1])