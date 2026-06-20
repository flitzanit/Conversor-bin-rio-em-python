import pygame
import sys

pygame.init()

# Tela
LARGURA = 1280
ALTURA = 720
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Conversor Binario - Versao Teste")

clock = pygame.time.Clock()

# Cores
BRANCO = (245, 245, 245)
PRETO = (20, 20, 20)
VERDE_LOUSA = (38, 92, 70)
VERDE_ESCURO = (24, 55, 44)
MADEIRA = (120, 75, 38)
AMARELO = (255, 215, 90)
AMARELO_ESCURO = (210, 160, 40)
CINZA = (80, 80, 80)

# Estados do jogo
TELA_MENU = "menu"
TELA_NOME = "nome"
TELA_BEM_VINDO = "bem_vindo"

estado_atual = TELA_MENU
nome_jogador = ""

# Fontes
def carregar_fonte(tamanho):
    try:
        return pygame.font.Font("PixelifySans-Regular.ttf", tamanho)
    except:
        return pygame.font.SysFont("arial", tamanho, bold=True)

fonte_titulo = carregar_fonte(58)
fonte_texto = carregar_fonte(38)
fonte_botao = carregar_fonte(34)
fonte_input = carregar_fonte(42)

# Tenta carregar background externo
try:
    background = pygame.image.load("background.png")
    background = pygame.transform.scale(background, (LARGURA, ALTURA))
except:
    background = None


def desenhar_fundo():
    if background:
        tela.blit(background, (0, 0))
    else:
        tela.fill((210, 185, 150))

        # Moldura da lousa
        pygame.draw.rect(tela, MADEIRA, (95, 55, 930, 610), border_radius=12)

        # Lousa
        pygame.draw.rect(tela, VERDE_LOUSA, (120, 80, 880, 560), border_radius=8)

        # Detalhes da lousa
        pygame.draw.rect(tela, VERDE_ESCURO, (120, 80, 880, 560), 6, border_radius=8)

        # Chao
        pygame.draw.rect(tela, (145, 95, 55), (0, 650, LARGURA, 70))

        # Professora simplificada placeholder
        pygame.draw.circle(tela, (245, 200, 170), (1120, 260), 45)
        pygame.draw.circle(tela, (180, 60, 35), (1120, 245), 55, 12)
        pygame.draw.rect(tela, (80, 70, 130), (1070, 310, 100, 190), border_radius=18)
        pygame.draw.line(tela, (190, 140, 80), (1070, 340), (990, 260), 8)
        pygame.draw.line(tela, (200, 170, 95), (985, 255), (910, 210), 6)

        # Olhos
        pygame.draw.circle(tela, PRETO, (1105, 260), 4)
        pygame.draw.circle(tela, PRETO, (1135, 260), 4)


def desenhar_texto(texto, fonte, cor, centro):
    superficie = fonte.render(texto, True, cor)
    retangulo = superficie.get_rect(center=centro)
    tela.blit(superficie, retangulo)


def desenhar_botao(texto, retangulo, mouse_pos):
    cor = AMARELO_ESCURO if retangulo.collidepoint(mouse_pos) else AMARELO

    pygame.draw.rect(tela, PRETO, retangulo.move(6, 6), border_radius=12)
    pygame.draw.rect(tela, cor, retangulo, border_radius=12)
    pygame.draw.rect(tela, PRETO, retangulo, 4, border_radius=12)

    desenhar_texto(texto, fonte_botao, PRETO, retangulo.center)


def tela_menu(mouse_pos):
    desenhar_fundo()

    desenhar_texto("CONVERSOR BINARIO", fonte_titulo, BRANCO, (560, 210))
    desenhar_texto("versao teste", fonte_texto, BRANCO, (560, 285))

    botao_play = pygame.Rect(480, 380, 260, 90)
    desenhar_botao("PLAY", botao_play, mouse_pos)

    return botao_play


def tela_nome(mouse_pos):
    desenhar_fundo()

    desenhar_texto("QUAL E O SEU NOME?", fonte_titulo, BRANCO, (560, 190))

    input_rect = pygame.Rect(320, 300, 480, 80)
    pygame.draw.rect(tela, BRANCO, input_rect, border_radius=10)
    pygame.draw.rect(tela, PRETO, input_rect, 4, border_radius=10)

    texto_input = nome_jogador if nome_jogador else "Digite aqui"
    cor_input = PRETO if nome_jogador else CINZA
    desenhar_texto(texto_input, fonte_input, cor_input, input_rect.center)

    botao_enter = pygame.Rect(430, 430, 260, 80)
    desenhar_botao("ENTER", botao_enter, mouse_pos)

    return botao_enter


def tela_bem_vindo():
    desenhar_fundo()

    nome = nome_jogador.strip()

    if nome == "":
        nome = "jogador"

    desenhar_texto("OLA,", fonte_titulo, BRANCO, (560, 220))
    desenhar_texto(nome.upper(), fonte_titulo, AMARELO, (560, 310))
    desenhar_texto("SEJA BEM-VINDO!", fonte_texto, BRANCO, (560, 410))


# Loop principal
while True:
    mouse_pos = pygame.mouse.get_pos()

    if estado_atual == TELA_MENU:
        botao_atual = tela_menu(mouse_pos)
    elif estado_atual == TELA_NOME:
        botao_atual = tela_nome(mouse_pos)
    elif estado_atual == TELA_BEM_VINDO:
        tela_bem_vindo()
        botao_atual = None

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if estado_atual == TELA_MENU:
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if botao_atual.collidepoint(evento.pos):
                    estado_atual = TELA_NOME

        elif estado_atual == TELA_NOME:
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if botao_atual.collidepoint(evento.pos):
                    estado_atual = TELA_BEM_VINDO

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    estado_atual = TELA_BEM_VINDO
                elif evento.key == pygame.K_BACKSPACE:
                    nome_jogador = nome_jogador[:-1]
                else:
                    if len(nome_jogador) < 14:
                        nome_jogador += evento.unicode

    pygame.display.update()
    clock.tick(60)