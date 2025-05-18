label cap_4start_auak:

    scene castelo

    show nerkk at right
    show auak at left
    show ricardo:
        xpos 0.6
        ypos 0.3
    show Pagesh:
        xpos 0.1
        ypos 0.3
    

    ricas "Finalmente chegamos!"

    pagesh "Mas o que vamos fazer agora?"

    pagesh "O Castelo está em ruinas."

    auak "Mesmo juntos, nós não temos mágia o suficiente para reeguer o castelo."

    nerkk "O professor me deu esse totem."

    scene bg_totem

    pause

    scene castelo

    show nerkk at right
    show auak at left
    show ricardo:
        xpos 0.6
        ypos 0.3
    show Pagesh:
        xpos 0.1
        ypos 0.3

    nerkk "E disse que eu ia saber quando usar..."

    nerkk "O que vocês acham?"

    ricas "Não custa tentar"

    menu:
        "Tentar usar o totem.":
            jump castelo_rebuild_auak

        "Não tentar usar o totem.":

            auak "Acho melhor não, não vai dar em nada mesmo."
            pagesh "É a única opção que temos!"
            ricas "Você precisa fazer isso, agora!"
            auak "OK! Eu vou usar!"
            jump castelo_rebuild_auak

label castelo_rebuild_auak:

    scene castelo_rebuild

    show nerkk at right
    show auak at left
    show ricardo:
        xpos 0.6
        ypos 0.3
    show Pagesh:
        xpos 0.1
        ypos 0.3

    auak "DEU CERTO!!"
    ricas "Era óbvio que isso ia acontecer."
    ricas "Não sei porque você está tão chocado."

    nerkk "Não temos tempo, vamos entrar."
    pagesh "Right behind you."
    jump castelo_inside_auak

label castelo_inside_auak:
    scene castelo_inside


    show nerkk at right
    show auak at left
    show ricardo:
        xpos 0.6
        ypos 0.3
    show Pagesh:
        xpos 0.5
        ypos 0.3
    "*barulho de portas se fechando*"

    "*sons de corneta*"

    "Quatro desafiantes entraram no castelo."

    "Mas.. quantos irão sair?"

    "*risadas maléficas*"

    pagesh "O que foi isso?"

    ricas "Não faço a menor ideia."

    nerkk "Eu tô quase ficando com medo..."

    pint "Olá visitantes."

    auak "Quem disse isso?"

    nerkk "Você também ouviu?"

    ricas "Acho que veio de dentro dessa pintura (?)"

    show pintura_mulher:
        xpos 0.215
        ypos 0.1

    pint "Você é mais esperto que seus amiguinhos, não é?"

    pint "Não precisam ficar com medo."

    pint "Vocês estão seguros."

    pint "Talvez."

    nerkk "Não temos tempo para conversas."

    nerkk "Só viemos buscar [pronome] [antidoto] e ja estamos indo embora."

    pint "Vocês não acharam que seria tão fácil assim, não é?"

    pagesh "Como assim?"

    pint "Para conseguirem [pronome] [antidoto], vocês terão que completar o seguinte desafio."

    pint "O desafio se trata de uma charada."

    pint "O que é, o que é: quanto mais é pedida, menos valor tem?"

    pagesh "Ah.. essa é muito fácil."
    
    pagesh "A resposta é..."

    pagesh "Pizza!!"

    "*barulho de magia*"

    hide Pagesh
    show fuinha:
        xpos 0.5
        ypos 0.4

    pint "Seu tolo!!"

    pint "Você errou a charada e pagou a consequência."

    nerkk "POR MERLIM O QUE ACONTECEU????!!!"

    auak "O Pagesh foi transformado numa fuinha, não tá vendo?"

    ricas "E agora o que vamos fazer?"

    auak "A gente tem que acertar a charada."

    ricas "Eu acho que a resposta é:"

    ricas  "Marmelada?"

    "*barulho de magia ainda mais intensa que antes*"

    hide ricardo
    show ricardo morto:
        xpos 0.6
        ypos 0.3
    
    pint "Não brinquem comigo crianças."

    pint "Eu posso manter todos vocês nesse castelo, junto comigo."

    pint "PARA SEMPRE!!"

    auak "Por favor se acalme moça da pintura!"

    auak "Eu vou responder mas..."

    auak "Você tem que:"

    menu:
        "Você tem que:"
        "Trazer meus amigos de volta.":
            jump bad_ending_auak
        
        "Me fazer ser o mais poderoso mago que já existiu.":
            jump finale_auak
        
        "Matar todos os meus inimigos.":
            jump bad_ending_auak
        
        "Me transformar em imortal.":
            jump bad_ending_auak

