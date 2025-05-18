label cap_2start_auak:
    scene restaurante

    show nerkk at right
    show auak:
        xpos 0.6
        ypos 0.3
    
    nerkk "Então o professor nos enviou como a esperança de salvar a escola?"

    auak "Isso!"

    nerkk "Espero que sejamos capazes de encontrar logo o que buscamos. Você acha que vai ser muito difícil?"

    auak "Claro que não! Só vai depender de nós quão fácil vai ser."

    menu:
        "Você gostaria de iniciar um furacão para atrapalhar a jornada?"

        "Sim":
            jump causar_furacao
        "Não":
            jump nao_causar_furacao

label causar_furacao:

    play sound "vento.mp3"
    pause

    nerkk "Que barulho foi esse?"

    auak "Imagino que não seja nada bom."

    scene restaurante exterior

    pause

    scene restaurante

    show nerkk ataque at right
    show auak ataque:
        xpos 0.4
        ypos 0.3

    nerkk "Meu deus! É um furacão!"

    auak "Um furacão?! O que vamos fazer?"

    nerkk "Vamos pedir ajuda!"

    auak "(Droga!)"

    nerkk "Alguém pode nos ajudar?"

    show ricardo ataque at left
    show Pagesh ataque:
        xpos 0.2
        ypos 0.3
    pause

    pagesh "Não se preocupem! Nós somos do ano acima e já vimos a magia elemental do vento."

    ricas "Sim! É só fazer o vento no sentido contrário do furacão!"

    play sound "vento.mp3"

    nerkk "Está funcionando!"

    hide Pagesh ataque
    hide ricardo ataque
    hide auak ataque
    hide nerkk ataque

    show auak at right
    show nerkk:
        xpos 0.3
        ypos 0.3
    show ricardo at left
    show Pagesh:
        xpos 0.2
        ypos 0.3

    auak "Perfeito! Conseguimos! Muito obrigado pela ajuda. Quem são vocês?"

    pagesh "Eu com essa barba maravilhosa sou o Pagesh."

    ricas "E eu sou o Kuracier. Ficaram sabendo do que aconteceu na escola?"

    nerkk "Sim. Por isso estamos aqui. Somos a esperança de salvar a escola. Não sei como vamos fazer isso. Se não fosse por vocês já estaríamos fritos, sendo que mal começamos."

    ricas "Podemos acompanhar vocês se quiserem."

    nerkk "Sim! Seria perfeito!"

    jump cap_3_auak

label nao_causar_furacao:
    show ricardo at left
    show Pagesh:
        xpos 0.2
        ypos 0.3
    
    ricas "Oi pessoal! Ficaram sabendo do que aconteceu na escola?"

    nerkk "Sim. Por isso estamos aqui. Somos a esperança de salvar a escola."

    pagesh "Nossa! Podemos ir com vocês? Somos do ano acima, podemos ajudar."

    auak "Não sei não..."

    nerkk "Claro que podem! Quanto mais ajuda melhor!"

    pagesh "Maravilha! Eu com essa barba maravilhosa sou o Pagesh."

    ricas "E eu sou o Kuracier."

    auak "Ótimo! Agora vamos logo!"

    jump cap_3_auak