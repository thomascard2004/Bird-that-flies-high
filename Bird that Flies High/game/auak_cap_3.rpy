label cap_3_auak:

    scene trilha

    show nerkk at right
    show auak at left
    show ricardo:
        xpos 0.6
        ypos 0.3

    auak "Pelas palavras do professor, acho que devemos seguir nessa direção"

    auak "Podem ir indo na frente, eu vou só fazer um xixizinho maroto"

    scene trilha_auak
    with dissolve

    show auak at left

    auak "Agora que estou sozinho, tenho uma escolha a fazer. O único jeito de mandar eles pelo pior caminho é fingir ser outra pessoa. "

    menu:
        "O que você deseja fazer?"

        "Se transformar em ave e mandar o grupo ir pela floresta.":
            jump ave_auak
        "Não se transformar em nada e ir com o grupo pelo lago.":
            jump caminho_lago_auak


label ave_auak:
    
    scene floresta

    show nerkk at right
    show ricardo at left

    "Um súbito bater de asas chama a atenção do grupo."
    show falcao_voando at truecenter
    pause 0.5
    hide falcao_voando
    show falcao_parado at center


    falcao "Bom dia viajantes, como posso ajudá-los?" 
    nerkk "Estamos tentando chegar ao castelo que fica além desta floresta. Sabe o melhor caminho?"


    falcao "Hmm, o castelo..."
    falcao "O lago é extremamente traiçoeiro, rico de criaturas perigosas a morte é certa."
    falcao "A floresta é mais direta, com certeza. Tenho que certeza que obterão sucesso"
    falcao "O que me dizem?"

    nerkk "Acho que vamos pela floresta então. Vamos Auak!"

    hide falcao_parado

    pause

    show auak:
        xpos 0.6
        ypos 0.3

    nerkk "Oi Auak. Decidimos ir pela floresta."

    auak "O que vocês acham de tentar um teleporte? Pode ser que valha a pena. Gaharíamos bastante tempo."

    menu:
        "Gostaria de sugerir o teleporte ao grupo?"
        "Sim":
            jump tp_floresta_auak
        "Não":
            jump caminho_floresta_auak


label caminho_lago_auak:
    scene lago2

    show nerkk at right
    show ricardo at left
    hide falcao_parado
    show auak:
        xpos 0.6
        ypos 0.3    

    auak "Ufa... consegui alcançar voces. Vamos pelo lago né? Um passaro estranho me falou que era meio perigoso..."
    ricas "Ah... ele deve estar exagerando só!"
    nerkk "O lago, então. Como vamos atravessar?"
    pagesh "Bem, sempre tem a opção de atravessar a nado né."
    nerkk "Isso me parece meio perigoso não? Baseado no que o falcão disse."
    ricas "Talvez eu possa ajudar. Lembro-me de um feitiço antigo, o 'Frost-walk'. Ele permite caminhar sobre superfícies aquáticas, solidificando-a momentaneamente sob os pés."
    nerkk "Você consegue fazer isso?!"
    ricas "Vou tentar ensinar o básico. Concentre sua energia nos pés, visualize o gelo se tornando mais forte sob você."

    "Após algum tempo de instrução e prática, vocês conseguem dominar o básico do Frost-walk."
    
    ricas "Pronto. Com cuidado, conseguiremos atravessar."
    nerkk "Incrível, Kuracier!"

    "Vocês atravessam o lago congelado com a nova habilidade."

    pagesh "Bem, o lago não me pareceu tão perigoso quanto o falcão falou. A floresta deve ser moleza."

    jump chegada_castelo_auak


label tp_floresta_auak:
    scene floresta

    show nerkk at right
    show ricardo at left
    show auak:
        xpos 0.6
        ypos 0.3 


    ricas "Um teleporte? É arriscado, Auak. Podemos parar em qualquer lugar."
    nerkk "Mas pode nos poupar muito tempo! Vamos tentar!"
    ricas "Certo, segurem-se. Vou tentar nos levar para um ponto mais avançado da floresta..."
    "Kuracier se concentra, e uma luz envolve vocês. Por um instante, tudo gira."
    "Quando a luz se dissipa, vocês se veem no meio de um caos."
    jump evento_fenix_auak

    
