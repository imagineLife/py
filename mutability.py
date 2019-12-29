#arrays hold their original id after mutation
arr = []
print(arr)
print(id(arr))

arr.append(14)
print(arr)
print(id(arr))

#arrays hold their original id after mutation
obj = {'a': 'water'}
print(obj)
print(id(obj))

obj['b'] = 'melon'
print(obj)
print(id(obj))


#integer variables do NOT hold their 
# original id after mutation
intVar = 5
print(id(intVar))

intVar = intVar + 1
print(id(intVar))