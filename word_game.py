# mateus-lopes -> https://github.com/mateus-lopes
# lucasxaviervieira -> https://github.com/lucasxaviervieira

""" WORD GAME """
import sys
from random import shuffle, choice
from functions.manage import users, words, topics, difficulty

topic = {
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
    "mateus-lnopes -> https://github.com/mateus-lopes",
    "lucasxaviervieira -> https://github.com/lucasxaviervieira ",
]


def main():
    print(
        "\nBem vindo ao Word Game, um jogo de raciocínio que irá aumentar seu vocabulário rapidamente.\n"
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
            is_account_available = users.available_account(nickname)
            if password != confirm_password:
                is_account_available = False
                print("\nAs senhas não são iguais...")
            if is_account_available:
                users.create_account(nickname, password)
                id = users.get_id(nickname)
                game(id)
            else:
                register_user()

        def login_user():
            print("\nLogin\n")
            nickname = input("Digite seu nome de usuário: ")
            password = input("Digite sua senha: ")
            is_account = users.is_account(nickname, password)
            if is_account:
                print("\nconta acessada com sucesso!\n")
                print("User:", nickname, password)
                id = users.get_id(nickname)
                game(id)
            else:
                print("\nconta não existe")
                get_account()

        get_account()

    def game(id):
        def start_game(topic, choose_difficulty, choose_topic):
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
                choose_topic = input("Selecione: ")
            print("\n" + ("*" * 14))
            print("  START GAME")
            print("*" * 14)
            print("\ntotal de pontos - [ {} ]".format(users.show_points(id)))

            sentences_replay = [
                "Poxa não foi dessa vez... Tente mais uma vez",
                "Vamos lá, você consegue!",
                "Nossa passou perto...",
            ]

            word = choice(topic[choose_topic][choose_difficulty])
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

            if result:
                print("\nVocê Conseguiu!!! - na {} tentaviva\n".format(c))
                if c == 1:
                    users.sum_points(id, 50)
                    print(
                        "vc recebeu mais 50 pontos ficando com "
                        + str(users.show_points(id))
                    )
                elif c == 2:
                    users.sum_points(id, 40)
                    print(
                        "vc recebeu mais 40 pontos ficando com "
                        + str(users.show_points(id))
                    )
                elif c == 3:
                    users.sum_points(id, 30)
                    print(
                        "vc recebeu mais 30 pontos ficando com "
                        + str(users.show_points(id))
                    )
                elif c == 4:
                    users.sum_points(id, 20)
                    print(
                        "vc recebeu mais 20 pontos ficando com "
                        + str(users.show_points(id))
                    )
                else:
                    users.sum_points(id, 10)
                    print(
                        "vc recebeu mais 10 pontos ficando com "
                        + str(users.show_points(id))
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
                        start_game(topic, choose_difficulty=False, choose_topic=False)
                    else:
                        start_game(topic, choose_difficulty, choose_topic)
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
                    print("\n" + ("*" * 14))
                    print("    Perfil")
                    print("*" * 14)
                    print("\nNickname - [ {} ]".format(users.show_nickname(id)))
                    print("Points - [ {} ]".format(users.show_points(id)))
                    input("\nvoltar ")
                    start_navbar()
                elif select == "2":
                    print("\nPontuação Zerada")
                    users.delete_points(id)
                    start_navbar()
                elif select == "3":
                    print("\n" + ("*" * 14))
                    print("   Creditos")
                    print("*" * 14)
                    print(
                        "\nAutores:\n{}\n{}".format((authors[0]), (authors[1])),
                    )
                    input("\nvoltar ")
                    start_navbar()
                elif select == "4":
                    start_navbar()
                elif select == "5":
                    word = input("\nPalavra para adicionar: ")
                    topic = topics.show_topics()
                    print(topic)
                    topic = input("\nDigite o nome do tópico para escolher: ")
                    words.add_word(word, topic)
                    # topics.use_topic(topic_id)
                    # ^^^ escolher o topíco pelo id ao inves de escrever o nome ^^^
                elif select == "6":
                    print(topics.show_topics())
                    topic_id = int(input("\nSelecione o tópico pelo número: \n"))
                    print(difficulty.show_diff())
                    diff_id = int(input("\nSelecione a dificuldade pelo número: \n"))
                    print(words.get_word_filtered(topic_id, diff_id))
                else:
                    print("comando não detectado")
                    select = input("\nselecione: ")

        def start_navbar():
            print("\n-- Menu de Jogo --")
            print("\n1 - Jogar")
            print("\n2 - Ver Pontuação Atual")
            print("\n3 - Opções")
            print("\n4 - Fechar jogo")
            selection = input("\nSelecione: ")
            while True:
                if selection == "1":
                    start_game(topic, choose_difficulty=False, choose_topic=False)
                elif selection == "2":
                    print("\nvocê tem {} pontos".format(users.show_points(id)))
                    start_navbar()
                elif selection == "3":
                    start_options()
                elif selection == "4":
                    print("\nexit\n")
                    sys.exit()
                else:
                    print("comando não detectado")
                    selection = input("\nSelecione: ")

        start_navbar()

    current_account()


if __name__ == "__main__":
    main()
