def log_action(message):
    with open('log.txt', 'a') as file:
        file.write(f'{message}\n')
