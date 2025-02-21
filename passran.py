import random

def generate_password(length=10):
    
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$%*&?!_-'
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


password = generate_password(10)
print("Сгенерированный пароль:", password)

