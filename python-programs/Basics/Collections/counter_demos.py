from collections import Counter

my_number_list = [1,12,1,2,1,4232,453,5,123,23,4,12,3123,12321,3,2,412,312,2,312,31,312,312,3123,21]
my_char_string = 'askdasnbdbsahfhasvfhsadfgsdfadjiasdwoeihjwqoirhsdkmfdijf'
my_word_string = 'djkd fb sa ba jdf shf dh hf sd jfh dsf hfd s sdfvb sd jfh sdf h sf'
print(Counter(my_number_list))
print(Counter(my_char_string))
print(Counter(my_word_string.split()))

c = Counter(my_word_string.split())
print(c.most_common(3))
print(c.most_common()[:-4:-1])

print(sum(c.values()))