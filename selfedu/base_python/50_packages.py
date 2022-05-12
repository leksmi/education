# Файл __init__.py это инициализатор пакета, он выполняется при импорте пакета
# Пакет импортируется как и модуль:
import courses

print(dir(courses))

courses.python.get_python()
courses.get_python() # это сработает за счет импорта from .. в файле __init__.py
print(courses.get_mysql())
