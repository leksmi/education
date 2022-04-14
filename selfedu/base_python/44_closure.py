def say_name(name):
    def say_goodbye():
        print(f'Do not say me goodbye {name} !')

    # say_goodbye()
    return say_goodbye

f = say_name('Olesya')
f()
f2 = say_name('Alena')
f2()

def counter(start=0):
    def step():
        nonlocal start
        start += 1
        return start
    return step

c1 = counter(10)
c2 = counter()

print(f'c1 = {c1()} | c2 = {c2()}')
print(f'c1 = {c1()} | c2 = {c2()}')
