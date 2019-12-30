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

print('------')
print('---WITH SUBSTITUTIONS DIFFERENTLY---')
print('------')
itm2 = 'SUB2 ball'
clr2 = 'SUB2 red'
print('Will\'s {0} is {1}'.format(itm2, clr2))