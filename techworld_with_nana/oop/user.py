from getpass import getpass


class User:
    def __init__(self, email='', name='', password=getpass(), current_job_title=''):
        self.email = email
        self.name = name
        self.password = password
        self.current_job_title = current_job_title

    def change_password(self):
        self.password = getpass()

    def change_job_title(self, new_title):
        self.current_job_title = new_title

    def get_user_info(self):
        print(f'Current user {self.name} works as {self.current_job_title}.'
              f'\nYou can contact them at {self.email}')
