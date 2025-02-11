def load(link):
    print("Загружаем", link)
    return "hello"


def save(link, filename):
    data = load(link)
    print("Сохраняем в", filename)


def default(values):
    print("Неизвестно как эти данные обработать")


def main(data_string: str):
    values = data_string.split("~")
    if isinstance(values, (list, tuple)) and len(values) == 2 and values[0] == "load":
        load(values[1])
    elif isinstance(values, (list, tuple)) and len(values) == 3 and values[0] == "save":
        save(values[1], values[2])
    else:
        default(values)


main("load~http://example.com/files/test.txt")
main("save~http://example.com/files/test.txt~file.txt")
main("use~http://example.com/files/test.txt~file.txt")
main("save~http://example.com/files/test.txt~file.txt~file2.txt")


def main_new(data_string: str):
    values = data_string.split("~")
    match values:
        case "load", link:
            load(link)
        case "save", link, filename:
            save(link, filename)
        case _:
            default(values)

print('-' * 10)
main_new("load~http://example.com/files/test.txt")
main_new("save~http://example.com/files/test.txt~file.txt")
main_new("use~http://example.com/files/test.txt~file.txt")


def create_rnd_data():
    names = ["phone", "TV", "PC", "car", "home", "case", "bird", "chicken",
            "dish", "float", "C++", "data", ""]
    prices = [500, 100, 1400, 2000, 750, 3500, 5000, 120, 50, 4200]
    goods = []
    for i in range(500_000):
        name = names[i % len(names)]
        