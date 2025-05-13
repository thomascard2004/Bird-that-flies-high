# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#BACKGROUNDS
image bg_saladeaula = Transform( "bgs/sala_de_aula.png", zoom = 1.3)
image bg_exterior_saladeaula = Transform("bgs/exterior_sala.png", zoom=1.3)

image castelo = Transform("bgs/castelo_em_ruinas.png", zoom = 1.3)
image ricardo = Transform("rickauer_sf.png", zoom = 1.3)
image thomas = Transform( "thomas_sf.png", zoom = 1.3)
image thomas transparente = Transform( "thomas_sf.png", zoom = 1.3, alpha=0.7)
image professor = Transform("professor.png", zoom = 0.8)
image professor abaixado = Transform("professor_abaixado.png", zoom = 0.8)

image auak = Transform("auak_sf.png", zoom=1.3)
image auak deitado = Transform("auak_sf.png", zoom=1.3, rotate=90)


#PERSONAGENS
define nerkk = Character("Thomas")
define auak = Character("Auak")
define prof = Character("Professor")

transform small_zoom:
    zoom 0.8

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg_saladeaula
    $ covardia = 0

    menu escolha_jogador:

        "Qual jogador você escolhe?"

        "Thomas.":

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

    

label cena_1:

    $ pts = 0
    $ maldade = 0

    auak "Professor, se a magia é bombeada pelo corpo inteiro, por que precisamos usar as mãos para fazer magia?"

    prof "Excelente pergunta! Alguém sabe responder?"

    if player=="Thomas":
        nerkk "Eu sei!"
    else:
        auak "Eu sei!"

    menu:
        "Por que precisamos usar as mãos para fazer magia?"

        "Porque as maõs são a parte mais importante do corpo.":
            jump errou_1
        
        "Para canalizar a magia através das mãos.":
            jump acertou_1

        "Porque as mãos cresceram geneticamente com propósitos místicos.":
            jump errou_1
        
        "Porque as mãos são a parte do corpo que mais entra em contato físico com o mundo.":
            jump errou_1
        
    label acertou_1:
        $ pts += 1

        prof "Muito bem! Acertou em cheio! As mãos são importantes porque são a forma de canalizar a magia através do corpo, mas existem outras formas de canalizar magia, como varinhas ou outros objetos."

        jump cena_2
    
    label errou_1:
        prof "Não é bem isso! As mãos são importantes porque são a forma de canalizar a magia através do corpo, mas existem outras formas de canalizar magia, como varinhas ou outros objetos."

        jump cena_2

label cena_2:

    pause

    if player=="Thomas":
        auak "Como você sabe disso?"
        jump sim
    else:
        nerkk "Quer saber como sei disso?"
        menu:
            nerkk "Quer saber como sei disso?"

            "Sim!":
                jump sim
            "Não!":
                $ maldade+=1
                jump nao

label sim:

    nerkk "Meu sonho sempre foi ser um biólogo mágico."
    if player=="Thomas":
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

label acertou_2:
    prof "Muito bem! Você está corretíssimo! As únicas coisas que limitam a capacidade mágica de um mago são a sua criatividade e se ele possui magia o suficiente para realizar o ato mágico que deseja."

    jump resto_2

label errou_2:
    prof "Isso sempre é importante, mas não é necessário ao realizar uma magia. As únicas coisas que limitam a capacidade mágica de um mago são a sua criatividade e se ele possui magia 
    o suficiente para realizar o ato mágico que deseja."

    jump resto_2

label resto_2: 
    prof "Se um mago não tiver magia o suficiente para realizar o ato mágico, ele será realizado até o ponto em que o mago cessar a canalização de magia."

    auak "O que acontece se a magia de um mago acabar?"

    prof "Ótima pergunta! Para um mago a magia é tão vital para sua saúde quanto o sangue. Quando um mago esgota sua magia, ele morre."

    prof "No início dos tempos muitos magos morriam porque cediam toda a sua magia para realizar ações básicas. Então agora, vamos falar sobre otimização do uso de magia e métodos para realização de magia segura."

    prof "Vamos dizer que você está numa floresta e deseja criar uma cabana de madeira. Fazer isso \"do nada\" demandaria muita magia. É mais inteligente se você usar a madeira das árvores ao redor, ao seu favor."

    player "Usando telecinese?"

    prof "Você pode chamar assim porque está usando da sua mente para fazer o que você deseja com a madeira, mas no fim das contas telecinese é 
    apenas um jeito que os humanos inventaram de explicar a magia que eles não entendem."

    auak "Professor, eu tenho uma…"

    play sound "boom.mp3"

    nerkk "O que foi isso?"

    prof "Fiquem aqui, eu vou verificar o que foi isso!"

    hide professor abaixado
    with dissolve

    if player=="Thomas":
        jump boom_nerkk
    else:
        jump boom_auak

label xixi:
    show professor abaixado at truecenter
    with dissolve

    play sound "xixi.mp3"

    prof "Que barulho é esse?"

    player "Nada professor. Conseguiu descobrir o que aconteceu?"

    prof "Consegui! A causa da explosão foi..."

    menu:
        "Escolha a causa da explosão."

        "Opção 1.":
            jump opcao_1
        "Opção 2.":
            jump opcao_2
        "Opção 3.":
            jump opcao_3
        "Opção 4.":
            jump opcao_4

label esconder:
    player "Me avisa quando o professor voltar!"

    if player == "Thomas":
        hide thomas
        with dissolve
    else:
        hide auak
        with dissolve

    return






label cena_fora:
    scene castelo

    show ricardo at small_zoom, right
    show thomas  at small_zoom, center
    show auak    at small_zoom, left

    pause
    return