label bad_ending_auak:
    pint "Hmmm.... Acho que depende apenas de você. Você tem que acertar a charada."

    auak "Não sei... Amizade?"

    hide auak 

    "Você morreu. Tente novamente."
    jump castelo_inside_auak

label finale_auak:
    scene castelo_inside

    show pintura_mulher:
        xpos 0.215
        ypos 0.1
    show nerkk at right
    show auak ataque at left
    show fuinha:
        xpos 0.5
        ypos 0.4
    show ricardo morto:
        xpos 0.6
        ypos 0.3
    
    

    auak "Você tem que me fazer o mago mais poderoso que o mundo já viu."

    nerkk "O que você tá fazendo Auak?"

    auak "O que eu vim aqui fazer."

    auak "Tudo que aconteceu foi para trazer a gente aqui. Eu só precisava do totem para reerguer esse castelo. E o jeito mais fácil de consegui-lo?"

    auak "Causar o caos na escola. Nem precisei pedir ao professor."

    nerkk "Como assim Auak?!"

    auak "Você vai ter duas opções: mostrar sua lealdade para mim ou morrer."

    pint "Você acertou a charada."

    pint "A resposta era: Lealdade."

    pint "Por conta do seu ato genuíno de lealdade."

    pint "Eu vou torná-lo no ser mágico mais poderoso que o mundo já viu."

    "*magia ensurdecedora*"

    hide auak
    with dissolve
    show auak super at left
    with dissolve

    menu:
        "O que fazer?"

        "Deixá-los ir.":
            jump bad_ending2_auak
        
        "Acabar com eles!":
            jump luta_final_auak

label luta_final_auak:

    scene castelo_inside

    show auak super at left

    show nerkk ataque at right

    show fuinha:
        xpos 0.5
        ypos 0.3
    
    

    nerkk "Eu não quero fazer isso Auak, sai da frente."

    auak "Eu quero, e muito!"

    "*barulhos intensos de luta*"

    pagesh "Como ele pode ser tão forte assim?"

    nerkk "Faz sentido. Se ele está por trás de tudo isso."

    nerkk "Ele deve ser muito mais poderoso do que nós achamos."

    auak "Graças ao Rotiv eu desbloqueei meu verdadei potencial usando amplificadores de magia."

    auak "Mas agora com essa forma, vocês não podem me deter."

    ricas "Isso não é ilegal?"

    nerkk "Sim, amplificadores de magia roubam a magia de magos ao redor, e permite que você use como a sua própria."

    nerkk "Isso é sujo, Auak"

    auak "Eu não me importo desde que signifique que eu tenha poder máximo."

    pagesh "Como podemos derrotar ele assim?"

    nerkk "Se dermos tudo de si, nosso esforço será recompensado."

    nerkk "Honestamente."

    nerkk "A gente consegue vencer."

    nerkk "Ele não tá com nada."

    "*magia da amizade entrando em ação.*"

    hide nerkk ataque
    hide fuinha

    auak "HAHAHAHAHAH. Pobres coitados."

    auak "Agora nada poderá me deter."

    auak "Com a escola em apuros e com esse poder, eu serei invencível."

    "FIM DE JOGO"

    return


label bad_ending2_auak:
    auak "Vocês podem ir."

    nerkk "Vamos Pagesh! Ainda vamos conseguir salvar a escola."

    scene bg_exterior_saladeaula

    show professor grande abaixado at left

    prof "Onde ele está?!!!"

    show nerkk at right
    show fuinha:
        xpos 0.6
        ypos 0.4

    nerkk "Aqui está prof!!"

    nerkk "[pronome] [antidoto] coming right up!"

    prof "Muito obrigado Nerkk, você salvou a escola!"

    prof "Onde está Auak? E quem é essa fuinha?"

    nerkk "O Auak se tornou um ser muito perigoso professor. Sozinhos não tinhamos chance de vencer."

    prof "Para saber a verdadeira natureza de alguém, dê-lhe poder. Agora com a escola reestaurada, pode ter certeza que ele sofrerá com as consequências."

    pagesh "Ainda bem. Meu amigo Kuracier se foi para sempre. "

    prof "Não tema, jovem. Seu amigo será vingado."

    "FIM DE JOGO"

    return 
    

            
