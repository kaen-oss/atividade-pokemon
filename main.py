from classePokemon import *
from classeTreinador import *
import random
def ganhar_xp(self, valor):
    self.xp += valor
    if self.xp >= 100:
        self.xp -= 100
        self.nivel += 1
        self.hp += 10
        self.atk += 5
        self.defesa += 5
        print(f"{self.especie} subiu para o nível {self.nivel}!")
def batalhaPokemon(self, meuPokemon, inimigo):
    print("----- BATALHA INICIADA -----")

    print(f"{meuPokemon.especie} X {inimigo.especie}")
    print()
    turnos = 1
    
    hpMax = meuPokemon.hp
    
    while (meuPokemon.hp > 0 and inimigo.hp > 0):
        print(f"----- TURNO {turnos} -----")
        meuPokemon.atacar(inimigo)

        if (inimigo.hp <= 0):
            print(f"{inimigo.especie} desmaiou!")
            print(f"{meuPokemon.especie} venceu a batalha contra {inimigo.especie}")
            meuPokemon.hp = hpMax
            meuPokemon.ganhar_xp(15)
            if self.xp >= 100:
                print("Seu pokémon evoluiu!")
            break
        
        inimigo.atacar(meuPokemon)

        if (meuPokemon.hp <= 0):
            print(f"{meuPokemon.especie} desmaiou!")
            print(f"{inimigo.especie} venceu a batalha contra {meuPokemon.especie}")
            meuPokemon.hp = hpMax
            break
        turnos += 1

def gerarPokemonAleatorio():
    numeroPokedex = random.randint(1, 10)

    dados = pokedex[numeroPokedex]

    pokemonAleatorio = Pokemon(numeroPokedex, dados["especie"], dados["tipo"], dados["hp"], dados["atk"], dados["defesa"])
    print("VOCÊ ENCONTROU UM POKEMON!")
    pokemonAleatorio.mostrarInformacoes()
    return pokemonAleatorio

pokedex = {
    1:  {"especie": "Bulbasaur",    "tipo": "Grama/Veneno", "hp": 45,  "atk": 49,  "defesa": 49,"xp": 0,"nivel": 5},
    2:  {"especie": "Ivysaur",      "tipo": "Grama/Veneno", "hp": 60,  "atk": 62,  "defesa": 63,"xp": 0,"nivel": 5},
    3:  {"especie": "Venusaur",     "tipo": "Grama/Veneno", "hp": 80,  "atk": 82,  "defesa": 83,"xp": 0,"nivel": 5},
    4:  {"especie": "Charmander",   "tipo": "Fogo",         "hp": 39,  "atk": 52,  "defesa": 43,"xp": 0,"nivel": 5},
    5:  {"especie": "Charmeleon",   "tipo": "Fogo",         "hp": 58,  "atk": 64,  "defesa": 58,"xp": 0,"nivel": 5},
    6:  {"especie": "Charizard",    "tipo": "Fogo/Voador",  "hp": 78,  "atk": 84,  "defesa": 78,"xp": 0,"nivel": 5},
    7:  {"especie": "Squirtle",     "tipo": "Água",         "hp": 44,  "atk": 48,  "defesa": 65,"xp": 0,"nivel": 5},
    8:  {"especie": "Wartortle",    "tipo": "Água",         "hp": 59,  "atk": 63,  "defesa": 80,"xp": 0,"nivel": 5},
    9:  {"especie": "Blastoise",    "tipo": "Água",         "hp": 79,  "atk": 83,  "defesa": 100,"xp": 0,"nivel": 5},
    10: {"especie": "Caterpie",     "tipo": "Inseto",       "hp": 45,  "atk": 30,  "defesa": 35,"xp": 0,"nivel": 5},
}

jogador = Jogador("Tarik", [])

print("Bem vindo ao mundo Pokemon!")

print("Para começar sua jornada você precisa de um parceiro!")

print()

print('''Escolha um Pokemon abaixo:
      
      
1. Charmander
2. Bulbasaur
3. Squirtle
      
''')

op = input("Digite o número do pokemon desejado: ")

if op == "1":
    pokemonInicial = Pokemon(4,"Charmander", "Fogo", 120, 20, 20, 0, 5)
elif op == "2":
    pokemonInicial = Pokemon(1, "Bulbasaur", "Grama", 100, 20, 20, 0, 5)
elif op == "3":
    pokemonInicial = Pokemon(7, "Squirtle", "Água", 100, 20, 20, 0, 5)
else:
    pokemonInicial = Pokemon(25, "Pikachu", "Elétrico", 100, 20, 20)
    print("Infelizmente esse pokemon não está mais disponível. Você receberá um Pikachu!")

jogador.capturarPokemon(pokemonInicial)

while True:
    print('''
Escolha uma opção do menu abaixo:
          
          1. Capturar Pokemon Aleatório
          2. Batalhar contra Pokemon Aleatório
          3. Ver Pokemons Capturados
          0. Sair

''') 
    op = input("Digite a opção desejada: ")

    if op == "1":
        jogador.capturarPokemon(gerarPokemonAleatorio())
    elif op == "2":
        batalhaPokemon(jogador.escolherPokemon(), gerarPokemonAleatorio())
    elif op == "3":
        jogador.verPokemons()
    elif op == "0":
        print("Você acorda do coma... Foi tudo um sonho... FIM DE JOGO")
        break
    else:
        print("Escolha uma opção válida!")

    input("DIGITE ENTER PARA CONTINUAR")