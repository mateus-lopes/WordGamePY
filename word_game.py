# mateus-lopes -> https://github.com/mateus-lopes
# lucasxaviervieira -> https://github.com/lucasxaviervieira

""" WORD GAME """
import sys
from random import shuffle, choice

from functions import manage_db as mn


topics = {
    "1": {
        "1": ["Ema", "Naja", "Vaca", "Zebu", "Foca", "Rato", "Leão"],
        "2": [
            "Hiena",
            "Sagui",
            "Quati",
            "Urubu",
            "Veado",
            "Ovelha",
            "Abelha",
            "Iguana",
            "Impala",
            "Jaguar",
            "Jacaré",
            "Macaco",
            "Perdiz",
            "Raposa",
            "Lagarto",
            "Babuíno",
        ],
        "3": [
            "Kakapo",
            "Cachorro",
            "Sardinha",
            "Papagaio",
            "Golfinho",
            "Queixada",
            "Tartaruga",
            "Musaranho",
            "Hipopótamo",
            "Orangotango",
            "Dragão-de-komodo",
        ],
    },
    "2": {
        "1": ["Noz", "Açaí", "Maçã", "Kiwi", "Coco", "Romã"],
        "2": [
            "Ajarí",
            "Amora",
            "Avelã",
            "Ameixa",
            "Banana",
            "Tomate",
            "Acerola",
            "Laranja",
            "Damasco",
        ],
        "3": [
            "Abacate",
            "Abacaxi",
            "Aboirana",
            "Azeitona",
            "Melancia",
            "Maça Verde",
            "Bergamota",
            "Pêssego do campo",
            "Castanha do Pará",
        ],
    },
    "3": {
        "1": [
            "Ana",
            "Abel",
            "Adão",
            "Diná",
            "Davi",
            "Bela",
            "Caim",
            "César",
            "André",
            "Cristo",
            "Daniel",
        ],
        "2": [
            "Abraão",
            "Calebe",
            "Débora",
            "Isabel",
            "Isaías",
            "Isaque",
            "Ismael",
            "Israel",
            "Eunice",
            "Golias",
            "Itamar",
            "Cláudio",
            "Cléofas",
            "Augusto",
        ],
        "3": [
            "Nicolau",
            "Betânia",
            "Finéias",
            "Ezequiel",
            "Baltasar",
            "Demétrio",
            "Natanael",
            "Benjamim",
            "Zacarias",
            "Zorobabel",
            "Fortunato",
            "Bartolomeu",
            "Quedorlaomer",
        ],
    },
}
authors = [
    "mateus-lopes -> https://github.com/mateus-lopes",
    "lucasxaviervieira -> https://github.com/lucasxaviervieira ",
]


