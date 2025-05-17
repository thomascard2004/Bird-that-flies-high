label cap_4start:

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

    nerkk "E disse que eu ia saber quando usar..."

    nerkk "O que vocês acham?"

    ricas "Não custa tentar."

    menu:
        "Tentar usar o totem.":
            jump castelo_rebuild

        "Não tentar usar o totem.":

            nerkk "Acho melhor não, não vai dar em nada mesmo."
            pagesh "É a única opção que temos!"
            ricas "Você precisa fazer isso, agora!"
            nerkk "OK! Eu vou usar!"
            jump castelo_rebuild

label castelo_rebuild:

    scene castelo_rebuild

    show nerkk at right
    show auak at left
    show ricardo:
        xpos 0.6
        ypos 0.3
    show Pagesh:
        xpos 0.1
        ypos 0.3

    nerkk "DEU CERTO!!"
    auak "Era óbvio que isso ia acontecer."
    auak "Não sei porque você está tão chocado."

    ricas "Não temos tempo, vamos entrar."
    pagesh "Right behind you."
    jump castelo_inside

label castelo_inside:
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

    pint "Para conseguirem [pronome] [antidoto], vocês teram que completar o seguinte desafio."

    pint "O desafio se trata de uma charada."

    pint "O que é, o que é: quanto mais é pedida, menos valor tem?"

    pagesh "Ah.. essa é muito fácil."
    
    pagesh "A resposta é..."

    pagesh "Pizza!!"

    "*barulho de magia*"

    hide Pagesh
    show fuinha:
        xpos 0.5
        ypos 0.3


    pint "Seu tolo!!"

    pint "Você errou a charada e pagou a consequência."

    nerkk "POR MELIM O QUE ACONTECEU????!!!"

    auak "O Pagesh foi transformado numa fuinha, não tá vendo?"

    ricas "E agora o que vamos fazer?"

    nerkk "A gente tem que acertar a charada."

    ricas "Eu acho que a resposta é:"

    ricas  "Marmelada?"

    "*barulho de magia ainda mais intensa que antes*"

    hide ricardo
    
    pint "Não brinquem comigo crianças."

    pint "Eu posso manter todos vocês nesse castelo, junto comigo."

    pint "PARA SEMPRE!!"

    nerkk "Por favor se acalme moça da pintura!"

    nerkk "Eu vou responder mas..."

    nerkk "Você tem que:"

    menu:
        "Você tem que:"
        "Trazer meus amigos de volta.":
            jump finale
        
        "Me fazer ser o mais poderoso mago que já existiu.":
            jump bad_ending
        
        "Matar todos os meus inimigos.":
            jump bad_ending
        
        "Me transformar em imortal.":
            jump bad_ending

label finale:
    scene castelo_inside

    show pintura_mulher:
        xpos 0.215
        ypos 0.1
    show nerkk at right
    show auak at left
    

    nerkk "Você tem que trazer meus amigos de volta a suas formas originais."

    auak "Você realmente se importa com esses dois que você acabou de conhecer?"

    nerkk "Sim, eu me importo."

    nerkk "Mesmo que nos conheçamos a pouco tempo, as coisas que nós vivemos juntos me fazem ser leal a eles."

    pint "Você acertou a charada."

    pint "A resposta era: Lealdade."

    pint "Por conta do seu ato genuíno de lealdade."

    pint "Eu vou restaurar seus amigos as suas formas originais."

    "*magia bondosa dessa vez*"

    show ricardo:
        xpos 0.6
        ypos 0.3
    show fuinha:
        xpos 0.5
        ypos 0.3
    

    ricas "I'm back bitches!"

    ricas "Ué, cadê o Pagesh?"

    nerkk "Ei, você mentiu pra mim!"

    nerkk "Imaginei que quem admira tanto a lealdade, seria fiel a sua palavra."

    pint "Mas eu realizei uma magia de \"restauração a verdadeira forma\" nele."

    nerkk "Será que isso signfica que..."

    auak "Que ele sempre foi uma fuinha?"

    auak "Sim, é isso que significa."

    ricas "Que doideira."

    pint "Enfim."

    pint "Aqui está [pronome] [antidoto]"



    

            