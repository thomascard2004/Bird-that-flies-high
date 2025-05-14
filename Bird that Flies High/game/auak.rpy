# label nerkk_start:

    jump cap_4start
    
    $ player = "Auak"

    scene bg_saladeaula

    show professor abaixado at truecenter

    prof "A anatomia de um mago é bem simples de entender. Ele possui tudo que um humano possui com uma pequena adição."

    prof "Um mago tem um \"saco\" de magia que funciona como um coração e tem como função bombear magia pelo corpo do mago, assim como o coração bombeia sangue."

    show nerkk at left

    nerkk "Professor, se a magia é bombeada pelo corpo inteiro, por que precisamos usar as mãos para fazer magia?"

    prof "Excelente pergunta! Alguém sabe responder?"

    show auak at right

    auak "Eu sei!"
    
    menu:
        "Por que precisamos usar as mãos para fazer magia?"

        "Porque as maõs são a parte mais importante do corpo.":
            jump errou_1_auak
        
        "Para canalizar a magia através das mãos.":
            jump acertou_1_auak

        "Porque as mãos cresceram geneticamente com propósitos místicos.":
            jump errou_1_auak
        
        "Porque as mãos são a parte do corpo que mais entra em contato físico com o mundo.":
            jump errou_1_auak

    #nerkk

    label acertou_1_auak:
        $ pts += 1

        prof "Muito bem! Acertou em cheio! As mãos são importantes porque são a forma de canalizar a magia através do corpo, mas existem outras formas de canalizar magia, como varinhas ou outros objetos."
        nerkk "Como você sabe disso?"

	menu:
	    "Deseja responder?":
		"Não responder":
		    jump jump cena_1_auak
		"Responder":
		    jump responder

        
label responder:
    auak "Eu sou muito estudioso. Eu já li sobre tudo o que estamos vendo em sala. Meus objetivos são maiores do que a escola consegue ensinar."

    nerkk "Uau! Você é impressionante."

    jump cena_1_auak
    
label errou_1_auak:
    prof "Não é bem isso! As mãos são importantes porque são a forma de canalizar a magia através do corpo, mas existem outras formas de canalizar magia, como varinhas ou outros objetos."
    
    jump cena_1_auak

label cena_1_auak:

    prof "Como eu ia dizendo, a magia flui pelo corpo inteiro, quando usamos as mãos estamos apenas canalizando a magia em uma parte do corpo em que temos pleno controle."

    prof "Algúem sabe quais são os pré requisitos para realizar uma magia bem sucedida?"

    auak "Eu!"

    menu:
        "Quais são os pré requisitos para realizar uma magia bem sucedida?"

        "Ter criatividade e ter a quantidade de magia necessária com excedente saudável":
            jump acertou_2_auak
        "Calma e paciência":
            jump errou_2_auak
        "Foco e conhecimento":
            jump errou_2_auak
        "Disruptividade e moedas de ouro":
            jump errou_2_auak

label acertou_2_auak:
    prof "Muito bem! Você está corretíssimo! As únicas coisas que limitam a capacidade mágica de um mago são a sua criatividade e se ele possui magia o suficiente para realizar o ato mágico que deseja."
    
    jump resto_2

label errou_2_auak:
    prof "Isso sempre é importante, mas não é necessário ao realizar uma magia. As únicas coisas que limitam a capacidade mágica de um mago são a sua criatividade e se ele possui magia o suficiente para realizar o ato mágico que deseja."
    
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

    jump boom_auak

label boom_auak:
    menu:
        "Fingir que se machucou.":
            jump fingir
        "Investigar o que aconteceu.":
            jump investigar_auak
        "Se esconder embaixo das cadeiras.":
            jump esconder_auak
        "Fazer xixi nas calças de medo.":
            jump xixi_auak

label fingir:
    $ maldade += 1

    show auak deitado

    auak "Nerkk! Me ajuda!"

    nerkk "Meu Deus! Você está bem?"

    auak "Preciso que você me transfira magia! Senão não vou conseguir me curar."

    nerkk "OK! Toma então."

    show thomas transparente

    pause

    show professor abaixado at truecenter
    with dissolve

    prof "Nerkk, o que aconteceu com você?"

    prof "Toma essa manga aqui, ela vai te deixar melhor."

    auak "Descobriu o que aconteceu professor?"

    prof "Descobri."

    jump acontecimento_1

label investigar_auak:
    scene bg_exterior_saladeaula

    show auak at center

    auak "Acho que o barulho veio daqui. Vou dar uma espiada."

    jump acontecimento_1
    


label esconder_auak:
    nerkk "Me avisa quando o professor voltar!"

    hide auak
    with dissolve

    nerkk "Me deixou aqui sozinho."

    pause

    show professor abaixado at truecenter
    with dissolve

    prof "Cadê o Auak?"

    auak "Ele se escondeu. Vou chamar ele."

    auak "AUAK VOLTA AQUI!"

    show auak
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
            jump opcao_1_auak
        "Raízes Mágicas descontroladas sairam da estufa.":
            jump opcao_2_auak
        "Alguém roubou um pergaminho almadiçoado na biblioteca.":
            jump opcao_3_auak
        "Todos os professores viraram estátua":
            jump opcao_4_auak

