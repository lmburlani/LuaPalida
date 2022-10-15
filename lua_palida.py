import random
import time
import math
OURO = 0
PÁ = 0
CORDA = 0
BURACO = 0

# Define Commands
def introGame():
    global PÁ
    global OURO
    global CORDA
    print("V.0.9")
    print()
    time.sleep(0)
    print("LUA PÁLIDA")
    time.sleep(0)
    print()
    print("Jogo feito por Luiz B.")
    print("Esse jogo é uma reimaginação do Pale Luna")
    print()
    time.sleep(1)
    s = input("Pressione Enter para começar: ")
    if s == "{s":
        print()
        print("-- { DEV > SKIP TO PLAYGAME()")
        playGame()
    elif s == "{s2":
        OURO = 1
        PÁ = 1
        CORDA = 1
        print()
        print("-- { DEV > SKIP TO PART3()")
        part3()
    elif s == "{sE":
        OURO = 1
        PÁ = 1
        CORDA = 1
        print()
        print("-- {DEV > SKIP TO PLAYGAME6()")
        playGame6()
    else:
        print()
        print()
        startGame()

def startGame():
    global PÁ
    global OURO
    global CORDA
    time.sleep(2)
    print()
    print("Você está em um quarto escuro. O luar brilha através da janela.")
    time.sleep(0.5)

    #-----------------------------------------------------------------------------

    print("Tem OURO na esquina, junto com um PÁ e um CORDA.")
    time.sleep(0.1)
    print("Há uma PORTA para o LESTE")
    print()
    print()
    time.sleep(2)
    print("Comando?")
    print()
    time.sleep(0.5)
    print("Você pode ver uma PORTA aqui.")
    print()
    playGame()

def playGame():
    global OURO
    global PÁ
    global CORDA
    s = input(">")
    if s == "PEGAR OURO":
        if OURO == 0:
            time.sleep(2.5)
            print("-- Pegou")
            OURO = 1
            print()
            playGame()
        else:
            print("-- Você já pegou este item.")
            print()
            playGame()
    elif s == "SAIR PELA PORTA":
        part2()

    elif s == "PEGAR PÁ":
        if PÁ == 0:
            time.sleep(2.5)
            print("-- Pegou")
            PÁ = 1
            print()
            playGame()
        else:
            print("-- Você já pegou este item.")
            print()
            playGame()
    elif s == "PEGAR CORDA":
        if CORDA == 0:
            time.sleep(2.5)
            print("-- Pegou")
            CORDA = 1
            print()
            playGame()
        else:
            print("-- Você já pegou este item.")
            print()
            playGame()
    elif s == "PEGAR OURO, PÁ, CORDA":
        time.sleep(1.4)
        print("-- OURO   > Pego.")
        print("-- PÁ > Pego.")
        print("-- CORDA   > Pego.")
        CORDA = 1
        OURO = 1
        PÁ = 1
        print()
        playGame()

    else:
        time.sleep(1)
        print("--Eu não entendo isso.")
        print()
        playGame()

def part2():
    time.sleep(2)
    print()
    print("Colha sua recompensa.")
    print()
    time.sleep(2)
    print("LUNA PÁLIDA SORRI PARA VOCÊ!")
    time.sleep(1)
    print()
    print()
    print("Você está em uma floresta. Há ")
    time.sleep(0.1)
    print("caminhos para o NORTE, OESTE e LESTE. ")
    print()
    time.sleep(1)
    print("Comando?")
    print()
    playGame2()

def playGame2():
    global PÁ
    global OURO
    global CORDA
    s0 = input(">")
    if s0 == "USE OURO":
        if OURO == 1:
            time.sleep(2.5)
            OURO = 1
            print("-- Agora não.")
            print()
            playGame2()
        else:
            print("-- Você não tem tal item.")
            print()
            playGame2()
    elif s0 == "USE PÁ":
        if PÁ == 1:
            time.sleep(1.4)
            PÁ = 1
            print("-- Aqui não.")
            print()
            playGame2()
        else:
            print("-- Você não tem tal item.")
            print()
            playGame2()
    elif s0 == "USE CORDA":
        if CORDA == 1:
            time.sleep(1.4)
            CORDA = 2
            print("-- Você já usou este item.")
            print()
            playGame2()
        else:
            print("-- Você não tem tal item.")
            print()
            playGame2()
    elif s0 == "LESTE":
        print()
        part3()
    elif s0 == "OESTE":
        print()
        gameOver()
    elif s0 == "NORTE":
        print()
        gameOver()
    else:
        print("--Eu não entendo isso.")
        print()
        playGame2()

def part3():
    time.sleep(0.5)
    print()
    print("Colha sua recompensa.")
    print()
    time.sleep(0.5)
    print("LUA PÁLIDA SORRI PARA VOCÊ!")
    time.sleep(1)
    print()
    print()
    print("Você está em uma floresta. Há ")
    time.sleep(0.1)
    print("Tem caminhos para  NORTE, OESTE, and LESTE.")
    print()
    time.sleep(1)
    print("Comando?")
    print()
    playGame3()

