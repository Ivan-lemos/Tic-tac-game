from turtle import Turtle, Screen
import random


banner = """\
████████╗██╗░█████╗░░░░░░░████████╗░█████╗░░█████╗░░██████╗░░█████╗░███╗░░░███╗███████╗
╚══██╔══╝██║██╔══██╗░░░░░░╚══██╔══╝██╔══██╗██╔══██╗██╔════╝░██╔══██╗████╗░████║██╔════╝
░░░██║░░░██║██║░░╚═╝█████╗░░░██║░░░███████║██║░░╚═╝██║░░██╗░███████║██╔████╔██║█████╗░░
░░░██║░░░██║██║░░██╗╚════╝░░░██║░░░██╔══██║██║░░██╗██║░░╚██╗██╔══██║██║╚██╔╝██║██╔══╝░░
░░░██║░░░██║╚█████╔╝░░░░░░░░░██║░░░██║░░██║╚█████╔╝╚██████╔╝██║░░██║██║░╚═╝░██║███████╗
░░░╚═╝░░░╚═╝░╚════╝░░░░░░░░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝
"""

# Configurar a tela
screen = Screen()
screen.title("< TIC_TAC GAME >       ( ͡X_͡❛X)")
screen.bgcolor("white")
# Chamar a função mestre para qualquer clique

funtion_name = None
user_symbol=None
pc_symbol=None
quadrant = None
board = ['','','','','','','','',''] # Tabuleiro 3x3 em uma lista de 9 posições (0-8)

marker_positions = {
    "vertical":{
        "left":[(-180.0, 255.0),(-180.0, -255.0)],
        "middle":[(0.0, 255.0),(0.0, -255.0)],
        "right":[(180.0, 255.0),(180.0, -255.0)]
    },

    "horizontal":{
        "top": [(-255.0, 180.0),(255.0, 180.0)],
        "middle": [(-255.0, 0.0),(255.0, -0.0)],
        "botton": [(-255.0, -180.0),(255.0, -180.0)]
    },

    "diagonal":{
        "left": [ (230.0, 250.0), (-230.0, -250.0) ],
        "right" : [ (-230.0, 250.0), (230.0, -250.0) ]
    }
} # Posições do marcador para sinalizar o resultado do jogo

symbol_positions = [
    (-241.0, 105.0),(-57.0, 105.0), (121.0, 105.0),
    (-241.0, -81.0), (-57.0, -81.0),(121.0, -81.0),
    (-241.0, -258.0),(-57.0, -258.0),(121.0, -258.0)
] # Posições em que o marcador deve colocar o simbolo


def user_choice(x, y):
    """Callback function identify marked quadrant by user."""
    global quadrant
    # Verifica se o clique ocorreu dentro do quadrante 1
    if (-260 <= x <= -106) and (107 <= y <= 250):
        print("Opção 0 selecionada")
        quadrant=0
    elif (-93 <= x <= 93) and (107 <= y <= 250):
        print("Opção 1 selecionada")
        quadrant=1
    elif ( 106<= x <= 253) and (107 <= y <= 250):
        print("Opção 2 selecionada")
        quadrant=2
    elif (-260 <= x <= -106) and (-90 <= y <= 90):
        print("Opção 3 selecionada")
        quadrant=3
    elif (-93 <= x <= 93) and (-90 <= y <= 90):
        print("Opção 4 selecionada")
        quadrant=4
    elif (106 <= x <= 253) and (-90 <= y <= 90):
        print("Opção 5 selecionada")
        quadrant=5
    elif (-260 <= x <= -106) and (-250 <= y <= -107):
        print("Opção 6 selecionada")
        quadrant=6
    elif (-93 <= x <= 93) and (-250 <= y <= -107):
        print("Opção 7 selecionada")
        quadrant=7
    elif (106 <= x <= 253) and (-250 <= y <= -107):
        print("Opção 8 selecionada")
        quadrant=8
    else:
        print('selecionou fora')

    if quadrant is not None:
        game_play()

def get_mouse_position(x, y):
    """Callback function to print the mouse position."""
    print(f"Mouse clicked at ({x}, {y})")

