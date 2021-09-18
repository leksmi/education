# Варианты создания:

a = [['moskva', 495],
     ['piter', 812],
     ['ryazan', 4912]]

d = {
    'moskva': 495,
    'piter': 812,
    'ryazan': 4912
}

r = dict(moskva=495, piter=812, ryazan=4912)

t = dict(a)
q = dict.fromkeys(['a', 'b', 'c'], 'default_data')

print(q)
