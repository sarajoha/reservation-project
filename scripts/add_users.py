from reservation.models import User

#create products in db
def run():
    USERS = ['Luis Lacruz', 'Nata G', 'Leonel Zambrano', 'Yeison Vasquez', 'Brian Cortes',
            'Andres Carreno', 'Andres Alarcon', 'Luis Villalobos', 'Julian Amaya', 'Juan Medina',
            'Estefany Salas', 'Alejandra Garcia', 'Elizabeth Pena', 'Jose Andrade']

    for user in USERS:
        user_name = user.split()
        User.objects.create(first_name=user_name[0], last_name=user_name[1])
