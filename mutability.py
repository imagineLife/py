#arrays hold their original id after mutation
arr = []
print(id(arr))

arr.append(14)
print(id(arr))

#integer variables do NOT hold their 
# original id after mutation
intVar = 5
print(id(intVar))

intVar = intVar + 1
print(id(intVar))