# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
image bg_saladeaula = Transform( "sala_de_aula.png", zoom = 1.3)
image thomas = Transform( "thomas_sf.png", zoom = 1.3)
define principal = Character("Thomas")
image castelo = Transform("castelo_em_ruinas.png", zoom = 1.3)
image ricardo = Transform("rickauer_sf.png", zoom = 1.3)
define aluno_2 = Character("Auak")
image professor = Transform("professor.png", zoom = 0.8)
image professor abaixado = Transform("professor_abaixado.png", zoom = 0.8)
define prof = Character("Professor")
image auak = Transform("auak_sf.png", zoom=1.3)

transform small_zoom:
    zoom 0.8

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg_saladeaula

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show professor abaixado at truecenter

    show thomas at right

    # These display lines of dialogue.

    prof "A anatomia de um mago é bem simples de entender. Ele possui tudo que um humano possui com uma pequena adição."

    prof "Um mago tem um \"saco\" de magia que funciona como um coração e tem como função bombear magia pelo corpo do mago, assim como o coração bombeia sangue."

    pause 

    show auak at left
    with dissolve

    aluno_2 "BOO!"

    aluno_2 "Sempre bom usar a magia para causar o caos."

    menu jogador:

        "Qual jogador você escolhe?"

        "Thomas.":
            $ player = "Thomas"

            jump cena_1

        "Auak.":
            $ player = "Auak"

            jump cena_1

label cena_1:

    $ pts = 0
    $ maldade = 0

    aluno_2 "Professor, se a magia é bombeada pelo corpo inteiro, por que precisamos usar as mãos para fazer magia?"

    prof "Excelente pergunta! Alguém sabe responder?"

    if player=="Thomas":
        principal "Eu sei!"
    else:
        aluno_2 "Eu sei!"

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
        aluno_2 "Como você sabe disso?"
        jump sim
    else:
        principal "Quer saber como sei disso?"
        menu:
            principal "Quer saber como sei disso?"

            "Sim!":
                jump sim
            "Não!":
                $ maldade+=1
                jump nao

label sim:

    principal "Meu sonho sempre foi ser um biólogo mágico."
    if player=="Thomas":
        aluno_2 "Que bacana! Nunca pensei muito no meu futuro, acho que sempre gostei de viver o presente."
    else:
        principal "E você Auak? Qual é seu sonho?"
        aluno_2 "Nunca pensei muito no meu futuro, acho que sempre gostei de viver o presente."
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

    aluno_2 "O que acontece se a magia de um mago acabar?"

    prof "Ótima pergunta! Para um mago a magia é tão vital para sua saúde quanto o sangue. Quando um mago esgota sua magia, ele morre."

    prof "No início dos tempos muitos magos morriam porque cediam toda a sua magia para realizar ações básicas. Então agora, vamos falar sobre otimização do uso de magia e métodos para realização de magia segura."

    prof "Vamos dizer que você está numa floresta e deseja criar uma cabana de madeira. Fazer isso \"do nada\" demandaria muita magia. É mais inteligente se você usar a madeira das árvores ao redor, ao seu favor."

    player "Usando telecinese?"

    prof "Você pode chamar assim porque está usando da sua mente para fazer o que você deseja com a madeira, mas no fim das contas telecinese é 
    apenas um jeito que os humanos inventaram de explicar a magia que eles não entendem."

    aluno_2 "Professor, eu tenho uma…"

    play sound "boom.mp3"

    prof "Por hoje ficamos por aqui turma. Estão dispensados."
    hide professor abaixado
    with dissolve

    player "Que aula legal!"

    jump cena_fora



label cena_fora:
    scene castelo

    show ricardo at small_zoom, Position(xalign=0.25, yalign=2)
    show thomas  at small_zoom, center
    show auak    at small_zoom, Position(xalign=0.75, yalign=2)

    pause
    return

