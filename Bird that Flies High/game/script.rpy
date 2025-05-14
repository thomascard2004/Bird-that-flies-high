# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#BACKGROUNDS
image bg_saladeaula = Transform( "bgs/sala_de_aula.png", zoom = 1.3)
image bg_exterior_saladeaula = Transform("bgs/exterior_sala.png", zoom=1.3)

image castelo = Transform("bgs/castelo_em_ruinas.png", zoom = 1.3)
image ricardo = Transform("rickauer_sf.png", zoom = 1.3)
image nerkk = Transform( "thomas_sf.png", zoom = 1.3)
image nerkk_t = Transform( "thomas_sf.png", zoom = 1.3, alpha=0.7)
image professor = Transform("professor.png", zoom = 0.8)
image professor abaixado = Transform("professor_abaixado.png", zoom = 0.8)
image bolsa = Transform("personagens/bolsa.png", zoom=0.8)
image popotino = Transform("personagens/popotino.png", zoom=1.3)
image auak = Transform("auak_sf.png", zoom=1.3)
image auak deitado = Transform("auak_sf.png", zoom=1.3, rotate=90)


#PERSONAGENS
define nerkk = Character("Nerkk")
define auak = Character("Auak")
define prof = Character("Professor")
define ricas = Character("RiKauer")
define pagesh = Character("Pagesh")
define pint = Character("Moça da Pintura")

transform small_zoom:
    zoom 0.8

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    jump castelo_inside
    scene bg_saladeaula
    $ covardia = 0
    $ pts = 0
    $ maldade = 0
    $ opcao = ""

    menu escolha_jogador:

        "Qual jogador você escolhe?"

        "Nerkk.":

            jump nerkk_start

        "Auak.":

            jump auak_start
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    

    

    # These display lines of dialogue.

    prof "A anatomia de um mago é bem simples de entender. Ele possui tudo que um humano possui com uma pequena adição."

    prof "Um mago tem um \"saco\" de magia que funciona como um coração e tem como função bombear magia pelo corpo do mago, assim como o coração bombeia sangue."

    pause 

    show auak at left
    with dissolve

    auak "BOO!"

    auak "Sempre bom usar a magia para causar o caos."

    

label sim:

    nerkk "Meu sonho sempre foi ser um biólogo mágico."
    if player=="Nerkk":
        auak "Que bacana! Nunca pensei muito no meu futuro, acho que sempre gostei de viver o presente."
    else:
        nerkk "E você Auak? Qual é seu sonho?"
        auak "Nunca pensei muito no meu futuro, acho que sempre gostei de viver o presente."
    jump nao

label nao:

    prof "Como eu ia dizendo, a magia flui pelo corpo inteiro, quando usamos as mãos estamos apenas canalizando a magia em uma parte do corpo em que temos pleno controle."

    prof "Algúem sabe quais são os pré requisitos para realizar uma magia bem sucedida?"

    player "Eu!"

    menu:
        "Quais são os pré requisitos para realizar uma magia bem sucedida?"

        "Ter criatividade e ter a quantidade de magia necessária com excedente saudável":
            jump acertou_2
        "Calma e paciência":
            jump errou_2
        "Foco e conhecimento":
            jump errou_2
        "Disruptividade e moedas de ouro":
            jump errou_2


label esconder:
    player "Me avisa quando o professor voltar!"

    if player == "Nerkk":
        hide thomas
        with dissolve
    else:
        hide auak
        with dissolve
    
    jump prof_voltou

    return

label prof_voltou:
    show professor abaixado
    with dissolve

    prof "Oi pessoal. Consegui descobrir o que aconteceu. A causa da explosão foi..."

    menu:
        "Escolha a causa da explosão."

        "Foi o Poppotino Griffino.":
            jump opcao_1
        "Opção 2.":
            jump opcao_2
        "Opção 3.":
            jump opcao_3
        "Opção 4.":
            jump opcao_4





label cena_fora:
    scene castelo

    show ricardo at small_zoom, right
    show thomas  at small_zoom, center
    show auak    at small_zoom, left

    pause
    return

