# label cap_4start:

#     scene castelo

#     show nerkk at right
#     show auak at left
#     show ricardo:
#         xpos 0.6
#         ypos 0.3
    

#     ricas "Finalmente chegamos!"

#     pagesh "Mas o que vamos fazer agora?"

#     pagesh "O Castelo está em ruinas."

#     auak "Mesmo juntos, nós não temos mágia o suficiente para reeguer o castelo."

#     nerkk "O professor me deu esse totem."

#     nerkk "E disse que eu ia saber quando usar..."

#     nerkk "O que vocês acham?"

#     ricas "Não custa tentar"

#     menu:
#         "Tentar usar o totem.":
#             jump castelo_rebuild

#         "Não tentar usar o totem.":

#             auak "Acho melhor não, não vai dar em nada mesmo."
#             pagesh "É a única opção que temos!"
#             ricas "Você precisa fazer isso, agora!"
#             auak "OK! Eu vou usar!"
#             jump castelo_rebuild

# label castelo_rebuild:

#     scene castelo_rebuild

#     show nerkk at right
#     show auak at left
#     show ricardo:
#         xpos 0.6
#         ypos 0.3

#     auak "DEU CERTO!!"
#     ricas "Era óbvio que isso ia acontecer."
#     ricas "Não sei porque você está tão chocado."

#     nerkk "Não temos tempo, vamos entrar."
#     pagesh "Right behind you."
#     jump castelo_inside

# label castelo_inside:
#     scene castelo_inside

#     show nerkk at right
#     show auak at left
#     show ricardo:
#         xpos 0.6
#         ypos 0.3
#     "*barulho de portas se fechando*"

#     "*sons de corneta*"

#     "Quatro desafiantes entraram no castelo."

#     "Mas.. quantos iram sair?"

#     "*risadas maléficas*"

#     pagesh "O que foi isso?"

#     ricas "Não faço a menor ideia."

#     nerkk "Eu tô quase ficando com medo..."

#     pint "Olá visitantes."

#     auak "Quem disse isso?"

#     nerkk "Você também ouviu?"

#     ricas "Acho que veio de dentro dessa pintura (?)"

#     pint "Você é mais esperto que seus amiguinhos, não é?"

#     pint "Não precisam ficar com medo."

#     pint "Vocês estão seguros."

#     pint "Talvez."

#     nerkk "Não temos tempo para conversas."

#     nerkk "Só viemos buscar [pronome] [antidoto] e ja estamos indo embora."

#     pint "Vocês não acharam que seria tão fácil assim, não é?"

#     pagesh "Como assim?"

#     pint "Para conseguirem o [antidoto], vocês teram que completar o seguinte desafio."

#     pint "O desafio se trata de uma charada."

    

            