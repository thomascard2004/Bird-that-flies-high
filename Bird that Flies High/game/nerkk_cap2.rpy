label cap_2start_nerkk:
    scene restaurante

    show auak at right
    show nerkk:
        xpos 0.6
        ypos 0.3
    
    auak "Então o professor nos enviou como a esperança de salvar a escola?"

    nerkk "Isso!"

    auak "Espero que sejamos capazes de encontrar logo o que buscamos. Você acha que vai ser muito difícil?"

    nerkk "Claro que não! Só vai depender de nós quão fácil vai ser."

    play sound "vento.mp3"
    pause

    auak "Que barulho foi esse?"

    nerkk "Imagino que não seja nada bom."

    scene restaurante exterior

    pause

    scene restaurante

    show auak ataque at right
    show nerkk ataque:
        xpos 0.4
        ypos 0.3

    nerkk "Meu deus! É um furacão!"

    auak "Um furacão?! O que vamos fazer?"

    menu:
        "Pedir Ajuda??"

        "Sim":
            jump pedir_ajuda
        
        "Não":
            jump nao_pedir_ajuda
