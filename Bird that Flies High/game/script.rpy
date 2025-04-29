# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
image bg_saladeaula = Transform( "sala_de_aula.png", zoom = 1.3)
image thomas = Transform( "thomas_sf.png", zoom = 1.3)
define principal = Character("Thomas")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg_saladeaula

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show thomas at right

    # These display lines of dialogue.

    principal "You've created a new Ren'Py game."

    principal "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
