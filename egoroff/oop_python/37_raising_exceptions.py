# инструкция raise

# присвоение ссылки для исключения:
try:
    1 / 1
    # {}['some_key']

except (KeyError, IndexError) as loo_err:
    print(f'\nLookup error !')
    print(f'Logging error: {repr(loo_err)}')
except ZeroDivisionError as err:  # можно задать имя (ссылку), которая указывает на кортеж
    print('\nError: division by 0 !')
    print(f'Logging error: {err}; {repr(err)}')

# после raise указать или встроенный exception, или свой
# er = Exception('Перехватил все ошибки..')
# raise er

# raise можно вставить внутрь except:
try:
    [1, 2, 3, 4, 5][15]
except (IndexError, KeyError) as error:
    print(f'Logging error: {error}; {repr(error)}')
    raise  # за данного вызова исключение попадет в консоль, при это Python сам подставит возникшее исключение