label opcao_1_auak:
    scene poppotino

    show auak at left

    auak "É um Poppotino Griffino! Ele gera 5 filhotes por minuto. Se não o pararmos ele pode destruir a escola!"

    show professor at center

    prof "Que bom que você apareceu Auak! Vou precisar muito da sua ajuda."

    prof "Com o ataque do Poppotino Griffino eu tenho que ficar aqui tentando conter as gerações de filhotes dele, mas não é o suficiente para salvar a escola."

    prof "Eu preciso que você vá até o castelo desolado de Bacallister e busque a melancia dourada. É a única coisa que pode acalmar o Poppotino Griffino."

    prof "Uma última coisa. Leve este totem. Você saberá quando usá-lo."

    prof "Agora vá de uma vez, mas não vá sozinho!"

    scene bg_saladeaula

    show nerkk at left

    show auak at right 
    with dissolve

    auak "O professor me mandou em uma missão de encontrar uma melancia dourada para acalmar um Poppotino Griffino. Você vem comigo."

    nerkk "Como assim? Não entendi nada que você disse."

    auak "Eu te explico no caminho...."

    jump cap_2_auak

label opcao_2_auak:
    scene raizes

    show auak at left 

    auak "São as raízes! Se elas continuarem crescendo vão destruir a escola!"

    show professor at center

    prof "Que bom que você apareceu Auak! Vou precisar muito da sua ajuda."

    prof "Com o ataque das raízes eu tenho que ficar aqui tentando conter o crescimento delas, mas não é o suficiente para salvar a escola."

    prof "Eu preciso que você vá até o castelo desolado de Bacallister e busque o pergaminho que contém o feitiço que irá parar de vez o cresimento delas. Sem esse feitiço eu eventualmente esgotarei minha magia tentando atrasar seu cresimento."

    prof "Uma última coisa. Leve este totem. Você saberá quando usá-lo."

    prof "Agora vá de uma vez, mas não vá sozinho!"

    scene bg_saladeaula

    show nerkk at left

    show auak at right 
    with dissolve

    auak "O professor me mandou em uma missão de encontrar um pergaminho para parar o cresimento das raízes. Você vem comigo."

    nerkk "Como assim? Não entendi nada que você disse."

    auak "Eu te explico no caminho...."

    jump cap_2_auak

label opcao_3_auak:
    scene biblioteca

    show auak at left 

    auak "Foi o pergaminho! Alguém o levou! O pergaminho da escola contém seus maiores segredos. Quem o tiver só pode querer destruir a escola."

    show professor at center

    prof "Que bom que você apareceu Auak! Vou precisar muito da sua ajuda."

    prof "Com o sumiço do pergaminho eu tenho que ficar aqui tentando encontrá-lo já que eu conheço cada canto desse lugar. Estamos fritos se eu não o encontrar."

    prof "Eu preciso que você vá até o castelo desolado de Bacallister e busque o pergaminho irmão que contém o feitiço que irá destruir o pergaminho dessa escola. Eles ficam separados para permitir que possamos nos defender caso o nosso pergaminho desapareça."

    prof "Uma última coisa. Leve este totem. Você saberá quando usá-lo."

    prof "Agora vá de uma vez, mas não vá sozinho!"

    scene bg_saladeaula

    show nerkk at left

    show auak at right 
    with dissolve

    auak "O professor me mandou em uma missão de encontrar o pergaminho irmão para conter os efeitos do pergaminho roubado da escola. Você vem comigo."

    nerkk "Como assim? Não entendi nada que você disse."

    auak "Eu te explico no caminho...."


    jump cap_2_auak    

label opcao_4_auak:
    scene professores

    show auak at left 

    auak "Os professores! Todos viraram estátua! E agora? Como podemos resolver isso?"

    show professor at center

    prof "Que bom que você apareceu Auak! Vou precisar muito da sua ajuda."

    auak "Professor! Que bom que você está bem! "

    prof "Se eu não estivesse em aula, teria ficado assim também."

    prof "Com os professores todos pretrificados eu tenho que ficar aqui de apoio aos alunos. Muitos irão ficar com medo."

    prof "Eu preciso que você vá até o castelo desolado de Bacallister e busque a lágrima de medusa. Somente com ela podemos trazê-los de volta."

    prof "Uma última coisa. Leve este totem. Você saberá quando usá-lo."

    prof "Agora vá de uma vez, mas não vá sozinho!"

    scene bg_saladeaula

    show nerkk at right

    show auak at left
    with dissolve

    auak "O professor me mandou em uma missão de encontrar a lágrima de medusa para trazer os professores de volta. Você vem comigo."

    nerkk "Como assim? Não entendi nada que você disse."

    auak "Eu te explico no caminho...."


    jump cap_2_auak    