def menu_option(x, y):
    """Retorna qual opção de simbolo o usuário escolheu."""
    global user_symbol , pc_symbol

    # Verifica se o clique ocorreu dentro da área de 🅧
    if (-244 <= x <= -113) and (-113 <= y <= 18):
        user_symbol = '🅧'
        pc_symbol = '🅞'
    # Verifica se o clique ocorreu dentro da área de 🅞
    elif (72 <= x <= 201) and (-113 <= y <= 18):
        user_symbol = '🅞'
        pc_symbol = '🅧'
    else:
        print(f"Cliquei fora das opções: {x ,y}")
        user_symbol=None

    print(f"Opção selecionada: {user_symbol}")

    if user_symbol is not None: # para evitar execução automática
        screen.clearscreen()
        game_play() # chamada de função subsequente

def winner_calculate() ->str:
    """Calcula se há um vencedor no tabuleiro. Retorna o vencedor"""
    global board

    # 6.1 - Verificar Horizontais
    if board[0] == board[1] == board[2] and board[0] != '':  # Linha 1-2-3
        mark_result('horizontal' , 'top')
        return board[0]
    elif board[3] == board[4] == board[5] and board[3] != '':  # Linha 4-5-6
        mark_result('horizontal' , 'middle')
        return board[3]
    elif board[6] == board[7] == board[8] and board[6] != '':  # Linha 7-8-9
        mark_result('horizontal' , 'bottom')
        return board[6]

    # 6.2 - Verificar Verticais
    if board[0] == board[3] == board[6] and board[0] != '':  # Coluna 1-4-7
        mark_result('vertical' , 'left')
        return board[0]
    elif board[1] == board[4] == board[7] and board[1] != '':  # Coluna 2-5-8
        mark_result('vertical' , 'middle')
        return board[1]
    elif board[2] == board[5] == board[8] and board[2] != '':  # Coluna 3-6-9
        mark_result('vertical' , 'right')
        return board[2]

    # 6.3 - Verificar Diagonais
    if board[0] == board[4] == board[8] and board[0] != '':  # Diagonal 1-5-9
        mark_result('diagonal' , 'right')
        return board[0]
    elif board[2] == board[4] == board[6] and board[2] != '':  # Diagonal 3-5-7
        mark_result('diagonal' , 'left')
        return board[2]

    return None  # Nenhum vencedor ainda

def game_menu():
    """ Criar um menu interativo para o usuário escolher o simbolo x/o e começar a partida"""
    # configure screen
    screen.clearscreen()
    screen.setup(width=800 , height=600)

    # Create turtle object
    t = Turtle()
    t.hideturtle()  # set invisible
    t.penup()  # não deixar rastro
    t.shape("circle")

    # Exibe o banner do jogo
    x_central = 0  # Centralizado no eixo X
    y_topo = t.screen.window_height() // 2 - 50# Topo da tela (ajuste para centralizar)

    global banner
    linhas = banner.split("\n")
    for i , linha in enumerate(linhas):
        t.goto(x_central , y_topo - (i * 15))  # Desce 30px por linha
        t.write(linha , align="center" , font=("Courier" , 10 , "bold"))  # Centraliza cada linha

    #Menssagem do menu
    t.goto(0,50)
    t.write( 'Choose your symbol', align="center" , font=("Courier" , 24 , "bold"))

    screen.onscreenclick(menu_option)
    t.goto(-250,-150)
    t.write('🅧 | 🅞', font=('Arial', 150, 'bold'))

def mark_result(horientation, direction):
    """Marca na tela a partir do index quadrante"""
    marker=Turtle()
    marker.hideturtle()
    marker.pensize(15)
    marker.teleport(*marker_positions[horientation][direction][0])
    marker.pendown()
    marker.goto(marker_positions[horientation][direction][1])
    del marker

def mark_play(player_symbol, player_quadrant):
    global symbol_positions
    if player_quadrant is not None:
        marker = Turtle()
        marker.hideturtle()  # set invisible
        marker.penup()  # não deixar rastro
        marker.speed(0)
        marker.goto(symbol_positions[player_quadrant])
        marker.write(player_symbol, font=('Arial' , 125 , 'bold'))
        player_quadrant = None
        del marker

def quadrant_is_empty(index):
    return board[index] == ''

