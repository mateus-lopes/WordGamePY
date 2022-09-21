# mateus-lopes -> https://github.com/mateus-lopes
""" WORD GAME """
from sys import exit
from random import shuffle, choice

print('\nBem vindo ao Word Game, um jogo de raciocínio que irá aumentar seu vocabulario rapidamente.\n')
print('Responda as perguntas com S/N para logar ou criar uma conta.')
print('Em caso de duvidas acesse "Ajuda" no menu de configurações')

def get_account():
    global nickname
    account = input('\nÉ sua primeira vez no word game? ')
    while True:
        if account.lower() == "s":
            print('\nCrie sua Conta\n')
            nickname = input('Digite seu nome de usuário: ')
            # password = input('Digite sua senha: ')
            # confirm_password = input('Confirme sua senha: ')
            main()
        elif account.lower() == "n":
            print('\nLogin\n')
            nickname = input('Digite seu nome de usuário: ')
            # password = input('Digite sua senha: ')
            main()
        else:
            print("comando não detectado")
            account = input('\nÉ sua primeira vez no word game? ')

points = 0
nickname = ''
author = 'mateus-lopes -> https://github.com/mateus-lopes'

def main():
    game = True
    topics = {
        "1": {
            "1": [
                'Ema',
                'Naja',
                'Vaca',
                'Zebu',
                'Foca',
                'Rato',
                'Leão'
            ],
            "2": [
                'Hiena',
                'Sagui',
                'Quati',
                'Urubu',
                'Veado',
                'Ovelha',
                'Abelha',
                'Iguana',
                'Impala',
                'Jaguar',
                'Jacaré',
                'Macaco',
                'Perdiz',
                'Raposa',
                'Lagarto',
                'Babuíno'
            ],
            "3": [
                'Kakapo',
                'Cachorro',
                'Sardinha',
                'Papagaio',
                'Golfinho',
                'Queixada',
                'Tartaruga',
                'Musaranho',
                'Hipopótamo',
                'Orangotango',
                'Dragão-de-komodo'
            ]
        },
        "2": {
            "1": [
                'Noz',
                'Açaí',
                'Maçã',
                'Kiwi',
                'Coco',
                'Romã',
            ],
            "2": [
                'Ajarí',
                'Amora',
                'Avelã',
                'Ameixa',
                'Banana',
                'Tomate',
                'Acerola',
                'Laranja',
                'Damasco'
            ],
            "3": [
                'Abacate',
                'Abacaxi',
                'Aboirana',
                'Azeitona',
                'Melancia',
                'Maça Verde',
                'Bergamota',
                'Pêssego do campo',
                'Castanha do Pará'
            ]
        },
        "3": {
            "1": [
                'Ana',
                'Abel',
                'Adão',
                'Diná',
                'Davi',
                'Bela',
                'Caim',
                'César',
                'André',
                'Cristo',
                'Daniel'
            ],
            "2": [
                'Abraão',
                'Calebe',
                'Débora',
                'Isabel',
                'Isaías',
                'Isaque',
                'Ismael',
                'Israel',
                'Eunice',
                'Golias',
                'Itamar',
                'Cláudio',
                'Cléofas',
                'Augusto'
            ],
            "3": [
                'Nicolau',
                'Betânia',
                'Finéias',
                'Ezequiel',
                'Baltasar',
                'Demétrio',
                'Natanael',
                'Benjamim',
                'Zacarias',
                'Zorobabel',
                'Fortunato',
                'Bartolomeu',
                'Quedorlaomer'
            ]
        }
    }

    def start_game(topics, choose_difficulty, choose_topic):
        global points
        if not choose_difficulty and not choose_topic:
            print('\nEscolha a dificuldade')
            print('1 - Iniciante')
            print('2 - Intermediário')
            print('3 - Avançado')
            choose_difficulty = input("Selecione: ")
            print('\nEscolha a dificuldade')
            print('1 - Animais')
            print('2 - Frutas')
            print('3 - Persongens Bíblicos')
            choose_topic = input("Selecione: ")
        print("\n" + ('*' * 14))
        print("  START GAME")
        print('*' * 14)
        print('\ntotal de pontos - [ {} ]'.format(points))

        sentences_replay = [
            "Poxa não foi dessa vez... Tente mais uma vez",
            "Vamos lá, você consegue!",
            "Nossa passou perto...",
        ]

        word = choice(topics[choose_topic][choose_difficulty]) 
        scrambled_word = []

        def shuffle_word(string):
            for i in string:
                scrambled_word.append(i)
            shuffle(scrambled_word)
            return " ".join(scrambled_word)

        print('\n--- [ {} ] --- '.format(shuffle_word(word).upper()))

        resultado, c, tentativa = False, 1, ""

        while c < 7:
            if tentativa.lower() == word.lower():
                resultado = True
                break
            else:
                if c < 6:
                    tentativa = input("\nTentativa numero {}: ".format(c))
                    if c != 5:
                        print("Você ainda tem {} chances".format(str(5 - c)))
            c += 1

        if resultado:
            print("\nVocê Conseguiu!!! - na {} tentaviva\n".format(c - 1))
            if (c - 1) == 1:
                points += 50
                print('vc recebeu mais 50 pontos ficando com ' + str(points))
            elif (c - 1) == 2:
                points += 40
                print('vc recebeu mais 40 pontos ficando com ' + str(points))
            elif (c - 1) == 3:
                points += 30
                print('vc recebeu mais 30 pontos ficando com ' + str(points))
            elif (c - 1) == 4:
                points += 20
                print('vc recebeu mais 20 pontos ficando com ' + str(points))
            else:
                points += 10
                print('vc recebeu mais 10 pontos ficando com ' + str(points))
        else:
            print("\n" + choice(sentences_replay) + "\n")
            print("A palavra era -- {} --".format(word))

        replay = input("\nQuer jogar denovo? (S/N): ")

        while True:
            if replay.lower() == "s":
                change_options = input("Deseja alterar as configurações do jogo? (S/N) ")
                if change_options.lower() == "s":
                    start_game(topics, choose_difficulty=False, choose_topic=False)
                else:
                    start_game(topics, choose_difficulty, choose_topic)
            elif replay.lower() == "n":
                start_navbar()
            else:
                print("comando não detectado")
                replay = input("\nQuer jogar denovo? (S/N): ")

    def start_options():
        global points
        print('\n-- Configurações --')
        print('\n1 - Perfil')
        print('\n2 - Zerar Pontuação')
        print('\n3 - Creditos')
        print('\n4 - Voltar')
        select = input('\nSelecione: ')
        while True:
            if select =='1':
                print("\n" + ('*' * 14))
                print("    Perfil")
                print('*' * 14)
                print('\nNickname - [ {} ]'.format(nickname))
                print('Points - [ {} ]'.format(points))
                input('\nvoltar ')
                start_navbar()
            elif select =='2':
                print('\nPontuação Zerada')
                points = 0
                start_navbar()
            elif select =='3':
                print("\n" + ('*' * 14))
                print("   Creditos")
                print('*' * 14)
                print('\nAutor - [ {} ]'.format(author))
                input('\nvoltar ')
                start_navbar()
            elif select =='4':
                start_navbar()
            else:
                print("comando não detectado")
                select = input('\nselecione: ')

    def start_navbar():
        print("\n-- Menu de Jogo --")
        print('\n1 - Jogar')
        print('\n2 - Ver Pontuação Atual')
        print('\n3 - Opções')
        print('\n4 - Sair')
        selection = input("\nSelecione: ")
        while True:
            if selection == "1":
                start_game(topics, choose_difficulty=False, choose_topic=False)
            elif selection == "2":
                print('\nvocê tem {} pontos'.format(points))
                start_navbar()
            elif selection == "3":
                start_options()
            elif selection == "4":
                print("\nexit\n")
                exit()
            else:
                print("comando não detectado")
                selection = input("\nSelecione: ")

    if game:
        start_navbar()

if __name__ == "__main__":
    get_account()
