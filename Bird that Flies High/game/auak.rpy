label auak_start:

    $ player = "Auak"

    scene bg_saladeaula

    show professor abaixado at truecenter

    prof "A anatomia de um mago é bem simples de entender. Ele possui tudo que um humano possui com uma pequena adição."

    prof "Um mago tem um \"saco\" de magia que funciona como um coração e tem como função bombear magia pelo corpo do mago, assim como o coração bombeia sangue."

    

    show auak at right

    auak "Professor, se a magia é bombeada pelo corpo inteiro, por que precisamos usar as mãos para fazer magia?"

    prof "Excelente pergunta! Alguém sabe responder?"

    show thomas at left

    nerkk "Eu sei! Para canalizar a magia através das mãos."

    jump acertou_1

label boom_auak:
    menu:
        "Fingir que se machucou.":
            jump fingir
        "Investigar o que aconteceu.":
            jump investigar_auak
        "Se esconder.":
            jump esconder
        "Fazer xixi nas calças de medo.":
            jump xixi

label fingir:
    $ maldade += 1

    show auak deitado

    auak "Thomas! Me ajuda!"

    nerkk "Meu Deus! Você está bem?"

    auak "Preciso que você me transfira magia! Senão não vou conseguir me curar."

    nerkk "OK! Toma então."

    show thomas transparente

    pause

    jump prof_voltou

label investigar_auak:
    scene bg_exterior_saladeaula

    show auak at center

    auak "Acho que o barulho veio daqui. Vou dar uma espiada."

    auak "Meu Deus! O que é isso?"

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
    return
