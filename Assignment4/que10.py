#. Concatenate two lists index-wise.
#list1 = ["M", "na", "i", "Ku"]
#list2 = ["y", "me", "s", "nal"]
#Expected output: [’My’, ’name’, ’is’, ’Kunal’]
list1=["M","na","i","Ku"]
list2=["y","me","s","nal"]

result_list = [i + j for i, j in zip(list1, list2)]
print(result_list)