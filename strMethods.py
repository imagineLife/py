str = 'Here is my string.'

print('------')
print('---Ends With "string."---')
print('------')
print(str.endswith("string."))

print('------')
print('---Ends With substring---')
print('------')
subString = "string."
print(str.endswith(subString))

print('------')
print('---Index of matching "is"--')
print('------')
print(str.find("is"))

print('------')
print('---Index not matching, doesnt alter original element--')
print('------')
strSpaces = '   Wills ball is spaced out   '
print(strSpaces)
print(strSpaces.lstrip())
print(strSpaces.rstrip())