label caminho_floresta_auak:
    scene floresta_densa

    show nerkk at right
    show ricardo at left
    hide falcao_parado
    show auak:
        xpos 0.6
        ypos 0.3

    pagesh "Cuidado onde pisam e com o que tocam."
    "Vocês adentram mais a fundo na floresta. Após alguma caminhada, encontram árvores com frutas exóticas e brilhantes."
    
    jump Frutas_auak

label Frutas_auak:
    
    scene floresta_fruta

    show nerkk at right
    show ricardo at left
    show auak:
        xpos 0.6
        ypos 0.3

    ricas "Olha!!! Que frutas são essas? Parecem uma delícia...."
    pagesh "Desconfio de coisas que brilham demais na natureza, Kuracier."

    menu comer_fruta_escolha_auak:
        "Sugerir comer a fruta mágica.":
            auak "Não deve ter problema nenhum. Pode comer tranquilo Kuracier!"
            jump comer_fruta_magica_auak
        "Não sugerir comer a fruta e seguir em frente.":
            jump nao_comer_fruta_magica_auak


label comer_fruta_magica_auak:

    ricas "Ah, qual é o problema? Só uma mordidinha..."
    "Kuracier pega uma fruta e a morde."
    "Quase que instantaneamente, Kuracier começa a passar mal, engasgando e caindo ao chão."

    hide ricardo
    show ricardo morto at left

    pagesh "NÃO! O que você fez?!"

    "É tarde demais. A fruta era fatalmente venenosa."

    nerkk "Se ao menos o professor estivesse aqui, talvez soubesse o que fazer..." 
    
    "Um de seus companheiros pereceu. A jornada não pode continuar assim."

    "FIM DE JOGO."
    jump caminho_floresta_auak

label nao_comer_fruta_magica_auak:

    ricas "Que saco, eu queria tanto comer ela."
    nerkk "Melhor não arriscar."
    "Vocês ignoram as frutas e seguem caminho, mas logo à frente, o ar começa a esquentar e um brilho intenso surge."
    jump evento_fenix_auak


label evento_fenix_auak:
    scene Fenix 
    show nerkk at right
    show ricardo ataque at left
    show auak:
        xpos 0.6
        ypos 0.3

    "O ar se enche de cinzas e o calor é abrasador. Chamas mágicas, como uma tempestade invocada por uma Fênix, cercam vocês!"
    ricas "Droga! Era uma armadilha, é um guardião elemental!"
    nerkk "Precisamos fazer alguma coisa, e rápido!"
    pagesh "Minha magia pode ajudar, mas precisamos escolher o elemento certo!"

    menu magia_contra_fenix_auak:
        "Usar Magia de Vento para tentar dispersar as chamas." if True:
            jump usar_magia_vento_auak
        "Usar Magia de Água para tentar apagar o fogo." if True:
            jump usar_magia_agua_auak

label usar_magia_vento_auak:

    pagesh "Me ajudem! Não vou conseguir sozinho!"
    pagesh "Ventos, obedeçam-me! Dispersem estas chamas!"
    "Pagesh conjura uma forte rajada de vento, mas para seu horror, o vento apenas alimenta o fogo mágico, que cresce ainda mais intenso e consumidor."
    nerkk "Pagesh, está piorando!"
    pagesh "Não... não pode ser!"
    "As chamas se tornam incontroláveis, e tudo ao redor é engolido pelo fogo."
    
    "Parece que crianças em um mundo mágico não entendem nada de ciência mundana..."
    
    "FIM DE JOGO. Todos sucumbem às chamas."
    
    jump evento_fenix_auak

label usar_magia_agua_auak:

    pagesh "Me ajudem! Não vou conseguir sozinho!"
    pagesh "Espíritos da água, ajudem-nos! Apaguem este inferno!"
    "Pagesh invoca uma torrente de água mágica que colide com as chamas da fênix."
    "Vapor escaldante sobe por toda parte, mas a água começa a subjugar o fogo."
    nerkk "Está funcionando!"
    "Com esforço, Pagesh e seus amigos consegue extinguir a maior parte do perigo, abrindo um caminho."
    pagesh "Ufa... essa foi por pouco. Vamos sair daqui antes que algo mais aconteça."
    jump chegada_castelo_auak


label chegada_castelo_auak:
    jump cap_4start_auak
