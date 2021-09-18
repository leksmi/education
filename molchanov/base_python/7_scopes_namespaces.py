
name = 'Sveta'


def name1():
    # name = 'In names()'
    # age = 30
    # print("Function's a() namespaces", locals())

    def name2():
        # name = 'Samantha'
        print(name)
        print(locals())

    name2()


name1()

