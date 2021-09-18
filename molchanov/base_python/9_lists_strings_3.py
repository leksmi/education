#
children = ['arbuzov_2000', 'ivanov_2011', 'petrov_2009', 'Bubnov_2015']
print(children)

# Регистр важен при сортировке!:
print(sorted(children))

# Фильтрующая фугкция:
def sort_by_year(name):
    year = name.split('_')[-1]
    return year


print(sort_by_year(children[0]))

sorted_children = sorted(children, key=sort_by_year)
print(sorted_children)
    
