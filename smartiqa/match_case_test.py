def load():
    print('Loading ..')

def save_data():
    print('Save data ..')

def default_action():
    print('Unknown process method !')

def main(value):
    """
    Решение обычным способом через if/elif/else
    """
    if isinstance(value, str) and value == 'load':
        load()
    elif isinstance(value, str) and value == 'save_data':
        save_data()
    else:
        default_action()


def main_new(value):
    """
    Через проверку на тип match и селектор case
    """
    match value:
        case 'load':
            load()
        case 'save_data':
            save_data()
        case _:
            default_action()

print('With if/elif:')
main('reject_all')
main('run_fast')
main('save_data')
main('load')
print('With match/case:')
main_new('reject_all')
main_new('run_fast')
main_new('save_data')
main_new('load')
