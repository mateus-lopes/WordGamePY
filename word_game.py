# mateus-lopes -> https://github.com/mateus-lopes
""" WORD GAME """
from sys import exit
from random import shuffle, choice

print('\nBem vindo ao Word Game, um jogo de raciocínio que irá aumentar seu vocabulario rapidamente.\n')
print('Responda as perguntas com S/N para logar ou criar uma conta.')
print('Em caso de duvidas acesse "Ajuda" no menu de configurações')

# config database
author = 'mateus-lopes -> https://github.com/mateus-lopes'
points = 0

db = {
    'topics' : {
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
    },
    'users': [
        {
            'id': 'ABC123',
            'nickname':'mateus-lopes',
            'password':'mateus',
            'points': '0',
        },
    ]
}

def main(db):
    global points
    topics = db['topics']

    # log_in

    # create_user

    def get_account():
        account = input('\nÉ sua primeira vez no word game? ')
        user = {}
        while True:
            if account.lower() == "s":
                print('\nCrie sua Conta\n')
                user['nickname'] = input('Digite seu nome de usuário: ')
                user['password'] = input('Digite sua senha: ')
                user['confirm_password'] = input('Confirme sua senha: ')
                start_navbar(user)
            elif account.lower() == "n":
                print('\nLogin\n')
                user['nickname'] = input('Digite seu nome de usuário: ')
                user['password'] = input('Digite sua senha: ')
                start_navbar(user)
            else:
                print("comando não detectado")
                account = input('\nÉ sua primeira vez no word game? ')
    
    def start_game(user, topics, choose_difficulty, choose_topic):
        global points
        
        # funções de suporte 
        def shuffle_word(string):
            for i in string:
                scrambled_word.append(i)
            shuffle(scrambled_word)
            return " ".join(scrambled_word)

        def return_points(p):
            global points
            points += p
            return 'vc recebeu mais {} pontos ficando com {}'.format(p , points)
        
        # configuração inicial de partida
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


        # apresentando a palavra selecionada
        word = choice(topics[choose_topic][choose_difficulty]) 
        scrambled_word = []
        print('\n--- [ {} ] --- '.format(shuffle_word(word).upper()))

        # config tentativas
        resultado, c, tentativa = False, 0, ""
        while c < 7:
            c += 1
            if tentativa.lower() == word.lower():
                resultado = True
                break
            else:
                if c < 6:
                    if c != 5:
                        print("\nVocê ainda tem {} chances".format(str(6 - c)))
                    else:
                        print("\nÚltima Tentativa!")
                    tentativa = input("Tentativa numero {}: ".format(c))

        
        # config resultado
        sentences_replay = [
            "Poxa não foi dessa vez... Tente mais uma vez",
            "Vamos lá, você consegue!",
            "Nossa passou perto...",
        ]
        if resultado:
            print("\nVocê Conseguiu!!! - na {} tentaviva\n".format(c - 1))
            if (c) == 1:
                return_points(50)
            elif (c) == 2:
                return_points(40)
            elif (c) == 3:
                return_points(30)
            elif (c) == 4:
                return_points(20)
            else:
                return_points(10)
        else:
            print("\n" + choice(sentences_replay) + "\n")
            print("A palavra era -- {} --".format(word))

        # config para jogar denovo
        replay = input("\nQuer jogar denovo? (S/N): ")
        while True:
            if replay.lower() == "s":
                change_options = input("Deseja alterar as configurações do jogo? (S/N) ")
                if change_options.lower() == "s":
                    start_game(user, topics, choose_difficulty=False, choose_topic=False)
                else:
                    start_game(user, topics, choose_difficulty, choose_topic)
            elif replay.lower() == "n":
                start_navbar(user)
            else:
                print("comando não detectado")
                replay = input("\nQuer jogar denovo? (S/N): ")

    def start_options(user):
        global points

        # menu de opções
        print('\n-- Configurações --')
        print('\n1 - Perfil')
        print('\n2 - Zerar Pontuação')

        print('\n3 - Creditos')
        print('\n4 - Voltar')
        select = input('\nSelecione: ')

        # config options
        while True:
            if select =='1':
                print("\n" + ('*' * 14))
                print("    Perfil")
                print('*' * 14)
                print('\nNickname - [ {} ]'.format(user['nickname']))
                print('Points - [ {} ]'.format(points))
                input('\nvoltar ')
                start_navbar(user)
            elif select =='2':
                print('\nPontuação Zerada')
                points = 0
                start_navbar(user)
            elif select =='3':
                print("\n" + ('*' * 14))
                print("   Creditos")
                print('*' * 14)
                print('\nAutor - [ {} ]'.format(author))
                input('\nvoltar ')
                start_navbar(user)
            elif select =='4':
                start_navbar(user)
            else:
                print("comando não detectado")
                select = input('\nselecione: ')

    def start_navbar(user):
        # menu de jogo
        print("\n-- Menu de Jogo --")
        print('\n1 - Jogar')
        print('\n2 - Ver Pontuação Atual')
        print('\n3 - Opções')
        print('\n4 - Sair')
        selection = input("\nSelecione: ")

        # config options
        while True:
            if selection == "1":
                start_game(user, topics, choose_difficulty=False, choose_topic=False)
            elif selection == "2":
                string_points = 'você tem {} pontos'.format(points)
                print('\n' + '*' * len(string_points))
                print('\n{}'.format(string_points))
                print('\n' + '*' * len(string_points))
                start_navbar(user)
            elif selection == "3":
                start_options(user)
            elif selection == "4":
                print("\nexit\n")N
                exit()
            else:
                print("comando não detectado")
                selection = input("\nSelecione: ")
    
    get_account()
    

if __name__ == "__main__":
    main(db)
