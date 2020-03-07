import re

pattern = re.compile(r'bat(wo)?man')
bat_list = pattern.search('batman is there but not batwoman')
bat_list_all = pattern.findall('batman is there but not batwoman')

print(bat_list.group())
print(bat_list_all)