from django.contrib.auth.models import User

#create users in db
def run():
    USERS = ['Leonel Zambrano', 'Julian Amaya', 'Juan Medina', 'Jose Andrade']

    for user in USERS:
        user_name = user.split()
        first_name_l = user_name[0].lower()
        email = ''.join([first_name_l, '@monoku.com'])
        user = User.objects.create_user(first_name_l, email, '123pass456')
        user.first_name=user_name[0]
        user.last_name=user_name[1]
        user.save()
