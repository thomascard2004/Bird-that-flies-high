label cap_3start:

    scene trilha

    show nerkk at right
    show auak at left
    show ricardo:
        xpos 0.6
        ypos 0.3
    show Pagesh:
        xpos 0.1
        ypos 0.3

    auak "Pelas palavras do professor, acho que devemos seguir nessa direção"
    auak "Podem ir na frente, eu vou só fazer um xixizinho maroto"

    hide auak
    with dissolve

    nerkk "Bem, vamos andando então, não temos tempo a perder!"
    ricas "Certo, vamos lá."

    "Vocês caminham um pouco até que..."

    jump ave


label ave:
    
    scene floresta

    show nerkk at right
    show ricardo:
        xpos 0.6
        ypos 0.3
    show Pagesh:
        xpos 0.1
        ypos 0.3


    "Um súbito bater de asas chama a atenção."
    show falcao_voando at center
    pause 0.5
    hide falcao_voando
    show falcao_parado at center


    falcao "Bom dia, viajantes. Como posso ajudá-los?" 
    nerkk "Estamos tentando chegar ao castelo que fica além desta floresta. Sabe o melhor caminho?"


    falcao "Hmm, o castelo..."
    falcao "O lago é extremamente traiçoeiro, repleto de criaturas perigosas. A morte é certa."
    falcao "A floresta é o caminho mais direto. Tenho certeza de que obterão sucesso."
    falcao "O que me dizem?"

    menu falar_com_ave_escolhas:
        "Seguir pela floresta.":
            jump caminho_floresta
        
        "Tentar um teleporte, usando magia":
            jump tp_floresta

        "Ir pelo meio do lago.":
            jump caminho_lago


label caminho_lago:
    scene lago2

    show nerkk at right
    show ricardo:
        xpos 0.6
        ypos 0.3
    show Pagesh:
        xpos 0.1
        ypos 0.3
    hide falcao_parado
    with dissolve
    pause 0.5
    show auak at left


    auak "Ufa... consegui alcançar vocês. Vamos pelo lago né? Um pássaro estranho me falou que era meio perigoso..."
    ricas "Ah... ele deve estar exagerando só!"
    nerkk "O lago, então. Como vamos atravessar?"
    pagesh "Bem, sempre tem a opção de atravessar a nado, né?"
    nerkk "Isso me parece meio perigoso, não? Baseado no que o falcão disse."
    ricas "Talvez eu possa ajudar. Lembro-me de um feitiço antigo, o 'Frost-walk'. Ele permite caminhar sobre superfícies aquáticas, solidificando-as momentaneamente sob os pés."
    nerkk "Você consegue fazer isso?!"
    ricas "Vou tentar ensinar o básico. Concentre sua energia nos pés, visualize o gelo se tornando mais forte sob você."

    "Após algum tempo de instrução e prática, vocês conseguem dominar o básico do Frost-walk."
    
    ricas "Pronto. Com cuidado, conseguiremos atravessar."
    nerkk "Incrível, Kuracier!"

    "Vocês atravessam o lago congelado com a nova habilidade."

    pagesh "Bem, o lago não me pareceu tão perigoso quanto o falcão falou. A floresta deve ser moleza"

    jump chegada_castelo


label tp_floresta:
    scene floresta

    show nerkk at right
    show ricardo:
        xpos 0.6
        ypos 0.3
    show Pagesh:
        xpos 0.1
        ypos 0.3
    hide falcao_parado
    with dissolve


    ricas "Um teleporte? É arriscado, Nerkk. Podemos parar em qualquer lugar."
    nerkk "Mas pode nos poupar muito tempo! Vamos tentar!"

    pause 0.5
    show auak at left

    auak "Ufa... consegui alcançar vocês. Um passaro estranho me falou que estavam me esperando para teleportar..."
    nerkk "Pode confiar."
    auak "Lá vem..."

    ricas "Certo, segure-se. Vou tentar nos levar para um ponto mais avançado da floresta..."
    "Kuracier se concentra, e uma luz envolve vocês. Por um instante, tudo gira."
    "Quando a luz se dissipa, vocês se veem no meio de um caos."
    jump evento_fenix

    
