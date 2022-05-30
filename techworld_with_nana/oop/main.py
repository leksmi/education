from user import User
from post import Post

app_user_one = User('test@example.com', 'Sveta', current_job_title='HR manager')
print(app_user_one)
print(f'Password for user {app_user_one.name}: {app_user_one.password}')
app_user_one.get_user_info()

app_user_two = User(name='Vita', current_job_title='Engineer', email='vit@exa.com')
print(f'Password for user {app_user_two.name}: {app_user_two.password}')
app_user_two.get_user_info()
app_user_two.change_password()
print(f'User 2 passw: {app_user_two.password}')
print(f'User 1 passw: {app_user_one.password}')

new_post = Post('Some text today', app_user_one.name)
new_post.get_post_info()
