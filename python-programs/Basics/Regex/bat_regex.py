import re

pattern = re.compile(r'bat(?:wo)?man')
bat_list_all = pattern.findall('batman is there but not batwoman')
batman_match = pattern.search('batman is there')
batwoman_match = pattern.search('batwoman is there')

print(batman_match.group())
print(batwoman_match.group())
print(bat_list_all)