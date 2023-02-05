from controller import *


# Tela do menu principal
def screen_menu():

    #cria a tela do menu
    menu_screen = pygame.display.set_mode((WIDTH, HEIGHT))

    #configura a imagem de fundo do menu
    menu_background = pygame.image.load('./img/menu.png')
    menu_background = pygame.transform.scale(menu_background, (WIDTH, HEIGHT))
    menu_screen.blit(menu_background, (0, 0))

    # cria os textos do menu com a fonte neon na pasta font
    txt1 = pygame.font.Font('./font/Monoton-Regular.ttf', 100).render('Neon Maze 2', True, ('Blue')).get_rect(center=(WIDTH // 2, HEIGHT // 2 - 200))
    # coloca o texto na tela
    menu_screen.blit(pygame.font.Font('./font/Monoton-Regular.ttf',100).render('Neon Maze 2', True, ('Gold')), txt1)

    #cria e configura botão para iniciar o jogo (usando a imagem "play.png")
    startButton = pygame.Rect(0, 0, 200, 50)
    startButton.center = WIDTH // 2, HEIGHT // 2
    font = pygame.font.SysFont('./font/Monoton-Regular.ttf', 30)
    text = font.render('Start', True, ('Gold'))
    text_rect = text.get_rect()
    text_rect.center = startButton.center

    #cria e configura botão para sair do jogo
    exitButton = pygame.Rect(0, 0, 200, 50)
    exitButton.center = WIDTH // 2, HEIGHT // 2 + 200
    font3 = pygame.font.SysFont('./font/Monoton-Regular.ttf', 30)
    text3 = font3.render('Exit', True, ('Gold'))
    text_rect3 = text3.get_rect()
    text_rect3.center = exitButton.center

    #configurando barulho de clique
    click_sound = pygame.mixer.Sound('./music/transicao.wav')
    click_sound.set_volume(1)

    #configurando a musica de fundo
    pygame.mixer.music.load('./music/86.mp3')
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(-1)

    #configurando os eventos do menu
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if startButton.collidepoint(event.pos):
                    # adicionando o som de clique
                    click_sound.play()
                    screen_SelectMusic()
                elif exitButton.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

        #desenha o botão de iniciar o jogo
        pygame.draw.rect(menu_screen, (0, 0, 0), startButton)
        menu_screen.blit(text, text_rect)

        #desenha o botão de sair do jogo
        pygame.draw.rect(menu_screen, (0, 0, 0), exitButton)
        menu_screen.blit(text3, text_rect3)

        pygame.display.update() # atualiza a tela

# cria a tela de seleção da musica
def screen_SelectMusic():
    #cria a tela de seleção da musica
    select_music_screen = pygame.display.set_mode((WIDTH, HEIGHT))

    # cria os textos do menu com a fonte neon na pasta font
    txt1 = pygame.font.Font('./font/Monoton-Regular.ttf', 100).render('Neon Maze', True, ('Blue')).get_rect(center=(WIDTH // 1.7, HEIGHT // 2 - 200))
    # coloca o texto na tela
    select_music_screen.blit(pygame.font.Font('./font/Monoton-Regular.ttf',100).render('Músicas', True, ('Gold')), txt1)

    #cria e configura botão para selecionar a musica 1
    music1Button = pygame.Rect(0, 0, 200, 50) 
    music1Button.center = WIDTH // 2, HEIGHT // 2.5
    font = pygame.font.SysFont('./font/Monoton-Regular.ttf', 30)
    text = font.render('Castelvania 2 (Hard)', True, ('Gold'))
    text_rect = text.get_rect()
    text_rect.center = music1Button.center

    #cria e configura botão para selecionar a musica 2
    music2Button = pygame.Rect(0, 0, 200, 50)
    music2Button.center = WIDTH // 2, HEIGHT // 2.5 + 100
    font2 = pygame.font.SysFont('./font/Monoton-Regular.ttf', 30)
    text2 = font2.render('Donkey Kong Country (Hard)', True, ('Gold'))
    text_rect2 = text2.get_rect()
    text_rect2.center = music2Button.center

    #cria e configura botão para selecionar a musica 3
    music3Button = pygame.Rect(0, 0, 200, 50)
    music3Button.center = WIDTH // 2, HEIGHT // 2.5 + 200
    font3 = pygame.font.SysFont('./font/Monoton-Regular.ttf', 30)
    text3 = font3.render('Tokyo Drift (Medio)', True, ('Gold'))
    text_rect3 = text3.get_rect()
    text_rect3.center = music3Button.center

    #cria e configura botão para selecionar a musica 4
    music4Button = pygame.Rect(0, 0, 200, 50)
    music4Button.center = WIDTH // 2, HEIGHT // 2.5 + 300
    font4 = pygame.font.SysFont('./font/Monoton-Regular.ttf', 30)
    text4 = font4.render('Top Gear (Easy)', True, ('Gold'))
    text_rect4 = text4.get_rect()
    text_rect4.center = music4Button.center

    #cria e configura botão para voltar ao menu
    backButton = pygame.Rect(0, 0, 200, 50)
    backButton.center = WIDTH // 6, HEIGHT // 2.5 + 350
    font5 = pygame.font.SysFont('./font/Monoton-Regular.ttf', 30)
    text5 = font5.render('VOLTAR', True, ('Red'))
    text_rect5 = text5.get_rect()
    text_rect5.center = backButton.center

    #cria e configura botão para sair do jogo
    exitButton = pygame.Rect(0, 0, 200, 50)
    exitButton.center = WIDTH // 1.2, HEIGHT // 2.5 + 350
    font6 = pygame.font.SysFont('./font/Monoton-Regular.ttf', 30)
    text6 = font6.render('SAIR', True, ('Red'))
    text_rect6 = text6.get_rect()
    text_rect6.center = exitButton.center

    #configurando barulho de clique
    click_sound = pygame.mixer.Sound('./music/transicao.wav')
    click_sound.set_volume(0.2)
    click_sound2 = pygame.mixer.Sound('./music/letsFight.wav')
    click_sound2.set_volume(1)
    
    #configurando os eventos da tela de seleção da musica
    while True:

        for event in pygame.event.get():
            if event == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if music1Button.collidepoint(event.pos):
                    # adicionando o som de clique
                    click_sound.play()
                    pygame.time.delay(1300)
                    click_sound2.play()
                    pygame.time.delay(1300)
                    play_music(1)
                    screen_inGame(1)
                elif music2Button.collidepoint(event.pos):
                    click_sound.play()
                    pygame.time.delay(1300)
                    click_sound2.play()
                    pygame.time.delay(1300)
                    play_music(2)
                    screen_inGame(2)
                elif music3Button.collidepoint(event.pos):
                    click_sound.play()
                    pygame.time.delay(1300)
                    click_sound2.play()
                    pygame.time.delay(1300)
                    play_music(3)
                    screen_inGame(3)
                elif music4Button.collidepoint(event.pos):
                    click_sound.play()
                    pygame.time.delay(1300)
                    click_sound2.play()
                    pygame.time.delay(1300)
                    play_music(4)
                    screen_inGame(4)
                elif backButton.collidepoint(event.pos):
                    click_sound.play()
                    screen_menu()
                    break
                elif exitButton.collidepoint(event.pos):
                    click_sound.play()
                    pygame.quit()
                    sys.exit()

        #desenha o botão de selecionar a musica 1
        pygame.draw.rect(select_music_screen, (0, 0, 0), music1Button)
        select_music_screen.blit(text, text_rect)

        #desenha o botão de selecionar a musica 2
        pygame.draw.rect(select_music_screen, (0, 0, 0), music2Button)
        select_music_screen.blit(text2, text_rect2)

        #desenha o botão de selecionar a musica 3
        pygame.draw.rect(select_music_screen, (0, 0, 0), music3Button)
        select_music_screen.blit(text3, text_rect3)

        #desenha o botão de selecionar a musica 4
        pygame.draw.rect(select_music_screen, (0, 0, 0), music4Button)
        select_music_screen.blit(text4, text_rect4)

        #desenha o botão de voltar ao menu
        pygame.draw.rect(select_music_screen, (0, 0, 0), backButton)
        select_music_screen.blit(text5, text_rect5)

        #desenha o botão de sair do jogo
        pygame.draw.rect(select_music_screen, (0, 0, 0), exitButton)
        select_music_screen.blit(text6, text_rect6)

        pygame.display.update() # atualiza a tela

# função que representa o jogo rodando
def screen_inGame(music):

    # configurações do jogo
    FPS = 60 # velocidade do jogo
    pygame.init() # inicializa o pygame
    game_surface = pygame.Surface(RES) # cria uma superfície para o jogo
    surface = pygame.display.set_mode((WIDTH + 300, HEIGHT)) # cria a tela do jogo com 300px para o painel
    clock = pygame.time.Clock() # cria um relógio para controlar a velocidade do jogo

    # imagens do jogo
    personIMG = ''
    if music == 1:
        bg_game = pygame.image.load('img/bgCastelvania.png').convert() # carrega a imagem de fundo do jogo
        bg_game = pygame.transform.scale(bg_game, (WIDTH, HEIGHT)) # redimensiona a imagem de fundo do jogo
        bgPainel = pygame.image.load('img/bg_main.jpg').convert() # carrega a imagem de fundo do painel
        bgPainel = pygame.transform.scale(bgPainel, (300, HEIGHT)) # redimensiona a imagem de fundo do painel
        personIMG = 'img/CastelvaniaPerson.png'
    if music == 2:
        bg_game = pygame.image.load('img/bgDonkeyKong.jpg').convert() # carrega a imagem de fundo do jogo
        bg_game = pygame.transform.scale(bg_game, (WIDTH, HEIGHT)) # redimensiona a imagem de fundo do jogo
        bgPainel = pygame.image.load('img/bg_main.jpg').convert() # carrega a imagem de fundo do painel
        bgPainel = pygame.transform.scale(bgPainel, (300, HEIGHT)) # redimensiona a imagem de fundo do painel
        personIMG = 'img/DonkeyKongPerson.png'
    if music == 3:
        bg_game = pygame.image.load('img/bgTokioDrift.jpg').convert() # carrega a imagem de fundo do jogo
        bg_game = pygame.transform.scale(bg_game, (WIDTH, HEIGHT)) # redimensiona a imagem de fundo do jogo
        bgPainel = pygame.image.load('img/bg_main.jpg').convert() # carrega a imagem de fundo do painel
        bgPainel = pygame.transform.scale(bgPainel, (300, HEIGHT)) # redimensiona a imagem de fundo do painel
        personIMG = 'img/TokioDriftPerson.png'
    if music == 4:
        bg_game = pygame.image.load('img/bgTopGear.jpg').convert() # carrega a imagem de fundo do jogo
        bg_game = pygame.transform.scale(bg_game, (WIDTH, HEIGHT)) # redimensiona a imagem de fundo do jogo
        bgPainel = pygame.image.load('img/bg_main.jpg').convert() # carrega a imagem de fundo do painel
        bgPainel = pygame.transform.scale(bgPainel, (300, HEIGHT)) # redimensiona a imagem de fundo do painel
        personIMG = 'img/TopGearPerson.png'

    # gera o labirinto
    maze = generate_maze()

    # cria o jogador
    player_img = pygame.image.load(personIMG).convert_alpha()
    player_img = pygame.transform.scale(player_img, (TILE - 2 * maze[0].thickness, TILE - 2 * maze[0].thickness))
    player_rect = player_img.get_rect()
    player_speed = 5
    player_rect.center = TILE // 2, TILE // 2
    directions = {'a': (-player_speed, 0), 'd': (player_speed, 0), 'w': (0, -player_speed), 's': (0, player_speed)}
    keys = {'a': pygame.K_a, 'd': pygame.K_d, 'w': pygame.K_w, 's': pygame.K_s}
    direction = (0, 0)

    # cria a lista de personagens (selkers e inimigos)
    selkers_list = [normalSelkers(game_surface) for i in range(3)]
    blackSelkers_list = [blackSelkers(game_surface) for i in range(3)]

    # cria lista dos itens (baseadões, relógios e gasolina)
    baseadao_list = [baseadao(game_surface) for i in range(3)]
    watches_list = [watch(game_surface) for i in range(3)]
    gas_list = [gasolina(game_surface) for i in range(3)]

    # cria a lista de paredes para colisão
    walls_collide_list = sum([cell.get_rects() for cell in maze], [])

    # tempo de jogo, pontos, musica e record
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    if music == 1:
        time = 64
    elif music == 2:
        time = 61
    elif music == 3:
        time = 166 # duração da música 
    elif music == 4:
        time = 180
    score = 0
    baseadaoScore = 0
    watchScore = 0
    gasolinaScore = 0
    record = get_record()

    # Limite da mochila (baseadões, relógios e gasolina) --> depois será implementado com knapsack
    limiteBaseadao = 3
    limiteWatch = 3
    limiteGasolina = 3 

    # fontes de texto
    font = pygame.font.SysFont('Impact', 150)
    text_font = pygame.font.SysFont('Impact', 80)

    # configurações do botão de pausa
    pauseButton = pygame.Rect(0, 0, 200, 50)
    pauseButton.center = WIDTH + 150, 50
    font2 = pygame.font.SysFont('Arial', 30)
    text2 = font2.render('Pause', True, (255, 255, 255))
    text_rect2 = text2.get_rect()
    text_rect2.center = pauseButton.center

    # configurações do botão de sair
    exitButton = pygame.Rect(0, 0, 200, 50)
    exitButton.center = WIDTH + 150, 150
    font3 = pygame.font.SysFont('Arial', 30)
    text3 = font3.render('Exit', True, (255, 255, 255))
    text_rect3 = text3.get_rect()
    text_rect3.center = exitButton.center

    #configurando barulho da gasolina
    click_soundGasolina = pygame.mixer.Sound('./music/ReadyGoEffect.wav')
    click_soundGasolina.set_volume(1)

    #configurando barulho do baseadão
    click_soundBaseado = pygame.mixer.Sound('./music/RdrigoFaroCavalo.wav')
    click_soundBaseado.set_volume(1)

    #configurando barulho do relógio
    click_soundRelgio = pygame.mixer.Sound('./music/SamsungEstourado.wav')
    click_soundRelgio.set_volume(1)

    #configurando barulho de derrota
    click_soundDerrota = pygame.mixer.Sound('./music/OhShit.wav')
    click_soundDerrota.set_volume(1)

    # começa o jogo (loop principal - O labirinto é gerado aleatoriamente pelo maze_generator.py)
    while True:
        surface.blit(bgPainel, (WIDTH, 0))
        surface.blit(game_surface, (0, 0))
        game_surface.blit(bg_game, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.USEREVENT:
                time -= 1

        # configurações de movimento e controle de colisão
        pressed_key = pygame.key.get_pressed()
        for key, key_value in keys.items():
            if pressed_key[key_value] and not is_collide(*directions[key], walls_collide_list, player_rect):
                direction = directions[key]
                break
        if not is_collide(*direction, walls_collide_list, player_rect):
            player_rect.move_ip(direction)

        # desenha o labirinto
        [cell.draw(game_surface) for cell in maze]

        # verifica se comeu a comida e atualiza o score, tempo e FPS (velocidade do jogo)
        if take_Selker(selkers_list, player_rect):
            FPS += 0
            score += 1
            time += 0

        # verifica se comeu um selker preto (deixa mais lento e perde tempo e pontos) 
        if take_BlackSelker(blackSelkers_list, player_rect):
            FPS -= 10
            if score > 0:
                score -= 1
            time -= 50

        # verifica se comeu um baseadão (deixa um pouco mais lento mais ganha tempo)
        if take_baseadao(baseadao_list, player_rect):
            # som de baseadão
            click_soundBaseado.play()
            FPS -= 5
            score += 0
            time -= 10
            baseadaoScore += 1

        # verifica se comeu um relógio (apenas da mais tempo)
        if take_watch(watches_list, player_rect):
            # som de relógio
            click_soundRelgio.play()
            FPS += 0
            score += 0
            time += 50
            watchScore += 1

        # verifica se comeu gasolina
        if take_gasolina(gas_list, player_rect):
            # som de gasolina
            click_soundGasolina.play()
            FPS += 20
            score += 0
            time -= 20
            gasolinaScore += 1


        # reinicia o jogo quando o player perde (tempo esgotado) - 
        if time < 0:
            #player_rect.center = TILE // 2, TILE // 2
            #[food.set_pos() for food in selkers_list]
            #set_record(record, score)
            #record = get_record()
            #time, score, FPS = 60, 0, 60

            # som de derrota
            click_soundDerrota.play()
            pygame.time.delay(2500)
            screenGameOver(score, record)

        # draw player
        game_surface.blit(player_img, player_rect)

        # draw selkers
        [food.draw() for food in selkers_list]

        # draw blackSelkers
        [enemy.draw() for enemy in blackSelkers_list]

        # draw baseadao
        if baseadaoScore < limiteBaseadao:
            [baseadao.draw() for baseadao in baseadao_list]

        # draw watch
        if watchScore < limiteWatch:
            [watch.draw() for watch in watches_list]

        # draw gasolina
        if gasolinaScore < limiteGasolina:
            [gas.draw() for gas in gas_list]

        # desenha no painel a label e o valor do tempo 
        txt1 = text_font.render('TIME', True, pygame.Color('cyan'), True)
        txt1 = pygame.transform.scale(txt1, (int(txt1.get_width() * 0.2), int(txt1.get_height() * 0.2)))
        surface.blit(txt1, (WIDTH + 70, 15))
        txtTime = font.render(f'{time}', True, pygame.Color('cyan'))
        txtTime = pygame.transform.scale(txtTime, (int(txtTime.get_width() * 0.2), int(txtTime.get_height() * 0.2)))
        surface.blit(txtTime, (WIDTH + 70, 30))

        # desenha no painel a label e o valor do score
        txt2 = text_font.render('SCORE', True, pygame.Color('cyan'), True)
        txt2 = pygame.transform.scale(txt2, (int(txt2.get_width() * 0.2), int(txt2.get_height() * 0.2)))
        surface.blit(txt2, (WIDTH + 70, 70))
        txtScore = font.render(f'{score}', True, pygame.Color('cyan'))
        txtScore = pygame.transform.scale(txtScore, (int(txtScore.get_width() * 0.2), int(txtScore.get_height() * 0.2)))
        surface.blit(txtScore, (WIDTH + 70, 85))

        # desenha no painel a label e o valor do record
        txt3 = text_font.render('RECORD', True, pygame.Color('cyan'), True)
        txt3 = pygame.transform.scale(txt3, (int(txt3.get_width() * 0.2), int(txt3.get_height() * 0.2)))
        surface.blit(txt3, (WIDTH + 70, 125))
        txtRecord = font.render(f'{record}', True, pygame.Color('cyan'))
        txtRecord = pygame.transform.scale(txtRecord, (int(txtRecord.get_width() * 0.2), int(txtRecord.get_height() * 0.2)))
        surface.blit(txtRecord, (WIDTH + 70, 140))        

        # desenha no painel a label e o valor do baseadão
        txt4 = text_font.render('BASEADÕES (Max 3)', True, pygame.Color('cyan'), True)
        txt4 = pygame.transform.scale(txt4, (int(txt4.get_width() * 0.2), int(txt4.get_height() * 0.2)))
        surface.blit(txt4, (WIDTH + 70, 180))
        txtBaseadao = font.render(f'{baseadaoScore}', True, pygame.Color('cyan'))
        txtBaseadao = pygame.transform.scale(txtBaseadao, (int(txtBaseadao.get_width() * 0.2), int(txtBaseadao.get_height() * 0.2)))
        surface.blit(txtBaseadao, (WIDTH + 70, 195))

        # desenha no painel a label e o valor do relógio
        txt5 = text_font.render('RELOGIOS (Max 3)', True, pygame.Color('cyan'), True)
        txt5 = pygame.transform.scale(txt5, (int(txt5.get_width() * 0.2), int(txt5.get_height() * 0.2)))
        surface.blit(txt5, (WIDTH + 70, 235))
        txtWatch = font.render(f'{watchScore}', True, pygame.Color('cyan'))
        txtWatch = pygame.transform.scale(txtWatch, (int(txtWatch.get_width() * 0.2), int(txtWatch.get_height() * 0.2)))
        surface.blit(txtWatch, (WIDTH + 70, 250))

        # desenha no painel a label e o valor do gasolina
        txt6 = text_font.render('GASOLINAS (Max 3)', True, pygame.Color('cyan'), True)
        txt6 = pygame.transform.scale(txt6, (int(txt6.get_width() * 0.2), int(txt6.get_height() * 0.2)))
        surface.blit(txt6, (WIDTH + 70, 290))
        txtGas = font.render(f'{gasolinaScore}', True, pygame.Color('cyan'))
        txtGas = pygame.transform.scale(txtGas, (int(txtGas.get_width() * 0.2), int(txtGas.get_height() * 0.2)))
        surface.blit(txtGas, (WIDTH + 70, 305))

        pygame.display.flip()
        clock.tick(FPS)

# função que representa a tela de derrota
def screenGameOver(score, record):

    # para a música de fundo
    pygame.mixer.music.stop()

    # adiciona a musica de derrota
    pygame.mixer.music.load('./music/Lose.mp3')
    pygame.mixer.music.set_volume(1)
    pygame.mixer.music.play(-1)

    # cria a tela de derrota
    gameOver_screen = pygame.display.set_mode((WIDTH, HEIGHT))

    # carrega a imagem de fundo
    background = pygame.image.load('./img/lose.png')
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))

    #cria e configura botão para nova tentativa
    restart = pygame.Rect(0, 0, 200, 50) 
    restart.center = WIDTH // 2, HEIGHT // 2.5
    font = pygame.font.SysFont('./font/Monoton-Regular.ttf', 30)
    text = font.render('Tentar Novamente', True, ('Green'))
    text_rect = text.get_rect()
    text_rect.center = restart.center

    #cria e configura botão para voltar ao menu
    backButton = pygame.Rect(0, 0, 200, 50)
    backButton.center = WIDTH // 6, HEIGHT // 2.5 + 350
    font5 = pygame.font.SysFont('./font/Monoton-Regular.ttf', 30)
    text5 = font5.render('Menu Principal', True, ('Red'))
    text_rect5 = text5.get_rect()
    text_rect5.center = backButton.center

    #cria e configura botão para sair do jogo
    exitButton = pygame.Rect(0, 0, 200, 50)
    exitButton.center = WIDTH // 1.2, HEIGHT // 2.5 + 350
    font6 = pygame.font.SysFont('./font/Monoton-Regular.ttf', 30)
    text6 = font6.render('Sair', True, ('Red'))
    text_rect6 = text6.get_rect()
    text_rect6.center = exitButton.center

    #configurando barulho de clique
    click_sound = pygame.mixer.Sound('./music/transicao.wav')
    click_sound.set_volume(1)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                click_sound.play()
                if restart.collidepoint(event.pos):
                    screen_SelectMusic()
                if backButton.collidepoint(event.pos):
                    pygame.mixer.music.stop()
                    screen_menu()
                if exitButton.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

        pygame.draw.rect(gameOver_screen, 'Gold', restart, 5)
        pygame.draw.rect(gameOver_screen, 'Red', backButton, 5)
        pygame.draw.rect(gameOver_screen, 'Red', exitButton, 5)
        gameOver_screen.blit(background, (0, 0))
        gameOver_screen.blit(text, text_rect)
        gameOver_screen.blit(text5, text_rect5)
        gameOver_screen.blit(text6, text_rect6)
        pygame.display.flip()
        
# inicia o jogo
pygame.init()
screen_menu()