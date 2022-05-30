import requests
from pprint import pprint

response = requests.get('https://gitlab.com/api/v4/users/nanuchi/projects')
print(response.json())
print(type(response.json()))
print(response.json()[0])
my_projects_lst = response.json()

for project in my_projects_lst:
    print(f"Project name is: {project['name']}\nurl: {project['web_url']}\n")
