# label nerkk_start:

#     $ player = "Nerkk"

#     scene bg_saladeaula

#     show professor abaixado at truecenter

#     prof "A anatomia de um mago é bem simples de entender. Ele possui tudo que um humano possui com uma pequena adição."

#     prof "Um mago tem um \"saco\" de magia que funciona como um coração e tem como função bombear magia pelo corpo do mago, assim como o coração bombeia sangue."

#     show auak at right

#     auak "Professor, se a magia é bombeada pelo corpo inteiro, por que precisamos usar as mãos para fazer magia?"

#     prof "Excelente pergunta! Alguém sabe responder?"

#     show nerkk at left

#     nerkk "Eu sei!"
    
#     menu:
#         "Por que precisamos usar as mãos para fazer magia?"

#         "Porque as maõs são a parte mais importante do corpo.":
#             jump errou_1
        
#         "Para canalizar a magia através das mãos.":
#             jump acertou_1

#         "Porque as mãos cresceram geneticamente com propósitos místicos.":
#             jump errou_1
        
#         "Porque as mãos são a parte do corpo que mais entra em contato físico com o mundo.":
#             jump errou_1

# label boom_nerkk:
#     menu:
#         "Escolha uma ação"

#         "Se esconder embaixo das cadeiras!":
#             jump esconder
#         "Ir investigar o que aconteceu.":
#             jump investigar_nerkk
#         "Fazer xixi nas calças de medo.":
#             jump xixi
#         "Mandar auak ir ver o que aconteceu.":
#             jump investigar_auak

# label investigar_nerkk:
#     scene bg_exterior_saladeaula

#     show nerkk at center

#     nerkk "Acho que o barulho veio daqui. Vou dar uma espiada."

#     nerkk "Meu Deus! O que é isso?"

#     menu:
#         "Escolha a causa da explosão."

#         "Foi o Poppotino Griffino.":
#             jump opcao_1
#         "Opção 2.":
#             jump opcao_2
#         "Opção 3.":
#             jump opcao_3
#         "Opção 4.":
#             jump opcao_4
#     return


label nerkk_start:
    $ pts = 0

    scene bg_saladeaula

    show professor abaixado at truecenter

    prof "A anatomia de um mago é bem simples de entender. Ele possui tudo que um humano possui com uma pequena adição."

    prof "Um mago tem um \"saco\" de magia que funciona como um coração e tem como função bombear magia pelo corpo do mago, assim como o coração bombeia sangue."

    show auak at left

    auak "Professor, se a magia é bombeada pelo corpo inteiro, por que precisamos usar as mãos para fazer magia?"

    prof "Excelente pergunta! Alguém sabe responder?"

    show nerkk at right

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

    #nerkk

    label acertou_1:
        $ pts += 1

        prof "Muito bem! Acertou em cheio! As mãos são importantes porque são a forma de canalizar a magia através do corpo, mas existem outras formas de canalizar magia, como varinhas ou outros objetos."
        auak "Como você sabe disso?"
        nerkk "Quando eu era criança meu sonho era ser biólogo mágico."
        jump cena_1
    
    label errou_1:
        prof "Não é bem isso! As mãos são importantes porque são a forma de canalizar a magia através do corpo, mas existem outras formas de canalizar magia, como varinhas ou outros objetos."
        auak "Bem feito, sabe tudo!"
        jump cena_1

label cena_1:

    prof "Como eu ia dizendo, a magia flui pelo corpo inteiro, quando usamos as mãos estamos apenas canalizando a magia em uma parte do corpo em que temos pleno controle."

    prof "Algúem sabe quais são os pré requisitos para realizar uma magia bem sucedida?"

    nerkk "Eu!"

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
    auak "Você deu sorte."
    jump resto_2

label errou_2:
    prof "Isso sempre é importante, mas não é necessário ao realizar uma magia. As únicas coisas que limitam a capacidade mágica de um mago são a sua criatividade e se ele possui magia 
    o suficiente para realizar o ato mágico que deseja."
    auak "Na próxima fica de boca fechada."
    jump resto_2