def playGame3():
    global PÁ
    global OURO
    global CORDA
    s0 = input(">")
    if s0 == "USE OURO":
        if OURO == 1:
            time.sleep(1.4)
            OURO = 1
            print("-- Agora não.")
            print()
            playGame3()
        else:
            print("-- Você não tem tal item.")
            print()
            playGame3()
    elif s0 == "USE PÁ":
        if PÁ == 1:
            time.sleep(1.4)
            PÁ = 1
            print("-- Aqui não.")
            print()
            playGame3()
        else:
            print("-- Você não tem tal item.")
            print()
            playGame3()
    elif s0 == "USE CORDA":
        if CORDA == 1:
            time.sleep(1.4)
            CORDA = 1
            print("-- Você já usou este item.")
            print()
            playGame3()
        else:
            print("-- Você não tem tal item.")
            print()
            playGame3()

    elif s0 == "NORTE":
        if CORDA == 1:
            if OURO == 1:
                if PÁ == 1:
                    print()
                    part4()
                else:
                    part4()
            else:
                part4()
        else:
            part4()
    elif s0 == "LESTE":
        print()
        gameOver()
    elif s0 == "OESTE":
        print()
        gameOver()
    else:
        print("-- Eu não entendo isso. Digite na direção indicada.")
        print()
        playGame3()

def part4():
    time.sleep(0.5)
    print()
    print("Colha sua recompensa.")
    print()
    time.sleep(0.5)
    print("LUA PÁLIDA SORRI PARA VOCÊ!")
    time.sleep(1)
    print()
    print()
    print("Você está em uma floresta. Há ")
    time.sleep(0.1)
    print("Tem caminhos para  SUL and LESTE.")
    print()
    time.sleep(1)
    print("Comando?")
    print()
    playGame4()

def playGame4():
    global PÁ
    global OURO
    global CORDA
    s0 = input(">")
    if s0 == "USE OURO":
        if OURO == 1:
            time.sleep(1.4)
            OURO = 1
            print("-- Agora não.")
            print()
            playGame4()
        else:
            print("-- Você não tem tal item.")
            print()
            playGame4()
    elif s0 == "USE PÁ":
        if PÁ == 1:
            time.sleep(1.4)
            PÁ = 1
            print("-- Aqui não.")
            print()
            playGame4()
        else:
            print("-- Você não tem tal item.")
            print()
            playGame4()
    elif s0 == "USE CORDA":
        if CORDA == 1:
            time.sleep(1.4)
            CORDA = 1
            print("-- Você já usou este item.")
            print()
            playGame4()
        else:
            print("-- Você não tem tal item.")
            print()
            playGame4()

    elif s0 == "SUL":
        print()
        part5()

    elif s0 == "LESTE":
        print()
        gameOver()
    elif s0 == "DEVORAR":
        print()
        gameOver()
    else:
        print("-- Eu não entendo isso. Digite na direção indicada.")
        print()
        playGame4()

def part5():
    time.sleep(0.5)
    print()
    print("Colha sua recompensa.")
    print()
    time.sleep(0.5)
    print("LUA PÁLIDA SORRI PARA VOCÊ!")
    time.sleep(1)
    print()
    print()
    print("Você está em uma floresta. Há ")
    time.sleep(0.1)
    print("Tem caminhos para  OESTE and LESTE.")
    print()
    time.sleep(1)
    print("Comando?")
    print()
    playGame5()

def playGame5():
    global PÁ
    global OURO
    global CORDA
    s0 = input(">")
    if s0 == "USE OURO":
        if OURO == 1:
            time.sleep(1.4)
            OURO = 1
            print("-- Agora não.")
            print()
            playGame5()
        else:
            print("-- Você não tem tal item.")
            print()
            playGame5()
    elif s0 == "USE PÁ":
        if PÁ == 1:
            time.sleep(1.4)
            PÁ = 1
            print("-- Aqui não.")
            print()
            playGame5()
        else:
            print("-- Você não tem tal item.")
            print()
            playGame5()
    elif s0 == "USE CORDA":
        if CORDA == 1:
            time.sleep(1.4)
            CORDA = 1
            print("-- Você já usou este item.")
            print()
            playGame5()
        else:
            print("-- Você não tem tal item.")
            print()
            playGame5()

    elif s0 == "OESTE":
        print()
        part6()

    elif s0 == "LESTE":
        print()
        gameOver()
    elif s0 == "DEVORAR":
        print()
        gameOver()
    else:
        print("-- Eu não entendo isso. Digite na direção indicada.")
        print()
        playGame5()

def part6():
    print()
    time.sleep(1)
    print("LUA PÁLIDA SORRIU ABRANGENTE")
    print()
    time.sleep(2)
    print("Não há caminhos")
    print()
    time.sleep(1)
    print("LUA PÁLIDA SORRIU ABRANGENTE")
    print()
    time.sleep(2)
    print("O chão é macio")
    print()
    time.sleep(1)
    print("aQUI")
    time.sleep(1)
    print()
    print("Comando?")
    print()
    playGame6()

