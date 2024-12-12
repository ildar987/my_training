my_disk = {'Artur': 1995, 'Denis': 1997, 'Anton': 1999}
print(my_disk)
print(my_disk['Anton'])
print(my_disk.get('Max'))
my_disk.update({'Egor': 2001, 'Alex': 2003})
del my_disk['Denis']
print(my_disk)
my_set = {1, 2, 3, 2, 3, 'a', 'b', 'a'}
print(my_set)
my_set.add(5)
my_set.add('c')
my_set.remove('a')
print(my_set)
