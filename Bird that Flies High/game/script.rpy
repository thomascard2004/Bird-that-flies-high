# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
image bg_saladeaula = Transform( "sala_de_aula.png", zoom = 1.3)
image thomas = Transform( "thomas_sf.png", zoom = 1.3)
define principal = Character("Thomas")
image castelo = Transform("castelo_em_ruinas.png", zoom = 1.3)
image ricardo = Transform("rickauer_sf.png", zoom = 1.3)
define aluno_2 = Character("Ricardo")
image professor = Transform("professor.png", zoom = 0.8)
image professor abaixado = Transform("professor_abaixado.png", zoom = 0.8)
define prof = Character("Professor")


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

    show ricardo at left
    with dissolve

    aluno_2 "BOO!"

    aluno_2 "Sempre bom usar a magia para causar o caos."

    

    # This ends the game.

    return
