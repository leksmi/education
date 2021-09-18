
children = ['arbuzov_2000', 'ivanov_2011', 'petrov_2009', 'Bubnov_2015']
names = []

for child in children:
    print(child.split('_')[0])

for iname in children:
    name = iname.split('_')[0]
    names.append(name.title())

print(names)



