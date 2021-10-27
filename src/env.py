from os import environ

def get(name):
    return environ.get(name) 

BOT_TOKEN = get('BOT_TOKEN')
USER = get('USER')
PWD = get('PWD')
