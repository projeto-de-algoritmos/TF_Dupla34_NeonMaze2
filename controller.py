from maze_generator import *
from itens import *
from persons import *
import sys

# verifica se o player colidiu com a parede
def is_collide(x, y, walls_collide_list, player_rect):
    tmp_rect = player_rect.move(x, y)
    if tmp_rect.collidelist(walls_collide_list) == -1:
        return False
    return True

# verifica se o player colidiu com o selker
def take_Selker(selkers_list, player_rect):
    for food in selkers_list:
        if player_rect.collidepoint(food.rect.center):
            food.set_pos()
            return True
    return False

# verifica se o player colidiu com o selker inimigo (Black Selker)
def take_BlackSelker(blackSelkers_list, player_rect):
    for enemy in blackSelkers_list:
        if player_rect.collidepoint(enemy.rect.center):
            enemy.set_pos()
            return True
    return False

# verifica se o player colidiu com um baseadão (diminui a velocidade a velocidade de queda do tempo)
def take_baseadao(baseadaos_list, player_rect):
    for baseadao in baseadaos_list:
        if player_rect.collidepoint(baseadao.rect.center):
            baseadao.set_pos()
            return True
    return False

# verifica se o player colidiu com um relógio (aumenta o tempo de jogo)
def take_watch(watches_list, player_rect):
    for watch in watches_list:
        if player_rect.collidepoint(watch.rect.center):
            watch.set_pos()
            return True
    return False

# verifica se o player colidou com uma gasolina (aumenta a velocidade do player)
def take_gasolina(gasolinas_list, player_rect):
    for gasolina in gasolinas_list:
        if player_rect.collidepoint(gasolina.rect.center):
            gasolina.set_pos()
            return True
    return False

# retorna o recorde salvo no arquivo
def get_record():
    try:
        with open('record') as f:
            return f.readline()
    except FileNotFoundError:
        with open('record', 'w') as f:
            f.write('0')
            return 0

# atualiza o recorde
def set_record(record, score):
    rec = max(int(record), score)
    with open('record', 'w') as f:
        f.write(str(rec))

# musicas de fundo (de acordo com o parametro, toca uma musica ou outra da pasta music)
def play_music(option):
    if option == 1:
        pygame.mixer.music.load('./music/Castelvania2.mp3')
        pygame.mixer.music.set_volume(1)  # define o volume da música de fundo
        pygame.mixer.music.play(-1)  # reproduz a música de fundo em loop
    elif option == 2:
        pygame.mixer.music.load('./music/DonkeyKongCountry.mp3')
        pygame.mixer.music.set_volume(1)  # define o volume da música de fundo
        pygame.mixer.music.play(-1)  # reproduz a música de fundo em loop
    elif option == 3:
        pygame.mixer.music.load('./music/TokyoDriftInstrumental.mp3')
        pygame.mixer.music.set_volume(1)
        pygame.mixer.music.play(-1)
    elif option == 4:
        pygame.mixer.music.load('./music/TopGear.mp3')
        pygame.mixer.music.set_volume(1)
        pygame.mixer.music.play(-1)