label resto_2: 
    prof "Se um mago não tiver magia o suficiente para realizar o ato mágico, ele será realizado até o ponto em que o mago cessar
    a canalização de magia."

    auak "O que acontece se a magia de um mago acabar?"

    prof "Ótima pergunta! Para um mago a magia é tão vital para sua saúde quanto o sangue. Quando um mago esgota sua magia,
    ele morre."

    prof "No início dos tempos muitos magos morriam porque cediam toda a sua magia para realizar ações básicas. Então agora,
    vamos falar sobre otimização do uso de magia e métodos para realização de magia segura."

    prof "Vamos dizer que você está numa floresta e deseja criar uma cabana de madeira. Fazer isso \"do nada\" demandaria muita
    magia. É mais inteligente se você usar a madeira das árvores ao redor, ao seu favor."

    auak "Usando telecinese?"

    prof "Você pode chamar assim porque está usando da sua mente para fazer o que você deseja com a madeira, mas no fim das contas telecinese é 
    apenas um jeito que os humanos inventaram de explicar a magia que eles não entendem."

    auak "Professor, eu tenho uma…"

    play sound "boom.mp3"

    nerkk "O que foi isso?"

    prof "Fiquem aqui, eu vou verificar o que foi isso!"

    hide professor abaixado
    with dissolve

    jump boom_nerkk

label boom_nerkk:
    menu:
        "Mandar Auak ir ver o que aconteceu.":
            jump mandar
        "Investigar o que aconteceu.":
            jump investigar_nerkk
        "Se esconder embaixo das cadeiras.":
            jump esconder_nerkk
        "Fazer xixi nas calças de medo.":
            jump xixi

label mandar:
    nerkk "Vai ver o que aconteceu Auak."

    auak "Até estou curioso, mas não quero ir sozinho."

    show professor abaixado at truecenter

    prof "Descobri o motivo da explosão"

    jump acontecimento_1

label investigar_nerkk:
    scene bg_exterior_saladeaula

    show nerkk at center

    nerkk "Acho que o barulho veio daqui. Vou dar uma espiada."

    jump acontecimento_1
    


label esconder_nerkk:
    nerkk "Me avisa quando o professor voltar!"

    hide nerkk
    with dissolve

    auak "Meu Deus, que medroso."

    pause

    show professor abaixado at truecenter
    with dissolve

    prof "Cadê o Nerkk?"

    auak "Ele se escondeu. Vou chamar ele."

    auak "NERK VOLTA AQUI!"

    show nerkk
    with dissolve

    prof "Eu descobri o que foi."

    jump acontecimento_1

label xixi:
    show professor abaixado at truecenter
    with dissolve

    play sound "xixi.mp3"

    prof "Que barulho é esse?"

    nerkk "Nada professor... Conseguiu descobrir o que aconteceu?"

    prof "Engraçado, tá com cheiro de xixi aqui."
    
    prof "Enfim, eu descobri o que aconteceu."
    
    jump acontecimento_1

label acontecimento_1:

    menu:
        "A causa da explosão foi:"

        "O Poppotino Griffino fugiu do curral.":
            $ causa = "Poppotino Griffino"
            $ pronome = "a"
            $ antidoto = "Melancia Dourada"

            jump opcao_1
        "Raízes Mágicas descontroladas sairam da estufa.":
            $ pronome = "o"
            $ antidoto = "Pergaminho"
            jump opcao_2
            
        "Alguém roubou um pergaminho almadiçoado na biblioteca.":
            $ pronome = "o"
            $ antidoto = "Pergaminho"
            jump opcao_3

        "Todos os professores viraram estátua":
            $ pronome = "a"
            $ antidoto = "Lagrima da Medusa"
            jump opcao_4

label opcao_1:
    scene poppotino

    show nerkk at left

    nerkk "É um Poppotino Griffino! Ele gera 5 filhotes por minuto. Se não o pararmos ele pode destruir a escola!"

    show professor at center

    prof "Que bom que você apareceu Nerkk! Vou precisar muito da sua ajuda."

    prof "Com o ataque do Poppotino Griffino eu tenho que ficar aqui tentando conter as gerações de filhotes dele, mas não é o suficiente para salvar a escola."

    prof "Eu preciso que você vá até o castelo desolado de Bacallister e busque a Melancia Dourada. É a única coisa que pode acalmar o Poppotino Griffino."

    prof "Uma última coisa. Leve este totem. Você saberá quando usá-lo."

    prof "Agora vá de uma vez, mas não vá sozinho!"

    scene bg_saladeaula

    show auak at left

    show nerkk at right 
    with dissolve

    nerkk "O professor me mandou em uma missão de encontrar uma melancia dourada para acalmar um Poppotino Griffino. Você vem comigo."

    auak "Como assim? Não entendi nada que você disse."

    nerkk "Eu te explico no caminho...."

    jump cap_2

