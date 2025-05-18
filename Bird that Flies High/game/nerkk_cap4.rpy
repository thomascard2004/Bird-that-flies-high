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

    nerkk "O prof me deu esse totem."

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

    play sound "porta.mp3"    
    "*barulho de portas se fechando*"

    play sound "corneta.mp3"
    "*sons de corneta*"

    "Quatro desafiantes entraram no castelo."

    "Mas.. quantos irão sair?"

    play sound "risada.mp3"
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

    play sound "magia.mp3"
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

    nerkk "A gente tem que acertar a charada."

    ricas "Eu acho que a resposta é:"

    ricas  "Marmelada?"

    play sound "magia.mp3"
    "*barulho de magia ainda mais intensa que antes*"

    hide ricardo
    show ricardo morto:
        xpos 0.6
        ypos 0.3
    
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

    show fuinha:
        xpos 0.5
        ypos 0.4

    show ricardo morto:
        xpos 0.6
        ypos 0.3
    nerkk "Você tem que trazer meus amigos de volta a suas formas originais."

    auak "Você realmente se importa com esses dois que você acabou de conhecer?"

    nerkk "Sim, eu me importo."

    nerkk "Mesmo que nos conheçamos a pouco tempo, as coisas que nós vivemos juntos me fazem ser leal a eles."

    pint "Você acertou a charada."

    pint "A resposta era: Lealdade."

    pint "Por conta do seu ato genuíno de lealdade."

    pint "Eu vou restaurar seus amigos as suas formas originais."

    play sound "magia.mp3"
    "*magia bondosa dessa vez*"

    hide ricardo morto
    show ricardo:
        xpos 0.6
        ypos 0.3
    show fuinha:
        xpos 0.5
        ypos 0.4
    

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

    pint "Espero que consigam resolver o problema de vocês!"

    nerkk "Que ótimo, agora só precisamos levar [pronome] [antidoto] de volta, e tudo estará resolvido."

    auak "Não tão rápido."

    hide auak
    show auak ataque at left

    auak "Vocês não vão a lugar nenhum!"
    
    nerkk "Como assim Auak, para de brincadeira!!"

    nerkk "Temos que voltar logo para salvar a escola!."

    auak "E deixar que vocês acabem com o meu plano?"

    auak "Fácil assim?"

    nerkk "Como assim seu plano?"

    nerkk "Você estava por trás de tudo isso o tempo todo?"

    auak "SIM!"

    auak "Finalmente você entendeu."

    auak "Você foi bem burrinho de acreditar que eu ja fui seu amigo de verdade."

    auak "Agora pode ir tirando o seu cavalinho da chuva."

    auak "Vocês não vão a lugar nenhum."

    pagesh "E agora Nerkk? O que vamos fazer?"

    menu:
        "O que nós vamos fazer?"

        "Vamos nos render.":
            jump bad_ending2
        
        "Nós vamos lutar com ele!":
            jump luta_final
        
        "Iremos sentar e chorar.":
            jump bad_ending2
        
        "Iremos acabar com ele, aqui e agora.":
            jump luta_final

label luta_final:

    scene castelo_inside

    show auak ataque at left

    show nerkk ataque at right

    show fuinha:
        xpos 0.5
        ypos 0.3
    
    show ricardo ataque:
        xpos 0.6
        ypos 0.3

    nerkk "Eu não quero fazer isso Auak, sai da frente."

    auak "Eu quero, e muito!"

    play sound "luta.mp3"
    "*barulhos intensos de luta*"

    ricas "Como ele pode ser tão forte assim?"

    nerkk "Faz sentido. Se ele está por trás de tudo isso."

    nerkk "Ele deve ser muito mais poderoso do que nós achamos."

    auak "Graças ao Rotiv eu desbloqueei meu verdadei potencial usando amplificadores de magia."

    auak "Agora vocês não podem me deter."

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

    hide auak ataque
    show auak deitado at left

    nerkk "Conseguimos."

    nerkk "Aquele que cuida de mim não dorme."

    nerkk "Vamos voltar, amigos."

    ricas "Você completa a missão Nerkk, nós vamos te teletransportar para a escola."

    ricas "E provavelmente vamos desmaiar depois disso."

    scene bg_exterior_saladeaula

    show professor grande abaixado at left

    prof "Onde ele está?!!!"

    show nerkk at right

    nerkk "Aqui está prof!!"

    nerkk "[pronome] [antidoto] coming right up!"

    prof "Muito obrigado Nerkk, você salvou a escola!"

    $ MainMenu(confirm=False)()


label bad_ending:

    scene castelo_inside

    show nerkk at right
    show auak at left
    show fuinha:
        xpos 0.5
        ypos 0.4

    show ricardo morto:
        xpos 0.6
        ypos 0.3

    show pintura_mulher:
        xpos 0.215
        ypos 0.1

    pint "IGNORANTE!"

    pint "Você é um egoísta!"

    pint "Que só pensa em benefício próprio."

    pint "Você e seus amigos merecem perecer."

    jump castelo_inside

label bad_ending2:

    scene castelo_inside

    show pintura_mulher:
        xpos 0.215
        ypos 0.1

    show nerkk at right
    show auak ataque at left

    show fuinha:
        xpos 0.5
        ypos 0.4

    show ricardo:
        xpos 0.6
        ypos 0.3

    nerkk "Não tem nada que a gente possa fazer."

    nerkk "Não sou capaz de lutar contra ele."

    nerkk "Acho que só temos uma opção."

    nerkk "Desistir."

    ricas "Não."

    ricas "Não vamos fazer assim."

    ricas "Nós somos capazes."

    ricas "Você não precisa dele."

    ricas "Você tem a gente agora."

    ricas "A gente consegue!"

    jump luta_final