def playGame6():
    global PÁ
    global OURO
    global CORDA
    global BURACO
    s = input(">")
    if s == "CAVAR BURACO":
        if PÁ == 1:
            if BURACO == 0:
                time.sleep(1.4)
                BURACO = 1
                print("-- Você cavou um BURACO.")
                print()
                playGame6()
            else:
                print("-- Você não pode cavar outro BURACO.")
                print()
                playGame6()
        else:
            print("-- Você não consegue cavar um BURACO com as mãos!")
            print()
            playGame6()
    elif s == "JOGAR OURO":
        if BURACO == 1:
            if OURO == 1:
                time.sleep(1.4)
                OURO = 2
                print("-- Você jogou OURO no BURACO.")
                print()
                playGame6()
            else:
                print("-- Você não tem nada disso.")
                print()
                playGame6()
        else:
            time.sleep(1.4)
            print("-- Você deixou o OURO cair no chão.")
            OURO = 0
            print()
            playGame6()
    elif s == "PEGAR OURO":
        if OURO == 0:
            if BURACO == 0:
                time.sleep(1.4)
                print("-- Pegou.")
                OURO = 1
                print()
                playGame6()
            else:
                print("-- Você não pode pegar o OURO no BURACO.")
                print()
                playGame6()
        elif OURO == 1:
            print("-- Você não pode pegar tal coisa.")
            print()
            playGame6()
        elif OURO == 2:
            if BURACO == 1:
                print("-- Você não pode pegar OURO no BURACO.")
                print()
                playGame6()
            else:
                print("Fatal Error.") # Condição impossível
        else:
            print("Fatal Error.") # Condição impossível

    elif s == "LESTE":
        print("-- Não há caminhos.")
        print()
        playGame6()
    elif s == "OESTE":
        print("-- Não há caminhos.")
        print()
        playGame6()
    elif s == "SUL":
        print("-- Não há caminhos.")
        print()
        playGame6()
    elif s == "NORTE":
        print("-- Não há caminhos.")
        print()
        playGame6()
    elif s == "PREENCHER BURACO":
        if BURACO == 1:
            if OURO == 2:
                time.sleep(1.4)
                print("-- Você encheu BURACO.")
                BURACO = 0
                time.sleep(1)
                print()
                endGame()
            else:
                time.sleep(1.4)
                print("-- Você encheu BURACO.")
                BURACO = 0
                print()
                playGame6()
        else:
            print("-- Não tem BURACO para preencher.")
    else:
        print("--Eu não entendo isso.")
        print()
        playGame6()

def endGame():
    print()
    time.sleep(1)
    print("PARABÉNS!!!!!")
    print("---- 40.24248 ----")
    print("---- -121.4434 ----")
    time.sleep(2)
    print("Jogo. Encerrado")
    time.sleep(1)
    print()
    s = input("Enter para Continuar ou digite quit:")
    if s == "quit":
        print()
        print("Obrigado por jogar...")
        time.sleep(2)
    else:
        final()

def final():
    time.sleep(2)
    input("Você finalmente percebe que esses números")
    input(" no final do jogo eram coordenadas")
    input("de Longitude e Latitude. Ao usar os mapas")
    input(" você localiza o local perto do Parque Vulcânico Lassen.")
    input()
    input("Você decide caminhar sozinho para o local porque você ")
    input(" acreditar que o criador do jogo foi embora")
    input("algum tesouro atrás. Você viaja na floresta.")
    input("Você segue conjuntos de caminhos.")
    input()
    input("Você então começa a notar estranhamente que os caminhos que você")
    input(" pegue os mesmos caminhos no jogo. Você começa")
    input("para saber que algo parece um pouco fora.")
    input()
    input("Você então chega a um ponto onde não havia mais caminhos, apenas")
    input(" como no jogo. Você está confuso até perceber isso")
    input("Você estava pisando em terreno irregular. Tomando seu PÁ, você")
    input(" começar a cavar, esperando por algum tesouro perdido até. ")
    input("a cabeça decadente da menina loira apareceu...")
    input()
    input("Então tudo é colocado na sua cabeça...")
    input("Lua pálida sorri largamente...")
    input("Ouro... Cabelo loiro.")
    input("Colha sua recompensa... sufoque a garota com o CORDA...")
    input("LUA PÁLIDA SORRI AMPLAMENTE.")
    input("Jogar Ouro... encher BURACO...")
    input()
    input("A próxima coisa que você faz, você chama a polícia imediatamente. A garota")
    input(" foi identificada como Karen Paulsen, 11 anos. Ela era")
    input("desaparecido por um ano e meio de acordo com a polícia de San Diego.")
    input("O resto do corpo de Karen nunca foi encontrado...")

def gameOver():
    global OURO
    global PÁ
    global CORDA
    print("Desculpe, mas você perdeu...")
    time.sleep(4)
    print()
    print("Tentar novamente? ('Sim'/'Não')")
    s = input(">")
    if s == "s" or "sim" or "SIM" or "Sim":
        print()
        PÁ = 0
        CORDA = 0
        OURO = 0
        startGame()
    else:
        print()
        print("Que perdedor..")
        time.sleep(2)
#Comandos rodam aqui
introGame()