label opcao_2:
    scene raizes

    show nerkk at left 

    nerkk "São as raízes! Se elas continuarem crescendo vão destruir a escola!"

    show professor at center

    prof "Que bom que você apareceu Nerkk! Vou precisar muito da sua ajuda."

    prof "Com o ataque das raízes eu tenho que ficar aqui tentando conter o crescimento delas, mas não é o suficiente para salvar a escola."

    prof "Eu preciso que você vá até o castelo desolado de Bacallister e busque o pergaminho que contém o feitiço que irá parar de vez o cresimento delas. Sem esse feitiço eu eventualmente esgotarei minha magia tentando atrasar seu cresimento."

    prof "Uma última coisa. Leve este totem. Você saberá quando usá-lo."

    prof "Agora vá de uma vez, mas não vá sozinho!"

    scene bg_saladeaula

    show auak at left

    show nerkk at right 
    with dissolve

    nerkk "O professor me mandou em uma missão de encontrar um pergaminho para parar o cresimento das raízes. Você vem comigo."

    auak "Como assim? Não entendi nada que você disse."

    nerkk "Eu te explico no caminho...."

    jump cap_2

label opcao_3:
    scene biblioteca

    show nerkk at left 

    nerkk "Foi o pergaminho! Alguém o levou! O pergaminho da escola contém seus maiores segredos. Quem o tiver só pode querer destruir a escola."

    show professor at center

    prof "Que bom que você apareceu Nerkk! Vou precisar muito da sua ajuda."

    prof "Com o sumiço do pergaminho eu tenho que ficar aqui tentando encontrá-lo já que eu conheço cada canto desse lugar. Estamos fritos se eu não o encontrar."

    prof "Eu preciso que você vá até o castelo desolado de Bacallister e busque o pergaminho irmão que contém o feitiço que irá destruir o pergaminho dessa escola. Eles ficam separados para permitir que possamos nos defender caso o nosso pergaminho desapareça."

    prof "Uma última coisa. Leve este totem. Você saberá quando usá-lo."

    prof "Agora vá de uma vez, mas não vá sozinho!"

    scene bg_saladeaula

    show auak at left

    show nerkk at right 
    with dissolve

    nerkk "O professor me mandou em uma missão de encontrar um pergaminho para se proteger do sumiço do pergaminho da escola. Você vem comigo."

    auak "Como assim? Não entendi nada que você disse."

    nerkk "Eu te explico no caminho...."


    jump cap_2    

label opcao_4:
    scene professores

    show nerkk at left 

    nerkk "Os professores! Todos viraram estátua! E agora? Como podemos resolver isso?"

    show professor at center

    prof "Que bom que você apareceu Nerkk! Vou precisar muito da sua ajuda."

    nerkk "Professor! Que bom que você está bem! "

    prof "Se eu não estivesse em aula, teria ficado assim também."

    prof "Com os professores todos pretrificados eu tenho que ficar aqui de apoio aos alunos. Muitos irão ficar com medo."

    prof "Eu preciso que você vá até o castelo desolado de Bacallister e busque a lágrima de medusa. Somente com ela podemos trazê-los de volta."

    prof "Uma última coisa. Leve este totem. Você saberá quando usá-lo."

    prof "Agora vá de uma vez, mas não vá sozinho!"

    scene bg_saladeaula

    show auak at left

    show nerkk at right 
    with dissolve

    nerkk "O professor me mandou em uma missão de encontrar a lágrima de medusa para trazer os professores petrificados de volta. Você vem comigo."

    auak "Como assim? Não entendi nada que você disse."

    nerkk "Eu te explico no caminho...."


    jump cap_2    