label caminho_floresta:
    scene floresta_densa

    show nerkk at right
    show ricardo:
        xpos 0.6
        ypos 0.3
    show Pagesh:
        xpos 0.1
        ypos 0.3
    
    hide falcao_parado
    with dissolve

    pause 0.5

    show auak at left

    auak "Ufa... consegui alcançar vocês. Vamos pela floresta, né? Um pássaro estranho me falou que esse era o melhor caminho mesmo"
    nerkk "Vamos pela floresta mesmo. Parece mais seguro."
    pagesh "Cuidado onde pisam e com o que tocam."
    "Vocês adentram mais a fundo na floresta. Após alguma caminhada, encontram árvores com frutas exóticas e brilhantes."
    
    jump Frutas

label Frutas:
    
    scene floresta_fruta

    show nerkk at right
    show auak at left
    show ricardo:
        xpos 0.6
        ypos 0.3
    show Pagesh:
        xpos 0.1
        ypos 0.3

    ricas "Olha!!! Que frutas são essas? Parecem uma delícia...."
    pagesh "Desconfio de coisas que brilham demais na natureza, Ricas."

    menu comer_fruta_escolha:
        "Comer a fruta mágica.":
            jump comer_fruta_magica
        "Não comer a fruta e seguir em frente.":
            jump nao_comer_fruta_magica


label comer_fruta_magica:

    ricas "Ah, qual é o problema? Só uma mordidinha..."
    "Ricas pega uma fruta e a morde."
    "Quase que instantaneamente, Ricas começa a passar mal, engasgando e caindo ao chão."


    hide ricardo
    show ricardo morto at center
    with fade

    pagesh "NÃO! O que você fez?!"

    "É tarde demais. A fruta era fatalmente venenosa."

    nerkk "Se ao menos o professor estivesse aqui, talvez soubesse o que fazer..." 
    
    "Um de seus companheiros pereceu. A jornada não pode continuar assim."

    "FIM DE JOGO."
    jump caminho_floresta

label nao_comer_fruta_magica:

    ricas "Que saco, eu queria tanto comer ela."
    nerkk "Melhor não arriscar."
    "Vocês ignoram as frutas e seguem caminho, mas logo à frente, o ar começa a esquentar e um brilho intenso surge."
    jump evento_fenix


label evento_fenix:
    scene Fenix 
    show nerkk at right
    show ricardo at left
    show auak:
        xpos 0.6
        ypos 0.3
    show Pagesh:
        xpos 0.1
        ypos 0.3

    "O ar se enche de cinzas e o calor é abrasador. Chamas mágicas, como uma tempestade invocada por uma Fênix, cercam vocês!"

    hide nerkk
    hide ricardo
    hide auak
    hide Pagesh
    with fade

    show nerkk ataque at right
    show ricardo ataque at left
    show auak ataque:
        xpos 0.5
        ypos 0.3
    show Pagesh ataque:
        xpos 0.3
        ypos 0.3


    ricas "Droga! Era uma armadilha.É um guardião elemental!"
    nerkk "Precisamos fazer alguma coisa, e rápido!"
    pagesh "Minha magia pode ajudar, mas precisamos escolher o elemento certo!"

    menu magia_contra_fenix:
        "Usar Magia de Vento para tentar dispersar as chamas." if True:
            jump usar_magia_vento
        "Usar Magia de Água para tentar apagar o fogo." if True:
            jump usar_magia_agua

label usar_magia_vento:

    pagesh "Me ajudem! Não vou conseguir sozinho!"
    pagesh "Ventos, obedeçam-me! Dispersem estas chamas!"
    "Pagesh conjura uma forte rajada de vento, mas para seu horror, o vento apenas alimenta o fogo mágico, que cresce ainda mais intenso e consumidor."
    nerkk "Pagesh, está piorando!"
    pagesh "Não... não pode ser!"
    "As chamas se tornam incontroláveis, e tudo ao redor é engolido pelo fogo."
    
    "Parece que crianças em um mundo mágico não entendem nada de ciência mundana..."
    
    "FIM DE JOGO. Todos sucumbem às chamas."
    
    jump evento_fenix

label usar_magia_agua:

    pagesh "Me ajudem! Não vou conseguir sozinho!"
    pagesh "Espíritos da água, ajudem-nos! Apaguem este inferno!"
    "Pagesh invoca uma torrente de água mágica que colide com as chamas da fênix."
    "Vapor escaldante sobe por toda parte, mas a água começa a subjugar o fogo."
    nerkk "Está funcionando!"
    "Com esforço, Pagesh e seus amigos conseguem extinguir a maior parte do perigo, abrindo um caminho."
    pagesh "Ufa... essa foi por pouco. Vamos sair daqui antes que algo mais aconteça."
    jump chegada_castelo


label chegada_castelo:
    jump cap_4start
