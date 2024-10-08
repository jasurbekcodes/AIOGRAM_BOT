async def get_list(name):
    users = {
        'John': 'Darsda bor',
        'Asilbek': 'Darsda bor',
        'Azizbek': 'Darsda bor',
        'Alisher': 'Darsda bor',
    }
    try:
        return str(users[name])
    except KeyError:
        return "Bunday odam darsda yo'q!"