def main():
    print(
        "\nBem vindo ao Word Game, um jogo de raciocínio que irá aumentar seu vocabulario rapidamente.\n"
    )
    print("Responda as perguntas com S/N para logar ou criar uma conta.")
    print('Em caso de duvidas acesse "Ajuda" no menu de configurações')

    def current_account():
        def get_account():
            account = input("\nÉ sua primeira vez no word game? ")
            while True:
                if account.lower() == "s":
                    register_user()
                elif account.lower() == "n":
                    login_user()
                else:
                    print("comando não detectado")
                    account = input("\nÉ sua primeira vez no word game? ")

        def register_user():
            print("\nCrie sua Conta\n")
            nickname = input("Digite seu nome de usuário: ")
            password = input("Digite sua senha: ")
            confirm_password = input("Confirme sua senha: ")
            is_account_available = mn.available_account(nickname)
            if password != confirm_password:
                is_account_available = False
                print("\nAs senhas não são iguais...")
            if is_account_available:
                mn.create_account(nickname, password)
                id = mn.get_id(nickname)
                game(id)
            else:
                register_user()

        def login_user():
            print("\nLogin\n")
            nickname = input("Digite seu nome de usuário: ")
            password = input("Digite sua senha: ")
            is_account = mn.login(nickname, password)
            if is_account:
                print("\nconta acessada com sucesso!\n")
                print("User:", nickname, password)
                id = mn.get_id(nickname)
                game(id)
            else:
                print("\nconta não encontrada")
                get_account()

        get_account()

    def game(id):

        def select_opitions(options, title):
            print('\n{}:'.format(title.capitalize()))
            [print('{} - {}'.format((index+1), option)) for index, option in enumerate(options) ]
            choice = input("Selecione: ")
            return choice

        def print_title(title):
            print("\n" + ("*" * (6+len(title))))
            print('*  {}  *'.format(title.upper()))
            print("*" * (6+len(title)))

        def start_game(topics, choose_difficulty, choose_topic):
            if not choose_difficulty and not choose_topic:
                print("\nEscolha a dificuldade")
                print("1 - Iniciante")
                print("2 - Intermediário")
                print("3 - Avançado")
                choose_difficulty = input("Selecione: ")
                print("\nEscolha o tema")
                print("1 - Animais")
                print("2 - Frutas")
                print("3 - Persongens Bíblicos")
                # choose_topic = select_opitions(['Animais', 'Frutas', 'Persongens Bíblicos'], 'Tema')

            print_title('start game')
            print("\ntotal de pontos - [ {} ]".format(mn.show_points(id)))
            print('\nDescubra a palavra embaralhada')


            word = choice(topics[choose_topic][choose_difficulty])
            scrambled_word = []

            def shuffle_word(string):
                for i in string:
                    scrambled_word.append(i)
                shuffle(scrambled_word)
                return " ".join(scrambled_word)

            print("\n--- [ {} ] --- ".format(shuffle_word(word).upper()))

            result, c, attempt = False, 0, ""

            while c < 5:
                c += 1
                print("\nVocê tem {} chances".format(str(6 - c))) if c != 5 else print(
                    "\nÚltima chance"
                )
                attempt = input("\nTentativa numero {}: ".format(c))
                if attempt.lower() == word.lower():
                    result = True
                    break
            
            sentences_replay = [
                "Poxa não foi dessa vez... Tente mais uma vez",
                "Vamos lá, você consegue!",
                "Nossa passou perto...",
            ]

            if result:
                print("\nVocê Conseguiu!!! - na {} tentaviva\n".format(c))
                if c == 1:
                    mn.sum_points(id, 50)
                    print(
                        "vc recebeu mais 50 pontos ficando com "
                        + str(mn.show_points(id))
                    )
                elif c == 2:
                    mn.sum_points(id, 40)
                    print(
                        "vc recebeu mais 40 pontos ficando com "
                        + str(mn.show_points(id))
                    )
                elif c == 3:
                    mn.sum_points(id, 30)
                    print(
                        "vc recebeu mais 30 pontos ficando com "
                        + str(mn.show_points(id))
                    )
                elif c == 4:
                    mn.sum_points(id, 20)
                    print(
                        "vc recebeu mais 20 pontos ficando com "
                        + str(mn.show_points(id))
                    )
                else:
                    mn.sum_points(id, 10)
                    print(
                        "vc recebeu mais 10 pontos ficando com "
                        + str(mn.show_points(id))
                    )
            else:
                print("\n" + choice(sentences_replay) + "\n")
                print("A palavra era -- {} --".format(word))

            replay = input("\nQuer jogar denovo? (S/N): ")

            while True:
                if replay.lower() == "s":
                    change_options = input(
                        "Deseja alterar as configurações do jogo? (S/N) "
                    )
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
            print("\n-- Configurações --")
            print("\n1 - Perfil")
            print("\n2 - Zerar Pontuação")
            print("\n3 - Creditos")
            print("\n4 - Voltar")
            select = input("\nSelecione: ")
            while True:
                if select == "1":
                    print_title('perfil')
                    print("\nNickname - [ {} ]".format(mn.show_nickname(id)))
                    print("Points - [ {} ]".format(mn.show_points(id)))
                    input("\nvoltar ")
                    start_options()
                elif select == "2":
                    print_title('zerar pontuação')
                    print("\nvocê tem {} pontos".format(mn.show_points(id)))
                    confirm_points = input("\nTem certeza que deseja zerar seus pontos?")
                    if confirm_points.lower() == 's':
                        mn.delete_points(id)
                    start_options()
                elif select == "3":
                    print_title('creditos')
                    print(
                        "\nAutores:\n{}\n{}".format((authors[0]), (authors[1])),
                    )
                    input("\nvoltar ")
                    start_options()
                elif select == "4":
                    start_navbar()
                else:
                    print("comando não detectado")
                    select = input("\nselecione: ")

        def start_navbar():
            print("\n-- Menu de Jogo --")
            print("\n1 - Jogar")
            print("\n2 - Opções")
            print("\n3 - Fechar jogo")
            selection = input("\nSelecione: ")
            while True:
                if selection == "1":
                    start_game(topics, choose_difficulty=False, choose_topic=False)
                elif selection == "2":
                    start_options()
                elif selection == "3":
                    print("\nexit\n")
                    exit()
                else:
                    print("comando não detectado")
                    selection = input("\nSelecione: ")

        start_navbar()

    current_account()


if __name__ == "__main__":
    main()