def pc_choice():
    """Escolha do PC baseada na lógica de buscar 2 símbolos consecutivos."""
    global board, pc_symbol

    # Todas as combinações possíveis de 3 posições no tabuleiro (horizontal, vertical e diagonal)
    winning_combinations = [
        (0, 1, 2),  # Linha superior
        (3, 4, 5),  # Linha do meio
        (6, 7, 8),  # Linha inferior
        (0, 3, 6),  # Coluna esquerda
        (1, 4, 7),  # Coluna do meio
        (2, 5, 8),  # Coluna direita
        (0, 4, 8),  # Diagonal principal
        (2, 4, 6)   # Diagonal secundária
    ]

    #  Procurar por duas peças iguais e uma posição vazia
    for a, b, c in winning_combinations:
        # Se duas posições possuem o mesmo símbolo (X ou O) e a terceira está vazia
        if board[a] == board[b] != '' and quadrant_is_empty(c):  # Ex: X X _
            board_registry(pc_symbol, c)  # Registra a jogada do PC
            print(f"PC marcou na posição {c} para completar ({a}, {b}, {c})")
            return c
        elif board[a] == board[c] != '' and quadrant_is_empty(b):  # Ex: X _ X
            board_registry(pc_symbol, b)
            print(f"PC marcou na posição {b} para completar ({a}, {b}, {c})")
            return b
        elif board[b] == board[c] != '' and quadrant_is_empty(a):  # Ex: _ X X
            board_registry(pc_symbol, a)
            print(f"PC marcou na posição {a} para completar ({a}, {b}, {c})")
            return a

    # Se não houver duas peças iguais, marcar um espaço vazio aleatório
    empty_positions = [i for i in range(9) if quadrant_is_empty(i)]
    if empty_positions:
        choice = random.choice(empty_positions)
        board_registry(pc_symbol, choice)
        print(f"PC marcou na posição {choice} aleatoriamente.")
        return choice
    else:
        game_end('draw')


def board_registry(player_symbol, player_quadrant):
    """Registra o símbolo do jogador no tabuleiro se a posição estiver vazia."""
    global board
    if quadrant_is_empty(player_quadrant):
        print(f'Registro: {player_symbol} no quadrante {player_quadrant}')
        board[player_quadrant]=player_symbol
    else:
        print(f"Posição {player_quadrant} já está ocupada!")
        # posição já preenchida
        game_play() # Se a posição já estiver ocupada, reinicia o jogo

def game_restart(x,y):
    """Check if user want another game."""
    if (-189 <= x <= -69) and (-199 <= y <= -79):
        game_play(menu=True)
    elif(47<= x <= 168) and (-199 <= y <= -79):
        screen.bye()
    else:
        print('clique fora das opções')

def game_end(result):
    global user_symbol, restart
    screen.clearscreen()
    marker = Turtle()
    marker.hideturtle()
    marker.penup()
    marker.goto(-200,100)
    if user_symbol == result:
        marker.write('You Wiiiinn (>‿◠)✌', font=('Arial' , 30 , 'bold'))
    elif pc_symbol == result :
        marker.write('You Loooose  (ㆆ_ㆆ)' , font=('Arial' , 30 , 'bold'))
    else:
        marker.goto(-250 , 100)
        marker.write('Draw!  (👍≖‿‿≖)👍 👍(≖‿‿≖👍)' , font=('Arial' , 30 , 'bold'))

    marker.goto(0,0)
    marker.write('🅿🅻🅰🆈 🅰🅶🅰🅸🅽 ❓' , align="center" , font=("Arial" , 45 , "normal"))  # Centraliza cada linha

    marker.goto(-200,-200)
    marker.write('✅ | ❎' , font=('Arial' , 80 , 'bold'))


    screen.onscreenclick(game_restart)


def game_play(menu=False):
    """Configure and create the gameplay."""
    global board, funtion_name, user_symbol, quadrant
    if menu:
        game_menu() # menu é executado uma única vez
        board = ['','','','','','','','',''] # reset board
    else:
        # configure screen
        screen.setup(width=600 , height=600)
        screen.bgpic('jogo da velha.png')
        screen.onscreenclick(user_choice)

        empty_positions = [i for i in range(9) if quadrant_is_empty(i)]
        if not empty_positions:
            game_end('draw')
            return

        if quadrant is not None: #Ou seja aguarda pela jogada do usuário
            board_registry(user_symbol, quadrant) # Verificar se a escolha é válida e registra jogada
            mark_play(user_symbol, quadrant) # Marca no tabuleiro

            result = winner_calculate()
            # procesar resultado
            if result is not None:
                game_end(result)

            choice = pc_choice()
            mark_play(pc_symbol, choice)
            result = winner_calculate()
            if result is not None:
                game_end(result)

game_play(menu=True)

screen.mainloop()








