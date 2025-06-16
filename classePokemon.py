class Pokemon:
    def __init__(self, nroPokedex, especie, tipo, hp, atk, defesa, xp=0, nivel=5):
        self.nroPokedex = nroPokedex
        self.especie = especie
        self.tipo = tipo
        self.hp = hp
        self.atk = atk
        self.defesa = defesa
        self.nivel = 5
        self.xp = 0
        
    def ganhar_xp(self, valor):
        self.xp += valor
        if self.xp >= 100:
            self.xp -= 100
            self.nivel += 1
            self.hp += 10
            self.atk += 5
            self.defesa += 5
            print(f"{self.especie} subiu para o nível {self.nivel}!")
            
    def mostrarInformacoes(self):
        print(f'''
------- Poke Entry -------
              
Número: {self.nroPokedex}
Espécie: {self.especie}
Tipo: {self.tipo}
HP: {self.hp}
ATK: {self.atk}
DEF: {self.defesa} 
NIVEL: {self.nivel}

''')
def calcular_dano(self, inimigo):
    dano = self.atk - (inimigo.defesa // 2)
    return max(1, dano)

def atacar(self, inimigo):
        dano = calcular_dano(self, inimigo)
        inimigo.hp -= dano
        print(f"{self.especie} atacou {inimigo.especie} e causou {dano} de dano!")