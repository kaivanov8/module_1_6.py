# словари и множества
my_dict = {'Andrey':1990,'Anton':1991,'Olya':1992}
print(my_dict)
print('Existing vaiue:',my_dict.get('Olya'))
print('Not existing value:',my_dict.get('Igor'))
my_dict.update({'Masha':1993, 'Kolya':1994})
print('Modified dictionary:',my_dict)
#
my_set = {1.4,2,2,1,1,'дом'}
print('my_set:', my_set)
my_set.discard('дом')
print('modified set:',my_set)