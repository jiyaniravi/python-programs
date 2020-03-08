import re

value = 'Agent Ravi will hand over the document to Agent Vinod tomorrow'
pattern = re.compile(r'Agent \w+')
print(pattern.findall(value))
print(pattern.sub('Classified',value))