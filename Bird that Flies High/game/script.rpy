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
            
        label acertou_1:
            $ pts += 1

            prof "Muito bem! Acertou em cheio! As mãos são importantes porque são a forma de canalizar a magia através do corpo, mas existem outras formas de canalizar magia, como varinhas ou outros objetos."

            jump cena_2
        
        label errou_1:
            prof "Não é bem isso! As mãos são importantes porque são a forma de canalizar a magia através do corpo, mas existem outras formas de canalizar magia, como varinhas ou outros objetos."

            jump cena_2
        label cena_2:
            prof "Por hoje ficamos por aqui turma. Estão dispensados."
            hide professor abaixado
            with dissolve

            pause

            player "Que aula legal!"

            principal "Meu sonho sempre foi ser um biólogo mágico."
            if player=="Thomas":
                aluno_2 "Que bacana! Nunca pensei muito no meu futuro, acho que sempre gostei de viver o presente."
            else:
                principal "E você Auak? Qual é seu sonho?"

    

    # This ends the game.

    return
