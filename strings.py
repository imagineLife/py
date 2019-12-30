name = 'will'
withSingleQuote = "Will's Ball"
print(withSingleQuote)

print('------')
print('---WITH SPACES---')
print('------')
multiLine = """Will's ball
is red
and bouncy!"""
print(multiLine)

print('------')
print('---WITH TABS---')
print('------')
withTabs = "Will's\tball\tis\tbouncy!"
print(withTabs)

print('------')
print('---WITH SUBSTITUTIONS---')
print('------')
itm = 'SUB ball'
clr = 'SUB red'
print('Will\'s %s is %s' % (itm, clr))