from django.contrib.auth.models import User
from accounts.models import Profile

data_users = [{'username': 'Giuseppi', 'type_user': 'Boss'},
            {'username': 'manager1', 'type_user': 'Manager', 'boss__id': None},
            {'username': 'manager2', 'type_user': 'Manager'},
            {'username': 'manager3', 'type_user': 'Manager'},
            {'username': 'hitman1', 'type_user': 'Hitman', 'boss__id': 2},
            {'username': 'hitman2', 'type_user': 'Hitman', 'boss__id': 2},
            {'username': 'hitman3', 'type_user': 'Hitman', 'boss__id': 2},


            {'username': 'hitman4', 'type_user': 'Hitman', 'boss__id': 3},
            {'username': 'hitman5', 'type_user': 'Hitman', 'boss__id': 3},
            {'username': 'hitman6', 'type_user': 'Hitman', 'boss__id': 3},

            {'username': 'hitman7', 'type_user': 'Hitman', 'boss__id': 4},
            {'username': 'hitman8', 'type_user': 'Hitman', 'boss__id': 4},
            {'username': 'hitman9', 'type_user': 'Hitman', 'boss__id': 4},
]

def load():
    for data_user in data_users:
#        print(data_user)


        username = data_user.pop('username')

        print('username', username)

        data_to_create = {
            'username': username,
            'email': username + "@" + username + ".com",
            'first_name': username[((len(username)-1)//2):],
            'last_name': username[:(len(username)-1)//2],

        }

        try:
            user, user_created = User.objects.get_or_create(**data_to_create)
        except Exception :
            user = User.objects.get(username=username)

        user.set_password(username)
        user.save()
        

        Profile.objects.get_or_create(user=user, **data_user)

def run():
    load()