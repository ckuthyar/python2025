dict1={"name":"Ram",
       "age":21,
       "grade":"A"}

print(dict1.keys())
print(dict1.values())
print(dict1.items())

list1=list(dict1.items())
print(list1[0])
print(list1[1])
print(list1[2])

f_key, f_value=next(iter(dict1.items()))
print(f_key,f_value)
print(f"first key is {f_key} first value is {f_value}")

