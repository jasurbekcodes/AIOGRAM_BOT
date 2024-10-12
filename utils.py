from contents import words



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


async def calculate(text: str):
    try:
        if '+' in text:
            a, b = text.split('+')
            ans = int(a) + int(b)
        elif '-' in text:
            a, b = text.split('-')
            ans = int(a) - int(b)
        elif '*' in text:
            a, b = text.split('*')
            ans = int(a) * int(b)
        elif '/' in text:
            a, b = text.split('/')
            ans = int(a) / int(b)

        return str(ans)
    except ValueError:
        print("Error: Non-numeric input")
    except ZeroDivisionError:
        print("Error: Division by zero")

async def get_word(key, lang = 'uz'):
    word = words.get(key+ '-' + lang)
    return word
