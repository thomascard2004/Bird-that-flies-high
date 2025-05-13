label nerkk_start:

    $ player = "Thomas"

    scene bg_saladeaula

    show professor abaixado at truecenter

    prof "A anatomia de um mago é bem simples de entender. Ele possui tudo que um humano possui com uma pequena adição."

    prof "Um mago tem um \"saco\" de magia que funciona como um coração e tem como função bombear magia pelo corpo do mago, assim como o coração bombeia sangue."

    

    $ pts = 0
    $ maldade = 0

    show auak at right

    auak "Professor, se a magia é bombeada pelo corpo inteiro, por que precisamos usar as mãos para fazer magia?"

    prof "Excelente pergunta! Alguém sabe responder?"

    show thomas at left

    nerkk "Eu sei!"
    
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

label boom_nerkk:
    menu:
        "Escolha uma ação"

        "Se esconder embaixo das cadeiras!":
            jump hide
        "Ir investigar o que aconteceu.":
            jump investigar_nerkk
        "Fazer xixi nas calças de medo.":
            jump xixi
        "Mandar auak ir ver o que aconteceu.":
            jump investigar_auak

label investigar_nerkk:
    scene bg_exterior_saladeaula

    show thomas at center

    nerkk "Acho que o barulho veio daqui. Vou dar uma espiada."

    nerkk "Meu Deus! O que é isso?"

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
    return