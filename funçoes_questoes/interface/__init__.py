from time import sleep

def decoração(tamanho, item):
    return  tamanho * item

def tempo(segundos, msg, repetir = 1):
    for _ in range(repetir):
        sleep(segundos)
        print(msg,end='')
    return
